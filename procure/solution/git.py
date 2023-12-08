import subprocess
from pathlib import Path

from .solution import Solution


class GitSolution(Solution):
    path = ""
    url = ""
    branch = ""
    recursive = False

    def update(self):
        path = Path(self.path)
        if not path.exists():
            self.clone()
        else:
            self.pull()

    def clone(self):
        args = ["git", "clone"]
        if self.recursive:
            args = args + ["--recursive"]
        if self.branch:
            args = args + ["-b", self.branch]
        args = args + [self.url, self.path]
        subprocess.run(args)

    def pull(self):
        path = Path(self.path)
        args = ["git", f"--git-dir={path / '.git'}", f"--work-tree={path}", "pull"]
        if self.recursive:
            args = args + ["--recurse-submodules"]

        subprocess.run(args)
