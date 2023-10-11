steps = [
    [
        """
        CREATE TYPE alignment_types AS ENUM (
            'Lawful Good', 'Lawful Neutral', 'Lawful Evil', 
            'Neutral Good', 'True Neutral', 'Neutral Evil',
            'Chaotic Good', 'Chaotic Neutral', 'Chaotic Evil';
        )

        CREATE TABLE character_stats (
            id SERIAL PRIMARY KEY NOT NULL,
            strength INTEGER NULL,
            dexterity INTEGER NULL,
            constitution INTEGER NULL,
            intelligence INTEGER NULL,
            wisdom INTEGER NULL,
            charisma INTEGER NULL,
        )

        CREATE TABLE base_character (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(124) NOT NULL UNIQUE,
            backstory TEXT NULL,
            alignment alignment_types NULL,
            abilities TEXT NULL,
        )

        CREATE TABLE npc_characters (
            id SERIAL PRIMARY KEY NOT NULL,
            personality TEXT NULL,
            appearance TEXT NULL,
            role TEXT NULL,
            goals TEXT NULL,
            relationships TEXT NULL,
            character_arc TEXT NULL,
            secrets TEXT NULL,
            notes TEXT NULL,
            stats INTEGER REFERENCES character_stats(id) UNIQUE,
        );

        CREATE TABLE player_characters (
            id SERIAL PRIMARY KEY NOT NULL,
            backgrounds 
        )
        """,
        """
        DROP TABLE npc_characters;
        DROP TABLE character_stats;
        """,
    ]
]
