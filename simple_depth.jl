using DelimitedFiles

depths = readlm("depth.txt")

depth_increase_count = 0

prev_depth = nothing

for d in depths
    if prev_depth === nothing
        prev_depth = d
        continue
    if d > prev_depth
        depth_increase_count = depth_increase_count + 1

print(depth_increase_count)

