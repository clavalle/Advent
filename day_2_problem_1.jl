dataTupleVector = split.(readlines(open(ARGS[1]))," ")

x = sum([parse(Int,a[2]) for a in dataTupleVector if a[1] == "forward"])
y = sum([parse(Int,a[2]) for a in dataTupleVector if a[1] == "down"]) - sum([parse(Int,a[2]) for a in dataTupleVector if a[1] == "up"])

println(x * y)