from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# Server configuration
IP = "212.128.255.37"
PORT = 8081

# Create client
c = Client(IP, PORT)

print(c)

# Send message
print("Sending a message to the server...")
response = c.talk("Testing!!!")

print(f"Response: {response}")