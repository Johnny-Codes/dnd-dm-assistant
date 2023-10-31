steps = [
    [
        """
        CREATE TABLE npc (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(124) NOT NULL UNIQUE,
            race TEXT NOT NULL,
            personality TEXT NULL,
            physical_description TEXT NULL
        );
        CREATE TABLE role_playing_tips (
            id SERIAL PRIMARY KEY NOT NULL,
            tip TEXT NULL,
            character_id INT REFERENCES npc(id) ON DELETE CASCADE
        );
        """,
        """
        DROP TABLE npc;
        DROP TABLE role_playing_tips;
        """,
    ]
]
