import random


def initialize_boxes():
    box_locations = [random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)]
    box_weights = [random.randint(1, 713) for _ in range(3)]
    while sum(box_weights) != 713:
        box_weights = [random.randint(1, 713) for _ in range(3)]
    return box_locations, box_weights


def move_boxes():
    return [random.randint(1, 7) for _ in range(3)]


def main():
    box_locations, box_weights = initialize_boxes()
    attempts = 0

    while True:
        attempts += 1
        guessed_locations = [int(input(f"Enter guess {i+1} (1-7): ")) for i in range(3)]
        found_weights = [box_weights[i] for i, loc in enumerate(box_locations) if loc in guessed_locations]
        
        if sum(found_weights) == 713:
            print(f"Congratulations! All boxes found in {attempts} attempts.")
            break
        else:
            print("Not all boxes found. Boxes are moving...")
            box_locations = move_boxes()

if __name__ == "__main__":
    main()
