# Basic Data Structures

This homework focuses on applying essential data structures to solve practical problems. You’ll work with queues, deques, and stacks to simulate request processing in a service center, check if a string is a palindrome, and verify the symmetry of bracket sequences. These tasks will enhance your understanding and usage of these fundamental data structures in programming.

## Task Descriptions

### Task 1: Service Center Request Processing

**Objective**: Develop a program that simulates the reception and processing of service requests. The program should automatically generate new requests (identified by a unique number or other data), add them to a queue, and then sequentially remove them from the queue for "processing", thus imitating the operation of a service center.

#### Steps to Implement

1. **Create a request queue**: Initialize a queue to hold incoming service requests.
2. **Generate new requests**: Create a function to generate new requests and add them to the queue.
3. **Process requests**: Create a function to process requests by removing them from the queue and handling them.
4. **Main program loop**: Implement a loop that continuously generates and processes requests until a specified condition is met.

### Task 2: Palindrome Checker

**Objective**: Develop a function that takes a string as an input parameter, adds all its characters to a deque (from the `collections` module in Python), and then compares characters from both ends of the deque to determine if the string is a palindrome. The program should correctly handle strings with both even and odd numbers of characters and be case insensitive and space insensitive.

#### Steps to Implement

1. **Import deque**: Import the deque class from the `collections` module.
2. **Palindrome checker function**: Create a function that:
   - Cleans the input string by removing non-alphanumeric characters and converting it to lowercase.
   - Adds characters of the cleaned string to a deque.
   - Compares characters from both ends of the deque to determine if the string is a palindrome.

## Task 3: Bracket Symmetry Checker

**Objective**: Write a function that checks if the brackets in a given string are symmetric. The function should handle round ( ), square [ ], and curly braces { } brackets. It should determine if the brackets are correctly balanced and properly nested.

#### Steps to Implement

1. **Initialize a stack**: Use a list to keep track of open brackets.
2. **Define bracket pairs**: Create a dictionary to map closing brackets to their corresponding opening brackets.
3. **Iterate through the string**: For each character in the input string:
   - If it's an opening bracket, push it onto the stack.
   - If it's a closing bracket, check if the stack is empty or if the top of the stack doesn't match the corresponding opening bracket.
4. **Final check**: After iterating through the string, check if the stack is empty to determine if the brackets are symmetric.
