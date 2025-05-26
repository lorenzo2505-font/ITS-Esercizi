'''PATH: str = "lezione_15/example.txt"

mode: str = "r+"

encoding: str = "utf-8"

file = open(PATH, mode = mode, encoding = encoding)

print(file)

output: str = file.write("my name is gustavo but you can call me gus")

output: str = file.read()

 

print(output)

file.close()'''


with open("lezione_15/example25.txt", mode = "w" , encoding = "utf-8" ) as file:
    
    message: str = "hello people \n"

    written_char: int = file.write(message)

    print(f"written characters: {written_char}")


import time

class StopWatch:

    def __init__(self):

        self.start_time = None

        self.end_time = None

    
    def __enter__ (self):

        self.start_time = time.time()

        return self
    
    def __exit__ (self, exc_tipe, exc_value, traceback):

        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time

        print(f"{elapsed_time:.8f} seconds")

        if exc_tipe is not None:

            print(exc_tipe)

            print(exc_value)

            print(traceback)

        
        return False


pass



with StopWatch():

    print("inizio")

    time.sleep(2)

    print("fine")

        

        



    