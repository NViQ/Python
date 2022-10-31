def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH", '').replace("SOUTH NORTH", '').replace("EAST WEST", '').replace("WEST EAST", '')
    dir3 = dir2.split()
    print(dirReduc(dir3) if len(dir3) < len(arr) else dir3)

# opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
#
# def dirReduc(plan):
#     new_plan = []
#     for d in plan:
#         if new_plan and new_plan[-1] == opposite[d]:
#             new_plan.pop()
#         else:
#             new_plan.append(d)
#     return new_plan


# u=["NORTH", "WEST", "SOUTH", "EAST"]
# dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"]

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
dirReduc(a)#, ['WEST'])
