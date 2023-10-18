from .pool import pool
from models.npc_creation import CreateNPCOut, RolePlayingTips


class NPCCreationRepo:
    def create(self, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    conn.begin()

                    char_id = self.insert_base_character(db, data)
                    npc_id = self.insert_npc_level_one(db, data, char_id)
                    self.update_base_character_npc_id(db, char_id, npc_id)
                    role_playing_tips = self.insert_role_playing_tips(
                        db,
                        data,
                        npc_id,
                    )

                    conn.commit()

                    npc_out = self.create_npc_out(
                        char_id,
                        data,
                        role_playing_tips,
                    )
                    return npc_out

                except Exception as e:
                    conn.rollback()
                    raise e

    def insert_base_character(self, db, data):
        base_character = db.execute(
            """
            INSERT INTO base_character (name, race)
            VALUES (%s, %s)
            RETURNING id
            """,
            [data["name"], data["race"]],
        )
        char = base_character.fetchone()
        return char[0]

    def insert_npc_level_one(self, db, data, char_id):
        npc_level_one_char = db.execute(
            """
            INSERT INTO npc_level_one (personality, physical_description, base_character_id)
            VALUES (%s, %s, %s)
            RETURNING id
            """,
            [
                data["personality"],
                data["physical_description"],
                char_id,
            ],
        )
        npc = npc_level_one_char.fetchone()
        return npc[0]

    def update_base_character_npc_id(self, db, char_id, npc_id):
        db.execute(
            """
            UPDATE base_character
            SET npc_level_one_id = %s
            WHERE id = %s
            """,
            [npc_id, char_id],
        )

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
