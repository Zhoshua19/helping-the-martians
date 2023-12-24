import random


box_locations = [random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)]


box_weights = [random.randint(1, 713) for _ in range(3)]
while sum(box_weights) != 713:
    box_weights = [random.randint(1, 713) for _ in range(3)]

def move_boxes():
    global box_locations
    box_locations = [random.randint(1, 7) for _ in range(3)]

def find_boxes(user_input):
    found_weights = [box_weights[i] for i, location in enumerate(box_locations) if location == user_input]
    return sum(found_weights)

def main():
    while True:
        total_found_weight = 0
        for _ in range(3):
            user_input = int(input("Enter a kilometer mark (1-7): "))
            found_weight = find_boxes(user_input)
            total_found_weight += found_weight

            if found_weight == 0:
                move_boxes()
                break

        if total_found_weight == 713:
            print("Congratulations! All boxes found.")
            break
        else:
            print("Not all boxes found. Try again.")

if __name__ == "__main__":
    main()
