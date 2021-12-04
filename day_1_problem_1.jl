depths = readlines(open(ARGS[1]))

println(count([(a[1] < a[2]) for a in zip(parse.(Int, depths), parse.(Int, depths[2:end]))]))