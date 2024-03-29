steps = [
    [
        """
            CREATE TABLE quests (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(124) NOT NULL UNIQUE,
                description TEXT NULL
            );
            CREATE TABLE quests_npcs(
                quest_id INTEGER REFERENCES quests(id) ON DELETE CASCADE,
                npc_id INTEGER REFERENCES npc(id) ON DELETE CASCADE,
                CONSTRAINT quests_npcs_pk PRIMARY KEY(quest_id, npc_id)
            );
        """,
        """
            DROP TABLE quests;
            DROP TABLE quests_npcs;
        """,
    ]
]
