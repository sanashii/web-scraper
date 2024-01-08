from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file: # 'html_file' is a variable name that we use to read the file contents and do operations with it
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml') # note: lxml is a parsers
    # print(soup.prettify())
    # tags = soup.find('h5') # .find() finds the 1st instance of the passed string
    # courses = soup.find_all('h5') # .find_all() finds all the instances of the passed string    
    # for course in courses: # the for loop traverses through each h5 tags in the courses list
    #     print(course.text) # filters the tags to just get the text 
    course_cards = soup.find_all('div', class_='card')
    print(course_cards)
    for course in course_cards:
        course_name = course.h5.text # the .h5 ressembles the elements with the <h5> tag
        course_price = course.a.text.split()[-1] # ^^ same goes for this but here we are splitting by the blank and the index -1 is used to start from the end til we encounter the 1st space
        
        print(f'{course_name} costs {course_price}') # dynamic string printing (same sa old practices)
    