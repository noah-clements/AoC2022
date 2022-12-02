from itertools import groupby

with open('input.txt') as f:
    foods = f.read().split('\n')

elf_calories = [list(food) for i, food in groupby(foods, lambda x: x=='') if not i]
elf_calories = [[int(i) for i in inner_list] for inner_list in elf_calories]
# print(elf_calories)
elf_sums = [(i, sum(inner_list)) for i, inner_list in enumerate(elf_calories)]
print(elf_sums)

sorted_elves = sorted(elf_sums, key=lambda elf: elf[1], reverse=True)
print(sorted_elves[:3])
print(sum(elf for _, elf in sorted_elves[:3]))


