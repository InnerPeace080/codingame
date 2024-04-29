import math
import sys

# Save humans, destroy zombies!

humans: dict[int, list[int]] = {}
zombies: dict[int, list[int]] = {}


# game loop
while True:
    # clear humans and zombies
    humans.clear()
    zombies.clear()

    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans[human_id] = [human_x, human_y]
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies[zombie_id] = [zombie_x, zombie_y, zombie_xnext, zombie_ynext]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # calculate distance between human and zombie
    danger_human_id = 0
    threat_zombie_id = 0
    shortest_distance = None
    for human_id in humans:
        human_x, human_y = humans[human_id]
        can_save = False
        shortest_distance_local = None
        for zombie_id in zombies:
            zombie_x, zombie_y, zombie_xnext, zombie_ynext = zombies[zombie_id]
            distance = math.sqrt((zombie_x - human_x) ** 2 + (zombie_y - human_y) ** 2)
            print(f"Distance between human {human_id} and zombie {zombie_id}: {distance}", file=sys.stderr, flush=True)

            if shortest_distance_local is None or distance < shortest_distance_local:
                shortest_distance_local = distance

        if shortest_distance_local is not None:
            time_to_die = shortest_distance_local / 400
            distance_to_save = math.sqrt((human_x - x) ** 2 + (human_y - y) ** 2) - 1500
            time_to_save = distance_to_save / 1000
            if time_to_save < time_to_die:
                can_save = True

        for zombie_id in zombies:
            zombie_x, zombie_y, zombie_xnext, zombie_ynext = zombies[zombie_id]
            distance = math.sqrt((zombie_x - human_x) ** 2 + (zombie_y - human_y) ** 2)

            if can_save and (shortest_distance is None or distance < shortest_distance):
                shortest_distance = distance
                danger_human_id = human_id
                threat_zombie_id = zombie_id

    # # go straight to threat_zombie_id
    # print(f"Threat zombie id: {threat_zombie_id}", file=sys.stderr, flush=True)

    # # Your destination coordinates
    # print(f"{zombies[threat_zombie_id][0]} {zombies[threat_zombie_id][1]}")

    print(f"{humans[danger_human_id][0]} {humans[danger_human_id][1]}")
