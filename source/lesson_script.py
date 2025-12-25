import subprocess
from pathlib import Path
from typing import Iterable


class LessonScript:
    def __init__(
            self,
            no: int,
            name: str,
            source_file: str,
            compile_dir: str,
        ) -> None:
        self.no = no
        self.name = name
        self.source_file = Path(source_file)
        self.compile_dir = Path(compile_dir)

        self.compile_dir.mkdir(parents=True, exist_ok=True)
        self.compile_file = self.compile_dir / self.source_file.stem


    def compile(self) -> None:
        subprocess.run(
            ["g++", str(self.source_file), "-o", str(self.compile_file)],
            check=True,
            capture_output=True,
            text=True,
        )


    def run(self, *args: str) -> str:
        result = subprocess.run(
            [str(self.compile_file), *args],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()


    def __str__(self) -> str:
        return f"{self.no}. {self.name}"
