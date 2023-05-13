from csv import reader as rd, writer as wr
from os import path
from typing import Literal
# import bcrypt


def validatePath() -> bool:
    """
    validatePath is the first step for database GET process
    :return: Boolean indicating validation success
    """
    # Path check
    if path.exists(f"files/database/"):
        return True
    else:
        return False


def validateFile(table: Literal["users", "accounts", "hashes"]) -> bool:
    """
    validateFile is the second step for database GET process
    :param table: String modifier for database table
    :return: Boolean indicating validation success
    """
    # Reference variable
    database = f"files/database/{table}.csv"

    # Path check
    if path.isfile(database):
        return True
    else:
        return False


# CREATE
def createDb() -> bool:
    """
    createPath is for database table creation
    :return: Boolean indicating creation success
    """
    # Reference variables
    files = ["users", "accounts", "hashes"]

    for file in files:
        database = f"files/database/{file}.csv"
        # Write file and table header
        with open(database, "w", newline="") as f:
            writer = wr(f)
            if file == "users":
                writer.writerow(["PK", "ID", "FIRST", "LAST", "EMAIL", "HASH"])
            elif file == "accounts":
                writer.writerow(["ID", "EMAIL", "SCORE", "FK"])
            elif file == "hashes":
                writer.writerow(["ID", "HASH", "PASSWORD", "FK"])

    return True


# CREATE

# Create user record
def createUser(first: str, last: str, email: str, hashy: int) -> None:
    """
    createUser creates user record for users table
    :param first: String containing first name of user
    :param last: String containing last name of user
    :param email: String containing email of user
    :param hashy: String containing hashed password value
    :return: None
    """
    # Reference variables
    database = f"files/database/users.csv"
    pk: str | int = ""
    ident: str | int = ""

    with open(database, "r", newline="") as f:
        reader = rd(f)
        for row in reader:
            pk = row[0]
            ident = row[1]
            if row[4] == email:
                raise ValueError("This user already exists!")

    if pk == "PK":
        pk = 0
    else:
        pk = int(pk) + 1

    if ident == "ID":
        ident = 0
    else:
        ident = int(ident) + 1

    record = [pk, ident, first, last, email, hashy]

    with open(database, "a", newline="") as f:
        writer = wr(f)
        writer.writerow(record)


# Create account record
def createAccount(email: str, fk: int, score: int = 0) -> None:
    """
    createAccount creates account record for accounts table
    :param email: Email string of user
    :param score: Score, default = 0
    :param fk: Primary Key from users table
    :return: None
    """
    # Reference variables
    database = f"files/database/accounts.csv"
    ident: str | int = ""

    with open(database, "r", newline="") as f:
        reader = rd(f)
        for row in reader:
            ident = row[0]
            if row[1] == email:
                raise ValueError("This account already exists!")

    if ident == "ID":
        ident = 0
    else:
        ident = int(ident) + 1

    record = [ident, email, score, fk]

    with open(database, "a", newline="") as f:
        writer = wr(f)
        writer.writerow(record)


# Create hash record
def createSecret(hashy: int, password: str, fk: int) -> None:
    """
    createSecret creates hash record for hashes table
    :param hashy: Salty hash
    :param password: User's password
    :param fk: Primary Key from users table
    :return: None
    """
    # Reference variables
    database = f"files/database/hashes.csv"
    ident: str | int = ""

    with open(database, "r", newline="") as f:
        reader = rd(f)
        for row in reader:
            ident = row[0]
            if row[-1] == fk:
                raise ValueError("This record already exists!")

    if ident == "ID":
        ident = 0
    else:
        ident = int(ident) + 1

    record = [ident, hashy, password, fk]

    with open(database, "a", newline="") as f:
        writer = wr(f)
        writer.writerow(record)


def main():
    # valid_path = validatePath()
    # valid_file: bool
    #
    # print(valid_path)
    #
    # if valid_path:
    #     valid_file = validateFile("users")
    #     print(valid_file)
    #     if valid_file:
    #         print(createUser("en", "der", "com", 123))
    #
    # if not valid_file:
    #     createDb()
    #     print(createUser("en", "der", "com", 123))

    for num in range(0, 100):
        createUser("en", "der", "com", 123)


# READ

# Read users table
def authUser(email: str, pw: str) -> True:
    """
    AuthUser reads records from the users table
    :param email: User's email
    :param pw: User's pw hash
    :return: User's primary key
    """
    # Reference variables
    database = f"files/database/users.csv"
    user: str | None = None

    with open(database, "r", newline="") as f:
        reader = rd(f)
        for row in reader:
            if row[4] == email and row[5] == pw:
                user = row[0]
                break

    # TODO: Hash user pk

    # return hashed user
    return True


if __name__ == "__main__":
    main()
