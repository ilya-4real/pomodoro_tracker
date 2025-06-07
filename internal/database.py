from dataclasses import dataclass, field
from pathlib import Path
import sqlite3
import os


class AppConfig:
    def __init__(self) -> None:
        self.tasks_table = os.environ.get("POMODORO_TASK_TABLE", "tasks")
        file_path = os.environ.get("POMODORO_DB_FILE")
        if file_path is None:
            base_dir = Path.home() / ".local/share/pomodoro"
            base_dir.mkdir(parents=True, exist_ok=True)
            file_path = base_dir / "pomodoro.sqlite"
            file_path.touch()
            self.file_path = file_path.as_posix()
        else:
            self.file_path = file_path


@dataclass
class Task:
    task_title: str
    start_time: int
    end_time: int
    is_completed: bool = field(default=False)


class SqliteTaskDatabase:
    def __init__(self, config: AppConfig) -> None:
        self.config = config

    def insert_task(self, task: Task):
        insert_stmt = f"""
        INSERT INTO {self.config.tasks_table}
        VALUES
        (?, ?, ?, ?);
        """

        with sqlite3.connect(self.config.file_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                insert_stmt,
                [task.start_time, task.end_time, task.task_title, task.is_completed],
            )
        print(f"task inserted, {self.config.file_path}, {self.config.tasks_table}")

    @staticmethod
    def init_database(config: AppConfig):
        tasks_table_ddl = f"""
        CREATE TABLE IF NOT EXISTS {config.tasks_table}
        (
            start_timestamp INT,
            end_timestamp INT,
            task_title TEXT,
            completed BOOL
        );
        """
        with sqlite3.connect(config.file_path) as conn:
            cursor = conn.cursor()
            cursor.execute(tasks_table_ddl)
