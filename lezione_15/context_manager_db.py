class DataBaseConnection:

    def __init__(self, db_name):
        
        self.db_name = db_name

        self.connection = None
    
    def conncect (self):

        print(f"Connecting to database: {self.db_name} ")

        #simulate a database connection

        self.connection = f"Connection to {self.db_name}"

    
    def disconnect(self):

        print(f"Disconnetting to database: {self.db_name}")

        self.connection = None
    
    
    def commit (self):

        print("commit transaction")

    
    def rollback (self):

        print("rolling back transaction")

    
    def execute_query(self, query):

        print(f"executing query: {query}")

        #simulate a query connection

        return f"results of ' {query}"



class DataBaseContextManager:


    def __init__(self, db_name):

        self.db = DataBaseConnection (db_name)

    
    def __enter__(self):

        self.db.conncect()

        return self.db
    
    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is not None:

            #if an exception occured go back to the transiction

            self.db.rollback()


            print(f"Exeption type: {exc_type}")

            print(f"Exception value: {exc_value}")

            print(f"Traceback: {traceback}")


        else:

            #commit the transiction if no exception accoured

            self.db.commit()


        #always disconnect from the database 


        self.db.disconnect()

        #return False to propagate the exception, True to suppres

        return False












