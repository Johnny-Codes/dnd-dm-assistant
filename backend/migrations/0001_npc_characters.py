steps = [
    [
        """
        CREATE TABLE base_character (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(124) NOT NULL UNIQUE,
            race TEXT NOT NULL,
            npc_level_one_id INT UNIQUE
        );
        CREATE TABLE npc_level_one (
            id SERIAL PRIMARY KEY NOT NULL,
            personality TEXT NULL,
            physical_description TEXT NULL,
            base_character_id INT UNIQUE
        );
        CREATE TABLE role_playing_tips (
            id SERIAL PRIMARY KEY NOT NULL,
            tip TEXT NULL,
            character_id INT REFERENCES npc_level_one(id)
        );
        """,
        """
        DROP TABLE base_character;
        DROP TABLE npc_level_one;
        DROP TABLE role_playing_tips;
        """,
    ]
]
