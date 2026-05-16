# pets
id, UUID PK UNIQUE
name, varchar
age, integer
species (cat/dog), varchar
gender (m/f), varchar
created_at, timestamp

# pet_documents
id, UUID PK UNIQUE
label (filename), varchar
type, varchar
pets_id, integer references pets(id) FK
url, varchar
created_at, timestamp

# Create Tables (AI/StackOverflow/Google)
CREATE TABLE pets (
id          SERIAL PRIMARY KEY,
name        VARCHAR(100)  NOT NULL,
species     VARCHAR(10)   NOT NULL CHECK (species IN ('cat', 'dog')),
gender      VARCHAR(10)   NOT NULL CHECK (gender IN ('male', 'female')),
age         INTEGER       NOT NULL CHECK (age >= 0),
breed       VARCHAR(100),
created_at  TIMESTAMPTZ   DEFAULT NOW()
);

CREATE TABLE pet_documents (
id          SERIAL PRIMARY KEY,
pet_id      INTEGER       NOT NULL REFERENCES pets(id) ON DELETE CASCADE,
label       VARCHAR(200),
url         TEXT          NOT NULL,
created_at  TIMESTAMPTZ   DEFAULT NOW()
);

