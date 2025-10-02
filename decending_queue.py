from collections import deque

def sort_queue(input_queue):
    
    temp_list = []
    while input_queue:
        temp_list.append(input_queue.popleft())

    temp_list.sort()

    sorted_queue = deque(temp_list)
    
    return sorted_queue

if __name__ == "__main__":
    my_queue = deque()
    my_queue.append(5)
    my_queue.append(2)
    my_queue.append(8)
    my_queue.append(1)
    my_queue.append(4)

    print(f"Original queue: {list(my_queue)}")

    sorted_q = sort_queue(my_queue)

    print(f"Sorted queue:   {list(sorted_q)}")

    string_queue = deque()
    string_queue.append("Cherry")
    string_queue.append("Apple")
    string_queue.append("Elderberry")
    string_queue.append("Banana")
    
    print(f"\nOriginal string queue: {list(string_queue)}")
    sorted_string_q = sort_queue(string_queue)
    print(f"Sorted string queue:   {list(sorted_string_q)}")