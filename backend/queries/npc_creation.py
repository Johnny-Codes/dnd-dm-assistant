from .pool import pool
from models.npc_creation import CreateNPCOut, RolePlayingTips


class NPCCreationRepo:
    def create(self, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                base_character = db.execute(
                    """
                        INSERT INTO base_character (name, race)
                        VALUES (%s, %s)
                        RETURNING id
                    """,
                    [data["name"], data["race"]],
                )
                char = base_character.fetchone()
                char_id = char[0]
                npc_level_one_char = db.execute(
                    """
                        INSERT INTO npc_level_one (personality,
                            physical_description, base_character_id)
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
                npc_id = npc[0]
                db.execute(
                    """
                        UPDATE base_character
                        SET npc_level_one_id = %s
                        WHERE id = %s
                    """,
                    [
                        npc_id,
                        char_id,
                    ],
                )
                role_playing_tips = []
                for tip in data["role_playing_tips"]:
                    result = db.execute(
                        """
                            INSERT INTO role_playing_tips (tip, character_id)
                            VALUES (%s, %s)
                            RETURNING id
                        """,
                        [
                            tip,
                            npc_id,
                        ],
                    )
                    rtp_id = result.fetchone()
                    rtp__id = rtp_id[0]
                    role_playing_tips.append(
                        RolePlayingTips(
                            id=rtp__id,
                            tip=tip,
                        )
                    )

                npc_out = CreateNPCOut(
                    id=char_id,
                    personality=data["personality"],
                    physical_description=data["physical_description"],
                    name=data["name"],
                    race=data["race"],
                    role_playing_tips=role_playing_tips,
                )
                return npc_out
