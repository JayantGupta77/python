import random
import time

def red_light_green_light():
    position = 0
    finish = 10
    print("Reach the finish line at position", finish)
    print("Commands: 'go' to move forward (only during Green Light)")

    while position < finish:
        light = random.choice(['Green', 'Red'])
        print(f"\n{light} Light!")
        if light == 'Green':
            start_time = time.time()
            user_input = input("Type 'go' to move forward: ").strip().lower()
            elapsed = time.time() - start_time
            if user_input == 'go':
                position += 1
                print(f"You moved to position {position}")
            else:
                print("You didn't move.")
        else:
            # Red Light - if player tries to move, they lose
            start_time = time.time()
            user_input = input("Wait! (Press Enter if you don't move): ").strip().lower()
            elapsed = time.time() - start_time
            if user_input:
                print("You moved during Red Light. Game Over!")
                return
            else:
                print("Good job! You waited.")

        time.sleep(1)
    
    print("Congratulations! You won Red Light, Green Light.")

if __name__ == '__main__':
    red_light_green_light()
