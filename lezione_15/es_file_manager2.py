import time


class Timer:

    def __init__(self, name):

        self.name = name
    
    def __enter__ (self):

        self.start_time: float = time.perf_counter()

        print("inizio")

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):

        self.end_time: float = time.perf_counter()

        tempo_trascorso: float = self.start_time - self.end_time

        print(f"tempo trascorso: {tempo_trascorso:.3f} secondi")

        if exc_type is not None:

            print(f"exception type: {exc_type}")

            print(f"exception value: {exc_value}")

            print(f"traceback: {traceback}")
        
        return False



with Timer ("test") as t:


    print(t.name)

    for i in range (1000):

        print(i)




    