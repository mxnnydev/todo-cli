import os 

def create():
    db_option = input("🗃️  Do you want to create a new database? (Yes/y or No/n): ").strip().lower()
    if db_option in ['yes', 'y']:
        name_db = input("📝 Enter a name for your new database: ").strip()
        # if DB Does not exist create DB
        if not os.path.exists(name_db):
            os.mkdir(name_db)
        else:
            while os.path.exists(name_db):
                print("DB name is taken")
                name_db = input("📝 Enter a name for your new database: ").strip()
            os.mkdir(name_db)
    elif db_option in ['no', 'n']:
        access_db = input("Which DB: ").strip()
        if os.path.exists(access_db):
            print("✅ Database detected. Select an operation to proceed:")
        # Full path to the DB
        file_path = os.path.join(access_db, 'tasks.txt')

        task = "What is the next task?"

        # Create the file and write text
        with open(file_path, "w") as file:
            file.write(task)        
create()
    

    

def delete():
    print("delete Logic")

def edit():
    print("edit Logic")

def view():
    print("view Logic")