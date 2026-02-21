from web import scrapy_courses
from export import export_csv, export_json
from database import get_connection

def save_to_db(data):
    conn = get_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        for c in data:
            cur.execute(
                "INSERT INTO courses(course_name, duration, course_link) VALUES (%s,%s,%s)",
                c
            )
        conn.commit()
        conn.close()
        print("Data saved to PostgreSQL")
    except Exception as e:
        print("Insert error:", e)

def main():
    print("\nBroadway Infosys Course Scraper")
    print("1. Save to PostgreSQL")
    print("2. Export to CSV")
    print("3. Export to JSON")

    choice = input("Choose option: ")

    data = scrapy_courses()

    if not data:
        print("No data scraped")
        return

    if choice == "1":
        save_to_db(data)
    elif choice == "2":
        export_csv(data)
    elif choice == "3":
        export_json(data)
    else:
        print("Invalid choice")

main()