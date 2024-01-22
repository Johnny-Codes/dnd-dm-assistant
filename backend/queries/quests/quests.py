from queries.pool import pool
from models.quests.quests import (
    QuestOut,
)
from queries.npc_creation import NPCCreationRepo


class QuestsRepo:
    def create_quest(self, data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    quest_db = db.execute(
                        """
                        INSERT INTO quests (name, description)
                        VALUES (%s, %s)
                        RETURNING *
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

    def get_npcs_for_quest(self, db, quest_id):
        try:
            request = db.execute(
                """
                    SELECT npc_id
                    FROM quests_npcs
                    JOIN npc ON npc.id = quests_npcs.npc_id
                    WHERE quests_npcs.quest_id = %s;
                """,
                [
                    quest_id,
                ],
            )
            npc_list = []
            npcs = request.fetchall()
            if npcs:
                for npc in npcs:
                    npc_repo = NPCCreationRepo()
                    x = npc_repo.get_npc(npc_id=npc[0])
                    npc_list.append(x)
            return npc_list
        except Exception as e:
            raise e

    def add_npc_to_quest(self, quest_id, npc_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    quest_npc = db.execute(
                        """
                        INSERT INTO quests_npcs (quest_id, npc_id)
                        VALUES (%s, %s)
                        RETURNING *
                        """,
                        [
                            quest_id,
                            npc_id,
                        ],
                    )
                    quest = quest_npc.fetchone()
                    if quest:
                        return True
                    return False

                except Exception as e:
                    raise e

    def get_all_quests(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    quests = db.execute(
                        """
                            SELECT * FROM quests;
                        """
                    )
                    quest_list = []
                    q = quests.fetchall()
                    for quest in q:
                        get_npcs = self.get_npcs_for_quest(db, quest[0])
                        quest_list.append(
                            QuestOut(
                                id=quest[0],
                                name=quest[1],
                                description=quest[2],
                                npcs=get_npcs,
                            )
                        )
                    return quest_list
                except Exception as e:
                    raise e

    def create_quest_out(self, quest, npc_list):
        pass

    def get_quest(self, quest_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    print("Getting quest with ID:", quest_id)
                    quest = db.execute(
                        """
                        SELECT * FROM quests
                        WHERE id = %s;
                        """,
                        [quest_id],
                    )
                    quest_data = quest.fetchone()
                    if quest_data:
                        get_npcs = self.get_npcs_for_quest(db, quest_id)
                        return QuestOut(
                            id=quest_data[0],
                            name=quest_data[1],
                            description=quest_data[2],
                            npcs=get_npcs,
                        )
                    return None
                except Exception as e:
                    print("Error getting quest:", str(e))
                    raise e

    def delete_quest(self, quest_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    print("Deleting quest with ID:", quest_id)
                    db.execute(
                        """
                        DELETE FROM quests
                        WHERE id = %s;
                        """,
                        [
                            quest_id,
                        ],
                    )
                    conn.commit()
                    if db.rowcount != 1:
                        return None
                    return True
                except Exception as e:
                    print("Error deleting quest:", str(e))
                    # raise e
                    return e

    def update_quest(self, quest_id, updated_quest):
        with pool.connection() as conn:
            with conn.cursor() as db:
                try:
                    update = db.execute(
                        """
                        UPDATE quests
                        SET name = %s, description = %s
                        WHERE id = %s;
                        """,
                        [updated_quest.name, updated_quest.description, quest_id],
                    )
                    conn.commit()
                    update_quest = self.get_quest(quest_id)
                    return update_quest
                except Exception as e:
                    print("Error updating quest:", str(e))
                    raise e
