class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from Stack is Null")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from stack is Null")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def __repr__(self):
        return f"Stack({self.data})"


def display_menu():
    print("\n--- Stack Menu ---")
    print("A. Push an item to the stack")
    print("D. Pop an item from the stack")
    print("M. Peek the top item")
    print("S. Check the stack size")
    print("Q. Quit the program")
    print("------------------")


def main():
    new_stack = Stack()

    # รับจำนวนตัวเลขที่ต้องการเพิ่มใน Stack
    n = int(input("Enter the number of elements to add to the stack: "))
    
    for i in range(n):
        item = input(f"Enter element {i+1}: ")
        new_stack.push(item)

    print(f"\nStack initialized with {n} elements: {new_stack}")

    while True:
        display_menu()
        choice = input("Enter your choice (A, D, M, S, Q): ").upper()

        if choice == 'A':
            item = input("Enter the item to push: ")
            new_stack.push(item)
            print(f"Item '{item}' pushed to the stack.")
        
        elif choice == 'D':
            try:
                popped_item = new_stack.pop()
                print(f"Item '{popped_item}' popped from the stack.")
            except IndexError:
                print("Error: Stack is empty.")
        
        elif choice == 'M':
            try:
                top_item = new_stack.peek()
                print(f"Top item is: {top_item}")
            except IndexError:
                print("Error: Stack is empty.")
        
        elif choice == 'S':
            print(f"Stack size: {new_stack.size()}")
        
        elif choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter A, D, M, S, or Q.")


if __name__ == "__main__":
    main()
