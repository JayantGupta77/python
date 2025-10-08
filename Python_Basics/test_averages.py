def calculate_test_average(): 
    scores = []
    
    while True:
        try:
            num_tests = int(input("Enter the number of tests you want to average: "))
            if num_tests <= 0:
                print("Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    
    print("\nPlease enter the scores for each test (e.g., 95.5):")
    for i in range(num_tests):
        while True:
            try:
                score = float(input(f"Enter score for Test #{i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number for the score.")

    if scores:  
        total_score = sum(scores)
        average = total_score / len(scores)
        
        print("\n" + "="*30)
        print(f"Total number of tests: {len(scores)}")
        print(f"Total score sum: {total_score:.2f}")
        print(f"**Test Average: {average:.2f}**")
        print("="*30)
    else:
        print("\nNo scores were entered. Cannot calculate an average.")

if __name__ == "__main__":
    calculate_test_average()