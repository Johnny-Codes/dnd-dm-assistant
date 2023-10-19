from .pool import pool
from models.npc_creation import CreateNPCOut, RolePlayingTips


class NPCCreationRepo:
    def create(self, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    npc_id = self.insert_npc_level_one(db, data)

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

    def insert_npc_level_one(self, db, data):
        npc_level_one_char = db.execute(
            """
            INSERT INTO npc_level_one (name, race, personality, physical_description)
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
        npc = npc_level_one_char.fetchone()
        return npc[0]

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

    def get_all_npc_level_one_chars(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT * FROM npc_level_one;
                    """
                )
                new_list = []
                for npc in result.fetchall():
                    print("npc", npc)
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

    def get_role_playing_tips(self, db, character_id):
        result = db.execute(
            """
            SELECT id, tip
            FROM role_playing_tips
            WHERE character_id = %s;
            """,
            [character_id],
        )
        role_playing_tips = []
        for tip in result:
            role_playing_tips.append(RolePlayingTips(id=tip[0], tip=tip[1]))
        return role_playing_tips

    def get_npc_level_one(self, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    SELECT * FROM npc_level_one
                    WHERE id = %s;
                    """,
                    [data],
                )
                npc = result.fetchone()
                if npc:
                    return CreateNPCOut(
                        id=npc[0],
                        name=npc[1],
                        race=npc[2],
                        personality=npc[3],
                        physical_description=npc[4],
                        role_playing_tips=self.get_role_playing_tips(db, npc[0]),
                    )
                else:
                    return None
