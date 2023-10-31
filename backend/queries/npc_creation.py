from .pool import pool
from models.npc_creation import (
    CreateNPCOut,
    RolePlayingTips,
    UpdateNPCData,
)


class NPCCreationRepo:
    def create_npc(self, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    npc_id = self.insert_npc(db, data)
                    role_playing_tips = self.insert_role_playing_tips(
                        db,
                        data,
                        npc_id,
                    )
                    npc_out = self.create_npc_out(
                        npc_id,
                        data,
                        role_playing_tips,
                    )
                    return npc_out
                except Exception as e:
                    raise e

    def insert_npc(self, db, data):
        npc_db = db.execute(
            """
            INSERT INTO npc (name, race, personality, physical_description)
            VALUES (%s, %s, %s, %s)
            RETURNING id
            """,
            [
                data["name"],
                data["race"],
                data["personality"],
                data["physical_description"],
            ],
        )
        npc = npc_db.fetchone()
        return npc[0]

    def update_role_playing_tips(self, db, data, npc_id):
        data = data.dict()
        role_playing_tips = []
        for tip in data["role_playing_tips"]:
            result = db.execute(
                """
                UPDATE role_playing_tips
                SET tip = %s
                WHERE id = %s
                RETURNING id, tip
                """,
                [tip["tip"], tip["id"]],
            )
            rtp_data = result.fetchone()
            if rtp_data:
                rtp_id, rtp_tip = rtp_data
                role_playing_tips.append(RolePlayingTips(id=rtp_id, tip=rtp_tip))
        return role_playing_tips

    def insert_role_playing_tips(self, db, data, npc_id):
        role_playing_tips = []
        for tip in data["role_playing_tips"]:
            result = db.execute(
                """
                INSERT INTO role_playing_tips (tip, character_id)
                VALUES (%s, %s)
                RETURNING id
                """,
                [tip, npc_id],
            )
            rtp_id = result.fetchone()
            rtp__id = rtp_id[0]
            role_playing_tips.append(RolePlayingTips(id=rtp__id, tip=tip))
        return role_playing_tips

    def create_npc_out(self, char_id, data, role_playing_tips):
        return CreateNPCOut(
            id=char_id,
            personality=data["personality"],
            physical_description=data["physical_description"],
            name=data["name"],
            race=data["race"],
            role_playing_tips=role_playing_tips,
        )

    def get_all_npcs(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT * FROM npc;
                    """
                )
                new_list = []
                for npc in result.fetchall():
                    new_list.append(
                        CreateNPCOut(
                            id=npc[0],
                            name=npc[1],
                            race=npc[2],
                            personality=npc[3],
                            physical_description=npc[4],
                            role_playing_tips=self.get_role_playing_tips(
                                db,
                                npc[0],
                            ),
                        )
                    )
                return new_list

    def get_role_playing_tips(self, db, npc_id):
        result = db.execute(
            """
            SELECT id, tip
            FROM role_playing_tips
            WHERE character_id = %s;
            """,
            [npc_id],
        )
        role_playing_tips = []
        for tip in result:
            role_playing_tips.append(
                RolePlayingTips(
                    id=tip[0],
                    tip=tip[1],
                )
            )
        return role_playing_tips

    def get_npc(self, npc_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT * FROM npc
                    WHERE id = %s;
                    """,
                    [npc_id],
                )
                npc = result.fetchone()
                if npc:
                    return CreateNPCOut(
                        id=npc[0],
                        name=npc[1],
                        race=npc[2],
                        personality=npc[3],
                        physical_description=npc[4],
                        role_playing_tips=self.get_role_playing_tips(
                            db,
                            npc[0],
                        ),
                    )
                else:
                    return None

    def delete_npc(self, npc_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM npc
                    WHERE id = %s;
                    """,
                    [
                        npc_id,
                    ],
                )
                if db.rowcount != 1:
                    return None
                return True

    def update_npc(self, data: UpdateNPCData):
        parameters = [
            data.name,
            data.race,
            data.personality,
            data.physical_description,
            data.id,
        ]
        print("parameters", parameters)
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    existing_npc = self.get_npc(data.id)
                    if existing_npc is None:
                        return None
                    db.execute(
                        """
                        UPDATE npc
                        SET name = %s, race = %s, personality = %s, physical_description = %s
                        WHERE id = %s
                        """,
                        parameters,
                    )
                    self.update_role_playing_tips(db, data, data.id)
                    role_playing_tips = self.get_role_playing_tips(db, data.id)
                    return self.create_npc_out(
                        data.id,
                        data.dict(),
                        role_playing_tips=role_playing_tips,
                    )
                except Exception as e:
                    raise e
