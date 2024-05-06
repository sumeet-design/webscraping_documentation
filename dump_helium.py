from insertion import data_transaction
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
def slug(name):
    name = re.sub(r'\s+', ' ', name)
    slug_name = name.replace('. ', '-').replace('.', '-').replace(' ', '-').lower()
    
    return slug_name
clinics = []
def helium_doc(url):

    driver.get(url)
    clinic_links = driver.find_elements(By.XPATH,'//div[@class="listings-card-info-right"]//a')
    clinics.extend([i.get_attribute('href') for i  in clinic_links])
    
    for link in clinics:

        hospital= {
        'name' : [],
        'address' : [],
        'city_id' : [],
        'country_id' : [],
        'category' : [],
        'treatment_availability' : [],
        'description' : [],
        'logo' : [],
        'hospital_logo' : [],
        'profile_views' : [],
        'latitude' : [],
        'longitude' : [],
        'key_points' : [],
        'created_by' : [],
        'created_at' : [],
        'updated_at' : [],
        'status' : [],
        'visible' : [],
        'estb_year' : [],
        'no_of_beds' : [],
        'no_icu_beds' : [],
        'operation_theaters' : [],
        'popular_for' : [],
        'team_and_speciality' : [],
        'infastructure' : [],
        'state' : [],
        'url_safe' : [],
        'email' : [],
        'other_emails' : [],
        'is_top' : [],
    #     'source' : [],
        'doctors_profile_link':[], #no need of these two feilds in db
        'doctors_name': []
        }
        doctors = {
        'name' : [],
        'email' : [],
        'phone_extension' : [],
        'phone_number' : [],
        'user_id' : [],
        'gender' : [],
        'designation' : [],
        'experience_years' : [],
        'about' : [],
        'slug_name' : [],
        'education' : [],
        'experience' : [],
        'specialization' : [],
        'list_of_treatments' : [],
        'papers_published' : [],
        'awards' : [],
        'surgeries' : [],
        'rating' : [],
        'address' : [],
        'latitude' : [],
        'longitude' : [],
        'state' : [],
        'city' : [],
        'city_id' : [],
        'country_id' : [],
        'profile_views' : [],
        'status' : [],
        'created_at' : [],
        'updated_at' : [],
        'avatar' : [],
        'profile_link' : [],
        'telemedicine_status' : [],
        'telemedicine_fee' : [],
        'created_by' : [],
        'updated_by' : [],
        'is_top' : [],
        'source' : [],
        }
        



        driver.get(link)
        try:
            name_element = WebDriverWait(driver,10).until(EC.presence_of_element_located(
                (By.XPATH,'//h1[@class="clinic-name-header"]')))
            hospital['name'].append(name_element.text)
        except (TimeoutException,NoSuchElementException):
            hospital['name'].append(None)
        try: 
    
            address_element = WebDriverWait(driver,10).until(EC.presence_of_element_located(
        (By.XPATH,'//a[@class="clinic-body-link area-link"]')))
            hospital['address'].append(address_element.text)
        except (TimeoutException,NoSuchElementException):
            hospital['address'].append(None)
    
        try:
            city_id_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//p[@class="clinic-body-light"]'))).text
            hospital['city_id'].append(city_id_element)
        except (TimeoutException,NoSuchElementException):
            hospital['city_id'].append(None)
        hospital['country_id'].append('Saudi Arabia')
        hospital['category'].append(None)
        try:
            treament_element = WebDriverWait(driver,10).until(EC.presence_of_element_located(
        (By.XPATH,'//div[@class="treatment-section"]'))).text.split('\n')
            hospital['treatment_availability'].append(len(treament_element))
        
        except (TimeoutException,NoSuchElementException):
            hospital['treatment_availability'].append(None)
        try:
            lat_long_element = driver.find_element(By.XPATH, '//div[@id="map"]/a').get_attribute('href')

            latitude, longitude = re.findall(r'-?\d{1,2}\.\d+', lat_long_element)
            hospital['latitude'].append(latitude)
            hospital['longitude'].append(longitude)
        
            driver.switch_to.default_content()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error: {e}")
            print(f"Failed for link: {link}")
            hospital['latitude'].append(None)
            hospital['longitude'].append(None)
        hospital['logo'].append(None)
        hospital['hospital_logo'].append(None)
        try:
            doctors_profile = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="doctor-card-button-group-inner"]/a')))
            hospital['doctors_profile_link'].extend([i.get_attribute('href') for i in doctors_profile])
            
        except (NoSuchElementException, TimeoutException):
                hospital['doctors_profile_link'].append(None)

        try: 
            doctors_name = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="doctor-card-name-group-wrapper"]')))
            hospital['doctors_name'].extend(i.text.split('\n')[0] for i in doctors_name)
        except (NoSuchElementException, TimeoutException):
            hospital['doctors_name'].append(None)
        hospital['description'].append(None)
        hospital['profile_views'].append(None)
        
        hospital['key_points'].append(None)
        hospital['created_by'].append(None)
        hospital['created_at'].append(None)
        hospital['updated_at'].append(None)
        hospital['status'].append(None)
        hospital['visible'].append(None)
        hospital['estb_year'].append(None)
        hospital['no_of_beds'].append(None)
        hospital['no_icu_beds'].append(None)
        hospital['operation_theaters'].append(None)
        hospital['popular_for'].append(None)
        hospital['team_and_speciality'].append(None)
        hospital['infastructure'].append(None)
        hospital['state'].append(None)
        #hospital['url_safe'].append(None) #copy 
        # print("checking", hospital['name'][0])
        hospital['url_safe'].append(slug(hospital['name'][0]))
        # hospital['url_safe'].append("")
        hospital['email'].append(None)
        hospital['other_emails'].append(None)
        hospital['is_top'].append(None)
#         hospital['source'].append(None)
        #print("this is hospital data",hospital)
        
    #i think this should be inside the hospital for better data insertion in database 
    #improving data value 
        name = []
        email = []
        phone_extension = []
        phone_number = []
        user_id = []
        gender = []
        designation = []
        experience_years = []
        about = []
        slug_name = []
        education = []
        experience = []
        specialization = []
        list_of_treatments = []
        papers_published = []
        awards = []
        surgeries = []
        rating = []
        address = []
        latitude = []
        longitude = []
        state = []
        city = []
        city_id = []
        country_id = []
        profile_views = []
        status = []
        created_at = []
        updated_at = []
        avatar = []
        profile_link = []
        telemedicine_status = []
        telemedicine_fee = []
        created_by = []
        updated_by = []
        is_top = []
        source = []
        print("Length of doctor in each clinic clinic", len(hospital['doctors_profile_link']))
        for doc_link in hospital['doctors_profile_link']:
#             name = []

            #print("printing doctors link",hospital['doctors_profile_link'])
            driver.get(doc_link)
            try:
                doc_name_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//h1[@class="profile-header"]')))
#                 doctors['name'].append(doc_name_element.text)
                name.append(doc_name_element.text)
            except (NoSuchElementException, TimeoutException):
                name.append(None)
            email.append(None)
            phone_extension.append(None)
            phone_number.append(None)
            user_id.append(None)
            gender.append(None)
            try:
                designation_element =  WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//p[@class="profile-subheader"]'))).text.split('\n')[0]
                designation.append(designation_element)
            except (TimeoutException,NoSuchElementException):
                designation.append(None)
            try:
                experience_element =  WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//h1[@class="profile-experience"]'))).text       
                experience_years_ = re.findall(r'\d+',experience_element)
                print("Experience year",experience_years_)
                #fixing experience year 
                if len(experience_years_) >= 1:
                    experience_years.append(experience_years_[0])
                else:
                    experience_years.append(None)
                    
               # experience_years.append(experience_years_[0]) #fixed experience year
            except (TimeoutException,NoSuchElementException):
#                 experience_years.append(None)
                experience_years.append(None)
                 
            about.append(None)
            try:
                slug_name_element = doc_name_element.text.replace(' ','-')
                slug_name.append(slug_name_element)
            except (TimeoutException,NoSuchElementException):
                slug_name.append(None)

            try:
                education_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="col-sm-6 col-xs-12 credential-details"]/div)[2]'))).text.split(',')
                education.append('<ul>' + " ".join(f'<li>{word}</li>' for word in education_element )+'</ul>')
            except (TimeoutException,NoSuchElementException):
                education.append(None)

            try:
                special_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="col-sm-6 col-xs-12 speciality-details"]/div)[1]'))).text.split(',')
                specialization.append('<ul>' + " ".join(f'<li>{word}</li>' for word in special_element )+'</ul>')
            except (TimeoutException,NoSuchElementException):
                specialization.append(None)

            try:
                treat_element = WebDriverWait(driver,10).until(
                    EC.presence_of_element_located(
                            (By.XPATH,'(//div[@class="col-sm-6 col-xs-12 speciality-details"]/div)[3]'))).text.split(',')
                list_of_treatments.append('<ul>' + " ".join([f'<li>{word}</li>' for word in treat_element] )+'</ul>')
            except (TimeoutException,NoSuchElementException):
                list_of_treatments.append(None)
            try: 
                country_id_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'(//div[@class="col-sm-6 col-xs-12 credential-details"]/div)[1]')))
                country_id.append(country_id_element.text.split('\n')[1])
            except (TimeoutException,NoSuchElementException):
                country_id.append(None)
            try:
                avatar_element = WebDriverWait(driver,10).until(EC.presence_of_element_located(
            (By.XPATH,'//img[@class="profile-pic"]'))).get_attribute('src')
                avatar.append(avatar_element)
            except (TimeoutException,NoSuchElementException):
                avatar.append(None) 
            papers_published.append(None)
            awards.append(None)
            surgeries.append(None)
            rating.append(None)
            profile_link.append(None) 
            latitude.append(None)
            longitude.append(None)
            state.append(None)
            city_id.append(None)
            profile_views.append(None)
            status.append(None)
            created_at.append(None)
            updated_at.append(None)
            telemedicine_status.append(None)
            telemedicine_fee.append(None)
            created_by.append(None)
            updated_by.append(None)
            is_top.append(None)
            source.append(None)
            city.append(None)
            experience.append(None)
            address.append(None)
#         print("this is doctor data",doctors)
        
        doctors['name'].append(name)     #{"name":[dox1,doc2,doc3],"email":[e]}
        doctors['email'].append(email)
        doctors['phone_extension'].append(phone_extension)
        doctors['phone_number'].append(phone_number)
        doctors['user_id'].append(user_id)
        doctors['gender'].append(gender)
        doctors['designation'].append(designation)
        doctors['experience_years'].append(experience_years)
        doctors['about'].append(about)
        doctors['slug_name'].append(slug_name)
        doctors['education'].append(education)
        doctors['experience'].append(experience)
        doctors['specialization'].append(specialization)
        doctors['list_of_treatments'].append(list_of_treatments)
        doctors['papers_published'].append(papers_published)
        doctors['awards'].append(awards)
        doctors['surgeries'].append(surgeries)
        doctors['rating'].append(rating)
        doctors['address'].append(address)
        doctors['latitude'].append(latitude)
        doctors['longitude'].append(longitude)
        doctors['state'].append(state)
        doctors['city'].append(city)
        doctors['city_id'].append(city_id)
        doctors['country_id'].append(country_id)
        doctors['profile_views'].append(profile_views)
        doctors['status'].append(status)
        doctors['created_at'].append(created_at)
        doctors['updated_at'].append(updated_at)
        doctors['avatar'].append(avatar)
        doctors['profile_link'].append(profile_link)
        doctors['telemedicine_status'].append(telemedicine_status)
        doctors['telemedicine_fee'].append(telemedicine_fee)
        doctors['created_by'].append(created_by)
        doctors['updated_by'].append(updated_by)
        doctors['is_top'].append(is_top)
        doctors['source'].append(source)


            #removig used doctors link 
        hospital['doctors_profile_link'] = []
        #fixed doctor data and creating data frame for insertion
        for key,value in doctors.items():
            doctors[key] = value[0]   
        #creatig data frame for doctors
        # print("final doctor data",doctors)    
        df = pd.DataFrame(doctors)
        print(df)   # data frame created succesfully 
    #converting data in proper format
    # Remove the list in each value and convert 'nan' to None
        for key, value in hospital.items():
            if isinstance(value, list) and len(value) == 1:
                hospital[key] = value[0]
            if isinstance(value, str) and value.lower() == 'nan':
                hospital[key] = None
        # print("final hospital data",hospital)
        #need to call data insertion here 
        data_transaction(df,hospital)
        print("Transaction done successfully.............")
        
    driver.quit()

    
driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://www.heliumdoc.com/sa/clinics/'
helium_doc(url)