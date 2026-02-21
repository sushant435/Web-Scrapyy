import csv
import json

def export_csv(data):
    try:
        with open("courses.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Course Name", "Duration", "Link"])
            writer.writerows(data)
        print("Saved to courses.csv")
    except Exception as e:
        print("CSV Error:", e)

def export_json(data):
    try:
        json_data = []
        for c in data:
            json_data.append({
                "course_name": c[0],
                "duration": c[1],
                "link": c[2]
            })

        with open("courses.json", "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4)

        print("Saved to courses.json")
    except Exception as e:
        print("JSON Error:", e)