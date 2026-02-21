import requests
from bs4 import BeautifulSoup
import lxml

def scrapy_courses():
    scrap_website = 'https://broadwayinfosys.com/courses'
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'}

    try:
        response = requests.get(scrap_website, headers= header)

        if response.status_code == 200:
            print("Connected to the website")
            html_content =response.text

            # creating soup
            soup = BeautifulSoup(html_content, 'lxml')
        
            # print(soup.prettify())

            #main containers
            course_divs = soup.find_all('div', class_ = "course-card")

            courses = []
            for course in course_divs:
                #Course Name
                title_tag = course.find('a', class_ = "course-card__title")
                course_name = title_tag.get_text(strip=True) if title_tag else "N/A"

                # Duration
                duration_div = course.find('div', class_ = "course-duration")
                #duration = list(duration_div.stripped_strings)[-1] if duration_div else "N/A"
                duration = duration_div.get_text(strip=True) if duration_div else "N/A"

                #gettting link
                link_tag = course.find('a', href=True)
                link = link_tag['href'] if link_tag else "N/A"
            
                courses.append((course_name, duration, link))

            return courses    
        else:
            print(f"Connected Failed!{response.status_code}")

    except Exception as e:
        print("Scraping error:", e)
        return[]
