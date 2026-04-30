import sqlite3
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class User:
    id: int
    name: str
    email: str
    created_at: str

class UserRepository:
    def __init__(self, db_path: str = 'users.db'):
        self.db_path = db_path

    def find_by_id(self, user_id: int) -> Optional[User]:
        conn = sqlite3.connect(self.db_path)
        query = "SELECT * FROM users WHERE id = ?"
        row = conn.execute(query, (user_id,)).fetchone()
        conn.close()
        if row:
            return User(id=row[0], name=row[1], email=row[2], created_at=row[3])
        return None

    def find_by_name(self, name: str) -> List[User]:
        conn = sqlite3.connect(self.db_path)
        query = "SELECT * FROM users WHERE name = ?"
        rows = conn.execute(query, (name,)).fetchall()
        conn.close()
        return [User(id=r[0], name=r[1], email=r[2], created_at=r[3]) for r in rows]

    def list_all(self) -> List[User]:
        conn = sqlite3.connect(self.db_path)
        rows = conn.execute("SELECT * FROM users").fetchall()
        conn.close()
        return [User(id=r[0], name=r[1], email=r[2], created_at=r[3]) for r in rows]
