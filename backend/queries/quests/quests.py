from queries.pool import pool
from models.quests.quests import (
    QuestIn,
    QuestOut,
)


class QuestsRepo:
    def create_quest(self, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    quest_db = db.execute(
                        """
                        INSERT INTO quests (name, description)
                        VALUES (%s, %s)
                        RETURNING *;
                        """,
                        [
                            data.name,
                            data.description,
                        ],
                    )
                    quest = quest_db.fetchone()
                    if quest:
                        id = quest[0]
                        name = quest[1]
                        description = quest[2]
                        return QuestOut(
                            id=id,
                            name=name,
                            description=description,
                        )
                    return False
                except Exception as e:
                    raise e

    def add_npc_to_quest(self, data):
        with pool.connection as conn:
            with conn.cursor as db:
                try:
                    quest_npc = db.execute(
                        """
                        INSERT INTO quests_npcs (quest_id, npc_id)
                        VALUES (%s, %s);
                        """,
                        [
                            data.quest_id,
                            data.npc_id,
                        ],
                    )
                    quest = quest_npc.fetchone()
                    if quest:
                        return True

                except Exception as e:
                    raise e
