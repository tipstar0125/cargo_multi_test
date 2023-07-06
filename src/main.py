from __future__ import annotations

import subprocess
from pathlib import Path

from common.settings import TEST_PATH


def main():

    if TEST_PATH is None:
        return

    path = Path(TEST_PATH)
    score_list = []

    for i in range(10):
        filename = str(i).zfill(4)
        print(f"{filename} start")
        cmd = f"cargo run < in/{filename}.txt > out"
        proc = subprocess.Popen(cmd, shell=True, cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stderr_list = proc.communicate()
        for stderr in stderr_list:
            out_list = stderr.decode().split("\n")
            for out in out_list:
                if "score" in out.lower():
                    score = int(out.split()[1])
                    print(f"{filename} score: {score}")
                    score_list.append(score)

    score_average = sum(score_list) / len(score_list)
    print(score_average)


if __name__ == "__main__":

    main()
