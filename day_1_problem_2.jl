import Pkg
Pkg.add("RollingFunctions")

using RollingFunctions

depths = readlines(open(ARGS[1]))

sum_depths = rolling(sum, parse.(Int, depths), 3)

println(count([(a[1] < a[2]) for a in zip(sum_depths, sum_depths[2:end])]))