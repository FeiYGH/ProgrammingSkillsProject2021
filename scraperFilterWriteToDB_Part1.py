import csv
import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
import pymongo 


client = pymongo.MongoClient("mongodb+srv://FYang:higherNBrighter@tpworkready.g9ab0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#If doesn’t exist, will create this DB and table when script executed
db=client.jobskills_DB
job_postings_table=db.linkedIN_job_postings_table


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
tx_url2 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location=San Antonio%2C%2BTexas%2C%2BUnited%2BStates&geoId=102396835&trk=public_jobs_jobs-search-bar_search-submit&distance=50&position=1&pageNum=0'
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

# total_url_list = [ga_url1, ga_url2, ga_url3, ga_url4, ga_url5, ga_url6, ga_url7, ga_url8, tx_url1, tx_url2, tx_url3, tx_url4, tx_url5, tx_url6, tx_url7, tx_url8, dc_url1, dc_url2, dc_url3, dc_url4]
# chrome_path = '/usr/local/bin/chromedriver'

# outfile = open('jobs_dc.csv','w', newline='')
# writer = csv.writer(outfile)
# writer.writerow(["job_title", "location", "job_desc", "applicants","company", "level", "job_length"])


def getJobsFromSearch(writer, url, experience_filter):
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get(url=url)
    num_of_jobs = ""
    try:
        num_of_jobs = driver.find_element_by_css_selector('h1>span').get_attribute('innerText')
    except:
        driver.quit()
        return
    num_of_jobs = num_of_jobs.replace(',','')
    num_of_jobs = num_of_jobs.replace('+','')
    num_of_jobs = int(num_of_jobs)
    print('Total: ' + str(num_of_jobs) + ' jobs')
    #num_of_jobs = 20

    # further filter down by experience level to make smaller batches of jobs
    if num_of_jobs >= 1000 and not experience_filter:
        filteredScrape(writer, driver.current_url)
    else:
        job_list = driver.find_element_by_class_name('jobs-search__results-list')
        jobs = []
        jobs = job_list.find_elements_by_tag_name('li')
        
        count = 1
        while count <= int(num_of_jobs/25):
            prev_len = len(jobs)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            count += 1
            try:
                driver.find_element_by_class_name('infinite-scroller__show-more-button').click()
                sleep(2)
            except:
                print("NO BUTTON")
                pass
                sleep(2)
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

            id_str = jobs[i].find_element_by_class_name('base-search-card').get_attribute('data-entity-urn')
            id_list = id_str.split(':')
            id = id_list[len(id_list)-1]

            title = jobs[i].find_element_by_tag_name('h3').get_attribute('innerText')
            print(title)

            location = jobs[i].find_element_by_class_name('job-search-card__location').get_attribute('innerText')
            print(location)

            click = jobs[i].click()
            sleep(1)
            #desc_path = '/html/body/main/section/div[2]/section[2]/div'
            #desc_box = driver.find_element_by_xpath(desc_path)

            for j in range(3):
                try:
                    desc = driver.find_element_by_class_name('show-more-less-html__markup').get_attribute('innerHTML').strip()
                    break
                except:
                    sleep(1)
            print(desc)

            for j in range(3):
                try:
                    num_applicants = driver.find_element_by_class_name('num-applicants__caption').get_attribute('innerHTML').strip()
                    break
                except:
                    sleep(1)
            print(num_applicants)

            company = ""
            try:
                company = jobs[i].find_element_by_tag_name('h4').find_element_by_tag_name('a').get_attribute('innerHTML').strip()
            except:
                pass
                company = jobs[i].find_element_by_css_selector('h4>div').get_attribute('innerHTML').strip()
            print(company)

            sleep(1)
            check_count = 0
            for j in range(3):
                try: 
                    criteria_list = driver.find_element_by_class_name('description__job-criteria-list')
                    break
                except:
                    sleep(1)
                    check_count += 1
            criterias = criteria_list.find_elements_by_tag_name('li')
            level = 'N/A'
            job_length = 'N/A'
            #print(criterias)
            if check_count < 3:
                sleep(1)
                for criteria in criterias:
                    for j in range(3):
                        try:
                            #print(criteria.find_element_by_class_name('description__job-criteria-subheader').get_attribute('innerHTML'))
                            if 'Seniority level' in criteria.find_element_by_class_name('description__job-criteria-subheader').get_attribute('innerHTML'):
                                level = criteria.find_element_by_class_name('description__job-criteria-text').get_attribute('innerHTML').strip()
                                break
                            if 'Employment type' in criteria.find_element_by_class_name('description__job-criteria-subheader').get_attribute('innerHTML'):
                                job_length = criteria.find_element_by_class_name('description__job-criteria-text').get_attribute('innerHTML').strip()
                                break
                        except:
                            pass
            print(level)
            print(job_length)

            job_posting_to_add = {
                "_id": id,
                "title": title,
                "location": location,
                "desc": desc,
                "num_applicants": num_applicants,
                "company": company,
                "level": level,
                "job_length": job_length

            }

            try:
                job_postings_table.insert_one(job_posting_to_add)
            except:
                job_postings_table.update_one({'_id': id}, {'$set': {"title": title,
                "location": location,
                "desc": desc,
                "num_applicants": num_applicants,
                "company": company,
                "level": level,
                "job_length": job_length}})

            writer.writerow([title, location, desc, num_applicants, company, level, job_length])
        sleep(10)
        driver.quit()


def filteredScrape(writer, base_url):
    print(base_url)
    for i in range(1, 6):
        getJobsFromSearch(writer, base_url + '&f_E=' + str(i), True)
        sleep(3)


def openAndGrabLinkedInJobs(writer, cityAndState):
    driver = webdriver.Chrome(executable_path=chrome_path)

    print(cityAndState)
    #navigate to linkedIN
    driver.get("https://www.linkedin.com/jobs?trk=homepage-basic_directory_jobsHomeUrl")

    inputJobSection = driver.find_element_by_class_name("keywords-typeahead-input")
    inputJobSection.find_element_by_class_name("dismissable-input__input").send_keys("Software Developer")

    inputCityStateSection = driver.find_element_by_class_name("location-typeahead-input")
    inputCityStateSection.find_element_by_class_name("dismissable-input__input").clear()
    inputCityStateSection.find_element_by_class_name("dismissable-input__input").send_keys(cityAndState)
    inputCityStateSection.find_element_by_class_name("dismissable-input__input").send_keys(Keys.RETURN)

    #searchButtons = driver.find_elements_by_class_name('search__button')
    #searchButtons[1].click()

    sleep(1)
    # action = ActionChains(driver)

    getJobsFromSearch(writer, driver.current_url, False)

    driver.quit()
    sleep(3)


chrome_path = '/usr/local/bin/chromedriver'
outfile = open('jobs_topten.csv','w', newline='')
writer = csv.writer(outfile)
writer.writerow(["job_title", "location", "job_desc", "applicants","company", "level", "job_length"])
biggestuscitieslink = "https://www.biggestuscities.com/"
all_cities = []

# most likely will delete
# linkedInlink1 = 'https://www.linkedin.com/jobs/search?keywords=Software%2BDeveloper&location='
# linkedInlink2 = '%2C%20United%20States&geoId=102759091&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

#states = ["tx", "ga", "md", "va", "dc" ]
#statesFullName = ['Texas', 'Georgia', 'Maryland', 'Virginia', 'District of Columbia']
states = ['ga']
statesFullName = ['Georgia']
 

i = 0; 
for state in states:
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get(biggestuscitieslink + state)
    sleep(1)
    

#     #job_list = driver.find_element_by_class_name('jobs-search__results-list')
#     #jobs = job_list.find_elements_by_tag_name('li')
    top_populated_table = driver.find_element_by_class_name("table-striped")
    cities = top_populated_table.find_elements_by_class_name("big")
    
    state = statesFullName[i]
    print(state)

    full_locations = []

    if state == "District of Columbia":
        print('state is dc')
        cityAndState = 'District of Columbia'
        openAndGrabLinkedInJobs(writer, driver, cityAndState)
    else:
        for k in range(10): 
            cityName = cities[k].find_element_by_tag_name('a').get_attribute('innerHTML')
            print(cityName)
            cityAndState = cityName + ', ' + state
            full_locations.append(cityAndState)
    i+=1

    for location in full_locations:
        openAndGrabLinkedInJobs(writer, location)



 

# for url in total_url_list:
#     driver = webdriver.Chrome(executable_path=chrome_path)
#     driver.get(url)
#     sleep(3)
#     # action = ActionChains(driver)

#     num_of_jobs = driver.find_element_by_css_selector('h1>span').get_attribute('innerText')
#     num_of_jobs = num_of_jobs.replace(',','')
#     num_of_jobs = num_of_jobs.replace('+','')
#     num_of_jobs = int(num_of_jobs)
#     #num_of_jobs = 20

#     job_list = driver.find_element_by_class_name('jobs-search__results-list')
#     jobs = []
    
#     i = 1
#     while i <= int(num_of_jobs/20):
#         prev_len = len(jobs)
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         i += 1
#         try:
#             driver.find_element_by_class_name('infinite-scroller__show-more-button').click()
#             sleep(5)
#         except:
#             print("NO BUTTON")
#             pass
#             sleep(5)
#         jobs = job_list.find_elements_by_tag_name('li')
#         print(str(len(jobs)))
#         if len(jobs) == prev_len:
#             break

#     #job_list = driver.find_element_by_class_name('jobs-search__results-list')
#     #jobs = job_list.find_elements_by_tag_name('li')

#     for i in range(len(jobs)):
#         #click_path = '/html/body/main/div/section[2]/ul/li[{}]/img'.format(str(i))
#         #click = driver.find_element_by_xpath(click_path).click()
#         #sleep(5)

#         title = jobs[i].find_element_by_tag_name('h3').get_attribute('innerText')
#         print(title)

#         location = jobs[i].find_element_by_class_name('job-search-card__location').get_attribute('innerText')
#         print(location)

#         click = jobs[i].click()
#         sleep(2)
#         #desc_path = '/html/body/main/section/div[2]/section[2]/div'
#         #desc_box = driver.find_element_by_xpath(desc_path)

#         desc = driver.find_element_by_class_name('show-more-less-html__markup').get_attribute('innerHTML')
#         print(desc)

#         num_applicants = driver.find_element_by_class_name('num-applicants__caption').get_attribute('innerHTML')
#         print(num_applicants)

#         company = ""
#         try:
#             company = jobs[i].find_element_by_tag_name('h4').find_element_by_tag_name('a').get_attribute('innerHTML')
#         except:
#             pass
#             company = jobs[i].find_element_by_css_selector('h4>div').get_attribute('innerHTML')
#         print(company)

#         criteria_list = driver.find_element_by_class_name('description__job-criteria-list')
#         criterias = criteria_list.find_elements_by_tag_name('li')
#         level = 'N/A'
#         job_length = 'N/A'
#         print(criterias)
#         for criteria in criterias:
#             print(criteria.find_element_by_class_name('description__job-criteria-subheader').get_attribute('innerHTML'))
#             if 'Seniority level' in criteria.find_element_by_class_name('description__job-criteria-subheader').get_attribute('innerHTML'):
#                 level = criteria.find_element_by_class_name('description__job-criteria-text').get_attribute('innerHTML')
#             if 'Employment type' in criteria.find_element_by_class_name('description__job-criteria-subheader').get_attribute('innerHTML'):
#                 job_length = criteria.find_element_by_class_name('description__job-criteria-text').get_attribute('innerHTML')
#         print(level)
#         print(job_length)

#         writer.writerow([title, location, desc, num_applicants, company, level, job_length])