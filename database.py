import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            database = "webscrapyy",
            user = "postgres",
            password = "06Suru13$",
            host = "localhost",
            port = "5432"
        )

        print("Database Connection Successfull.")
        
        return conn

    except Exception as e:
        print("Database connection error:", e)
        return None
    
conn = get_connection()
if conn:
    conn.close()