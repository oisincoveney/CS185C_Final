import os


class ChallengeIterator:
    def __init__(self):
        with open(os.path.join("data", "Challenge_stats.txt")) as stats_file:
            self.files = [line.split(",")[0] for line in stats_file.readlines()]
            self.files_iter = iter(self.files)

    def __iter__(self):
        return self

    def __next__(self):
        filename = next(self.files_iter)
        return str(round(os.path.getmtime(os.path.join("data", "Challenge", filename)) * 1000) // 10)


for x in ChallengeIterator():
    print(x)
