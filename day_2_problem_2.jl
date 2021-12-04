dataTupleVector = split.(readlines(open(ARGS[1]))," ")

instructions = [(a[1],parse(Int, a[2])) for a in dataTupleVector]

sub_status = (x = 0, y = 0, aim = 0)

for instruction in instructions
    if instruction[1] == "forward"
        global sub_status = (x = sub_status.x + instruction[2], y = sub_status.y + (sub_status.aim * instruction[2]), aim = sub_status.aim)
    elseif instruction[1] == "down"
        global sub_status = (x = sub_status.x, y = sub_status.y, aim = sub_status.aim + instruction[2])
    elseif instruction[1] == "up"
        global sub_status = (x = sub_status.x, y = sub_status.y, aim = sub_status.aim - instruction[2])
    end
end

println(sub_status.x * sub_status.y)