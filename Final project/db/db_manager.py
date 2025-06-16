# [3, 10] 任务状态和数据库管理
import sqlite3

class DBManager:
    def __init__(self, db_path="vocab.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS wordbook (
            user TEXT, word TEXT, meaning TEXT, PRIMARY KEY(user, word)
        )
        """)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS task_state (
            task_id TEXT PRIMARY KEY, state TEXT
        )
        """)
        self.conn.commit()

    def add_word(self, user, word, meaning):
        self.conn.execute("REPLACE INTO wordbook VALUES (?, ?, ?)", (user, word, meaning))
        self.conn.commit()

    def get_words(self, user):
        cur = self.conn.execute("SELECT word, meaning FROM wordbook WHERE user=?", (user,))
        return cur.fetchall()

    def save_state(self, task_id, state):
        self.conn.execute("REPLACE INTO task_state VALUES (?, ?)", (task_id, state))
        self.conn.commit()

    def load_state(self, task_id):
        cur = self.conn.execute("SELECT state FROM task_state WHERE task_id=?", (task_id,))
        row = cur.fetchone()
        return row[0] if row else None

if __name__ == "__main__":
    db = DBManager()
    db.add_word("alice", "apple", "苹果")
    print(db.get_words("alice"))
    db.save_state("task1", "doing apple")
    print(db.load_state("task1"))