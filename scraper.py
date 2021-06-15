import csv
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

#url1 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Atlanta%2C%2BGeorgia%2C%2BUnited%2BStates&geoId=106224388&trk=public_jobs_jobs-search-bar_search-submit&distance=100&position=1&pageNum=0'
#url2 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Houston%2C%2BTexas%2C%2BUnited%2BStates&geoId=103743442&trk=public_jobs_jobs-search-bar_search-submit&distance=100&position=1&pageNum=0'
#url3 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Washington%2C%2BDistrict%2Bof%2BColumbia%2C%2BUnited%2BStates&geoId=104383890&trk=public_jobs_jobs-search-bar_search-submit&distance=100&position=1&pageNum=0'
#url4 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Los%2BAngeles%2C%2BCalifornia%2C%2BUnited%2BStates&geoId=102448103&trk=public_jobs_jobs-search-bar_search-submit&distance=100&position=1&pageNum=0'
#Georgia scrapes
#Marshallville, 50 miles
ga_url1 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Marshallville%2C%2BGeorgia%2C%2BUnited%2BStates&geoId=103822070&trk=public_jobs_jobs-search-bar_search-submit&distance=50&position=1&pageNum=0'
#Thomasville, 50 miles
ga_url2 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Thomasville%2C%2BGeorgia%2C%2BUnited%2BStates&geoId=102477065&trk=public_jobs_jobs-search-bar_search-submit&distance=50&position=1&pageNum=0'
#Louisville, 50 miles
ga_url3 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Louisville%2C%2BGeorgia%2C%2BUnited%2BStates&geoId=102202429&trk=public_jobs_jobs-search-bar_search-submit&distance=50&position=1&pageNum=0'
#Comer, 25 miles
ga_url4 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Comer%2C%20Georgia%2C%20United%20States&geoId=103711946&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
#Richmond Hill, 50 miles
ga_url5 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Richmond%2BHill%2C%2BGeorgia%2C%2BUnited%2BStates&geoId=101323243&trk=public_jobs_jobs-search-bar_search-submit&distance=50&position=1&pageNum=0'
#Roopville, 50 miles
ga_url6 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Roopville%2C%2BGeorgia%2C%2BUnited%2BStates&geoId=103822980&trk=public_jobs_jobs-search-bar_search-submit&distance=50&position=1&pageNum=0'
#Cumming, 25 miles
ga_url7 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Cumming%2C%20Georgia%2C%20United%20States&geoId=102661238&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
#Calhoun, 25 miles
ga_url8 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Calhoun%2C%20Georgia%2C%20United%20States&geoId=100484068&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
ga_url_list = [ga_url1, ga_url2, ga_url3, ga_url4, ga_url5, ga_url6, ga_url7, ga_url8]

#Texas scrapes
#Houston, 50 miles
tx_url1 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Houston%2C%2BTexas%2C%2BUnited%2BStates&geoId=103743442&trk=public_jobs_jobs-search-bar_search-submit&distance=50&position=1&pageNum=0'
#San Antonio, 50 miles
tx_url2 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=San%2BAntonio%2C%2BTexas%2C%2BUnited%2BStates&geoId=102396835&trk=public_jobs_jobs-search-bar_search-submit&distance=50&position=1&pageNum=0'
#Round Rock, 10 miles
tx_url3 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Round%20Rock%2C%20Texas%2C%20United%20States&geoId=105523803&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&distance=10'
#Waco, 50 miles
tx_url4 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Waco%2C%2BTexas%2C%2BUnited%2BStates&geoId=103659815&trk=public_jobs_jobs-search-bar_search-submit&distance=50&position=1&pageNum=0'
#Fort Worth, 25 miles
tx_url5 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Fort%20Worth%2C%20Texas%2C%20United%20States&geoId=100432370&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
#Heath, 25 miles
tx_url6 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Heath%2C%20Texas%2C%20United%20States&geoId=104256779&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
#Abilene, 100 miles
tx_url7 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Abilene%2C%2BTexas%2C%2BUnited%2BStates&geoId=101330561&trk=public_jobs_jobs-search-bar_search-submit&distance=100&position=1&pageNum=0'
#Canyon, 100 miles
tx_url8 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Canyon%2C%2BTexas%2C%2BUnited%2BStates&geoId=102157510&trk=public_jobs_jobs-search-bar_search-submit&distance=100&position=1&pageNum=0'
tx_url_list = [tx_url1, tx_url2, tx_url3, tx_url4, tx_url5, tx_url6, tx_url7, tx_url8]

#DC area scrapes
#Warrenton, VA, 25 miles
dc_url1 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Warrenton%2C%20Virginia%2C%20United%20States&geoId=102759091&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
#Rockville, MD, 10 miles
dc_url2 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Rockville%2C%20Maryland%2C%20United%20States&geoId=100249151&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&distance=10'
#Springfield, VA, 10 miles
dc_url3 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Springfield%2C%2BVirginia%2C%2BUnited%2BStates&geoId=105794626&trk=public_jobs_jobs-search-bar_search-submit&distance=10&position=1&pageNum=0'
#Glenarden, MD, 10 miles
dc_url4 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=Glenarden%2C%2BMaryland%2C%2BUnited%2BStates&geoId=105259585&trk=public_jobs_jobs-search-bar_search-submit&distance=10&position=1&pageNum=0'
dc_url_list = [dc_url1, dc_url2, dc_url3, dc_url4]

total_url_list = [ga_url1, ga_url2, ga_url3, ga_url4, ga_url5, ga_url6, ga_url7, ga_url8, tx_url1, tx_url2, tx_url3, tx_url4, tx_url5, tx_url6, tx_url7, tx_url8, dc_url1, dc_url2, dc_url3, dc_url4]
chrome_path = '/usr/local/bin/chromedriver'

outfile = open('jobs_altanta.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(["job_title", "location", "job_desc", "applicants","company", "level", "job_length"])

atlanta_url_test = ['https://www.linkedin.com/jobs/search?keywords=Software%20Developer&location=Atlanta%2C%20GA&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0']


for url in atlanta_url_test:
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get(url)
    sleep(3)
    # action = ActionChains(driver)

    num_of_jobs = driver.find_element_by_css_selector('h1>span').get_attribute('innerText')
    num_of_jobs = num_of_jobs.replace(',','')
    num_of_jobs = num_of_jobs.replace('+','')
    num_of_jobs = int(num_of_jobs)
    #num_of_jobs = 20

    job_list = driver.find_element_by_class_name('jobs-search__results-list')
    jobs = []

    i = 1
    while i <= int(num_of_jobs/20):
        prev_len = len(jobs)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i += 1
        try:
            driver.find_element_by_class_name('infinite-scroller__show-more-button').click()
            sleep(5)
        except:
            print("NO BUTTON")
            pass
            sleep(3)
        jobs = job_list.find_elements_by_tag_name('li')
        print(str(len(jobs)))
        if len(jobs) == prev_len:
            break

    #job_list = driver.find_element_by_class_name('jobs-search__results-list')
    #jobs = job_list.find_elements_by_tag_name('li')

    for i in range(len(jobs)):
        #click_path = '/html/body/main/div/section[2]/ul/li[{}]/img'.format(str(i))
        #click = driver.find_element_by_xpath(click_path).click()
        #sleep(5)

        title = jobs[i].find_element_by_tag_name('h3').get_attribute('innerText')
        print(title)

        location = jobs[i].find_element_by_class_name('job-search-card__location').get_attribute('innerText')
        print(location)

        click = jobs[i].click()
        sleep(2)
        #desc_path = '/html/body/main/section/div[2]/section[2]/div'
        #desc_box = driver.find_element_by_xpath(desc_path)

        desc = driver.find_element_by_class_name('show-more-less-html__markup').get_attribute('innerHTML')
        print(desc)

        num_applicants = driver.find_element_by_class_name('num-applicants__caption').get_attribute('innerHTML')
        print(num_applicants)

        company = ""
        try:
            company = jobs[i].find_element_by_tag_name('h4').find_element_by_tag_name('a').get_attribute('innerHTML')
        except:
            pass
            company = jobs[i].find_element_by_css_selector('h4>div').get_attribute('innerHTML')
        print(company)

        criteria_list = driver.find_element_by_class_name('description__job-criteria-list')
        criterias = criteria_list.find_elements_by_tag_name('li')
        level = 'N/A'
        job_length = 'N/A'
        print(criterias)
        for criteria in criterias:
            print(criteria.find_element_by_class_name('description__job-criteria-subheader').get_attribute('innerHTML'))
            if 'Seniority level' in criteria.find_element_by_class_name('description__job-criteria-subheader').get_attribute('innerHTML'):
                level = criteria.find_element_by_class_name('description__job-criteria-text').get_attribute('innerHTML')
            if 'Employment type' in criteria.find_element_by_class_name('description__job-criteria-subheader').get_attribute('innerHTML'):
                job_length = criteria.find_element_by_class_name('description__job-criteria-text').get_attribute('innerHTML')
        print(level)
        print(job_length)

        writer.writerow([title, location, desc, num_applicants, company, level, job_length])