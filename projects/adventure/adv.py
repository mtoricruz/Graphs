from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# Fill this out with directions to walk
traversal_path = []
visited = {}
# create an empty list to store paths walking back
back_path = []
# reverse direction values to mimic walking back from dead end
walking_back = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
# starting point adds possible exits as values and room #'s as keys
visited[player.current_room.id] = player.current_room.get_exits()

# # while all rooms are not visited:
while len(visited) < len(room_graph):
    # check if current room not in visited dict:
    if player.current_room.id not in visited:
        # add it to visited and set exits
        visited[player.current_room.id] = player.current_room.get_exits()
        # print(visited, 'current exits')
        # store direction just visited in variable
        prev_direction = back_path[-1]
        # remove it from unexplored paths:
        visited[player.current_room.id].remove(prev_direction)
        # print(visited, 'after removing prev direction')
    # if len of paths for current room are 0 (all paths explored):
    if len(visited[player.current_room.id]) == 0:
        # back track to prev directions until room with unexplored
        # paths is found and assign the last added direction of back_path as prev_direction
        prev_direction = back_path[-1]
        # and pop() from list
        back_path.pop()
        # add prev direction to traversal_path
        traversal_path.append(prev_direction)
        # move in that direction
        player.travel(prev_direction)

    # else if unexplored direction
    else:
        # assign variable to first direction in current room 
        direction = visited[player.current_room.id][-1]
        # and pop it from list
        visited[player.current_room.id].pop()
        # add direction to traversal path list
        traversal_path.append(direction)
        # store the walking back path for direction to backpath list
        back_path.append(walking_back[direction])
        # move player in that direction
        player.travel(direction)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
