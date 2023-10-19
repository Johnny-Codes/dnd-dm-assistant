steps = [
    [
        """
        CREATE TABLE npc_level_one (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(124) NOT NULL UNIQUE,
            race TEXT NOT NULL,
            personality TEXT NULL,
            physical_description TEXT NULL,
            base_character_id INT UNIQUE
        );
        CREATE TABLE role_playing_tips (
            id SERIAL PRIMARY KEY NOT NULL,
            tip TEXT NULL,
            character_id INT REFERENCES npc_level_one(id) ON DELETE CASCADE
        );
        """,
        """
        DROP TABLE npc_level_one;
        DROP TABLE role_playing_tips;
        """,
    ]
]
