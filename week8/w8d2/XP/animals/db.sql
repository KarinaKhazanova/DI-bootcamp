CREATE TABLE
    families (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(50) NOT NULL
    );

CREATE TABLE
    animals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(50),
        weight REAL,
        height REAL,
        speed INTEGER,
        family INTEGER,
        FOREIGN KEY (family) REFERENCES families (id)
    )