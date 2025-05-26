class MyResource:

    def __enter__(self):

        #code to acquire resource or setup

        print("resource acquired")

        #return the resource itself (optional)

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):

        #code to release resource or cleanup:

        print("resource released")

        #it handle exception (optional)

        if exc_type is not None:

            print(f"exception type: {exc_type}")

            print(f"exception value: {exc_value}")

            print(f"traceback: {traceback}")
        
        #return false to provocate the exception

        return False
    

#using the custom context manager using the with statement


with MyResource() as resource:

    print("inside with block")


    #simulate some operation that might cause an exception

    #uncomment the following line to test exception handiling

    #raise ValueError