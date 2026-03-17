from Client0 import Client

if __name__ == "__main__":

    IP = "212.128.255.104"
    PORT = 8080

    print("-----| Practice 3, Exercise 7 |------")
    print(f"Connection to SERVER at {IP}, PORT: {PORT}")

    c = Client(IP, PORT)


    print("* Testing PING...")
    response = c.talk("PING")
    print(response)
    print()


    print("* Testing GET...")
    sequences = []
    for i in range(5):
        response = c.talk(f"GET {i}")
        sequences.append(response)
        print(f"GET {i}: {response}")
    print()


    seq0 = sequences[0]


    print("* Testing INFO...")
    response = c.talk(f"INFO {seq0}")
    print(response)
    print()


    print("* Testing COMP...")
    print(f"COMP {seq0}")
    response = c.talk(f"COMP {seq0}")
    print(response)
    print()


    print("* Testing REV...")
    print(f"REV {seq0}")
    response = c.talk(f"REV {seq0}")
    print(response)
    print()


    print("* Testing GENE...")
    genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

    for gene in genes:
        response = c.talk(f"GENE {gene}")
        print(f"GENE {gene}")
        print(response[:200] + "\n[...]")
        print()
