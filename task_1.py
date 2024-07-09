import queue
import random
import time

# Create a queue to hold the applications
application_queue = queue.Queue()

# Function to generate a new request
def generate_request():
    # Generate a new request with a unique ID
    request_id = random.randint(1, 1000)
    print(f"Created application: {request_id}")
    # Add the request to the queue
    application_queue.put(request_id)

# Function to process a request
def process_request():
    # If the queue is not empty
    if not application_queue.empty():
        # Remove the request from the queue
        request_id = application_queue.get()
        # Process the request
        print(f"Processing application: {request_id}")
    else:
        # Print a message if the queue is empty
        print("Queue is empty")

# Main program loop
try:
    while True:
        # Call generate_request() to create new applications
        generate_request()
        # Call process_request() to process applications
        process_request()
        # Simulate a delay between operations
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting the program.")  # Press Ctrl + C to exit