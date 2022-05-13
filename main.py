

def dirReduc(arr):
    # convert input to upper case in case any lowers are entered
    arr_upper = []
    for i in arr:
        arr_upper.append(i.upper())
    # create a dict of the opposites of each direction
    opposites_dict = {"NORTH": "SOUTH", "EAST": "WEST", "SOUTH": "NORTH", "WEST": "EAST"}
    print("Evaluating directions: {}\n".format(arr_upper))
    # get the total number of directions in our input
    total_directions = len(arr_upper)
    counter = 0
    while (counter < total_directions-1) and total_directions > 1:
        direction = arr_upper[counter]
        print("Checking value {} for a neighboring opposite.\n".format(direction))
        if arr_upper[counter] == opposites_dict[arr_upper[counter + 1]]:
            neighbor = arr_upper[counter+1]
            print("Found neighbor to the right {}. Deleting {} and {}.\n".format(neighbor, direction, neighbor))
            del arr_upper[counter + 1]
            del arr_upper[counter]
            print("Updated directions: {}\n".format(arr_upper))
            total_directions = len(arr_upper)
            if counter > 0:
                counter = counter - 1
        elif (arr_upper[counter] == opposites_dict[arr_upper[counter - 1]]) and (counter - 1) >= 0:
            neighbor = arr_upper[counter - 1]
            print("Found neighbor to the left {}. Deleting {} and {}.\n".format(neighbor, direction, neighbor))
            del arr_upper[counter]
            del arr_upper[counter - 1]
            print("Updated directions: {}\n".format(arr_upper))
            total_directions = len(arr_upper)
            if counter > 0:
                counter = counter - 1
        else:
            counter = counter + 1
    return arr_upper


if __name__ == '__main__':
    a = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']
    print(dirReduc(a))


