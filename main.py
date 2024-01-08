from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file: # 'html_file' is a variable name that we use to read the file contents and do operations with it
    content = html_file.read()
    # print(content)
    
    soup = BeautifulSoup(content, 'lxml') # note: lxml is a parsers
    # print(soup.prettify())
    # tags = soup.find('h5') # .find() finds the 1st instance of the passed string
    courses = soup.find_all('h5') # .find_all() finds all the instances of the passed string    
    for course in courses: # the for loop traverses through each h5 tags in the courses list
        print(course.text) # filters the tags to just get the text 