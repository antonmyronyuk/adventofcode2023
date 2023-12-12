with open("input.txt") as input_file:
    lines = input_file.read().strip().split("\n")


class Record:
    def __init__(self, line):
        self.row, self.groups_raw = line.split(" ")
        self.groups = [int(num) for num in self.groups_raw.split(",")]
        self.num_unknown = self.row.count("?")
        self.num_missing_damages = sum(self.groups) - self.row.count("#")
        self.num_missing_op = self.num_unknown - self.num_missing_damages
        self.cache = {}

    def is_valid(self, row):
        return [len(part) for part in row.split(".") if part] == self.groups

    def calc(self, row=None, i=0, num_missing_damages=None, num_missing_op=None, cur_group=-1, left=-1, in_group=False):
        cache_key = (i, num_missing_damages, num_missing_op, cur_group, left, in_group)
        if cache_key in self.cache:
            return self.cache[cache_key]

        if row is None and num_missing_damages is None and num_missing_op is None:
            row = self.row
            num_missing_damages = self.num_missing_damages
            num_missing_op = self.num_missing_op

        if num_missing_damages == 0 and num_missing_op == 0:
            return self.is_valid(row)

        res = 0
        if row[i] == ".":
            if (in_group and left == 0) or not in_group:
                res += self.calc(row, i + 1, num_missing_damages, num_missing_op, cur_group, left, False)
        if row[i] == "#":
            if not in_group and cur_group < len(self.groups) - 1:
                res += self.calc(row, i + 1, num_missing_damages, num_missing_op, cur_group + 1, self.groups[cur_group + 1] - 1, True)
            if in_group and left > 0:
                res += self.calc(row, i + 1, num_missing_damages, num_missing_op, cur_group, left - 1, True)
        if row[i] == "?":
            if num_missing_damages > 0:
                if not in_group and cur_group < len(self.groups) - 1:
                    res += self.calc(row.replace("?", "#", 1), i + 1, num_missing_damages - 1, num_missing_op, cur_group + 1, self.groups[cur_group + 1] - 1, True)
                if in_group and left > 0:
                    res += self.calc(row.replace("?", "#", 1), i + 1, num_missing_damages - 1, num_missing_op, cur_group, left - 1, True)
            if num_missing_op > 0:
                if (in_group and left == 0) or not in_group:
                    res += self.calc(row.replace("?", ".", 1), i + 1, num_missing_damages, num_missing_op - 1, cur_group, left, False)

        self.cache[cache_key] = res
        return res


unfolded_lines = []
for line in lines:
    row, groups = line.split(" ")
    unfolded_row, unfolded_groups = "?".join([row] * 5), ",".join([groups] * 5)
    unfolded_lines.append(f"{unfolded_row} {unfolded_groups}")

print(sum(Record(line).calc() for line in lines))  # part 1
print(sum(Record(line).calc() for line in unfolded_lines))  # part 2
