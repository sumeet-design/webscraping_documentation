# Hospital Project Documentation

This repository contains documentation for the hospital project, which involves extracting hospital and doctor details using web scraping. For demonstration purposes, a Python script `dump_helium.py` has been added to scrape data from a sample website. The repository also includes a folder named `data` which contains the expected output format for hospitals and doctors details in xlsx."

## Getting Started

To get started with the project, follow these steps:

### Installing Python

1. Download Python from the official website: [Python Downloads](https://www.python.org/downloads/).
2. Follow the installation instructions for your operating system.

### Installing Selenium and BeautifulSoup

1. Install Selenium using pip:
   ```bash
   pip install selenium
2. Install Beautifull Soup using pip
    ```bash
    pip install beautifulsoup4


### Project Description

We have to scraped hospital and doctor data for different countries, including India, UK, US, Turkey, and Saudi Arabia, and extracted various fields. For doctors, We have to captured details such as name, email, phone extension, phone number, user ID, gender, experience years, about, slug name, education, experience, specialization, list of treatments, papers published, awards, surgeries, rating, address, latitude, longitude, state, city, city ID, country ID, profile views, status, created at, updated at, avatar, profile link, telemedicine status, telemedicine fee, created by, updated by, is top, and source.

For hospitals, we have  to gathered information such as name, address, city ID, country ID, category, treatment availability, description, logo, hospital logo, profile views, latitude, longitude, key points, created by, created at, updated at, status, visible, establishment year, number of beds, number of ICU beds, operation theaters, popular for, team and speciality, infrastructure, state, URL safe, email, other emails, is top, and source.

### Data Format

The extracted data is stored in JSON format. Each entry contains the following fields:

#### For Doctors:
- `name`: Doctor's name
- `email`: Doctor's email
- `phone_extension`: Doctor's phone extension
- `phone_number`: Doctor's phone number
- `user_id`: Doctor's user ID
- `gender`: Doctor's gender
- `experience_years`: Doctor's years of experience
- `about`: Doctor's about section (about data should be in html format)
- `slug_name`: Doctor's slug name
- `education`: Doctor's education details
- `experience`: Doctor's experience details
- `specialization`: Doctor's specialization
- `treatments`: List of treatments offered by the doctor (treatment data should be in <ol> </ol> format)
- `papers_published`: Papers published by the doctor
- `awards`: Awards received by the doctor
- `surgeries`: Surgeries performed by the doctor
- `rating`: Doctor's rating
- `address`: Doctor's address
- `latitude`: Doctor's latitude
- `longitude`: Doctor's longitude
- `state`: Doctor's state
- `city`: Doctor's city
- `city_id`: Doctor's city ID
- `country_id`: Doctor's country ID
- `profile_views`: Doctor's profile views
- `status`: Doctor's status
- `created_at`: Doctor's creation date
- `updated_at`: Doctor's last update date
- `avatar`: Doctor's avatar
- `profile_link`: Doctor's profile link
- `telemedicine_status`: Doctor's telemedicine status
- `telemedicine_fee`: Doctor's telemedicine fee
- `created_by`: Doctor's creator
- `updated_by`: Doctor's last updater
- `is_top`: Doctor's top status
- `source`: Doctor's data source

#### For Hospitals:
- `name`: Hospital's name
- `address`: Hospital's address
- `city_id`: Hospital's city ID or city name
- `country_id`: Hospital's country ID or country name
- `category`: Hospital's category
- `treatment_availability`: Hospital's treatment availability
- `description`: Hospital's description (data should be in html format)
- `logo`: Hospital's logo
- `hospital_logo`: Hospital's hospital logo
- `profile_views`: Hospital's profile views
- `latitude`: Hospital's latitude
- `longitude`: Hospital's longitude
- `key_points`: Hospital's key points
- `created_by`: Hospital's creator
- `created_at`: Hospital's creation date
- `updated_at`: Hospital's last update date
- `status`: Hospital's status
- `visible`: Hospital's visibility
- `establishment_year`: Hospital's establishment year
- `num_beds`: Number of beds in the hospital
- `num_icu_beds`: Number of ICU beds in the hospital
- `operation_theaters`: Number of operation theaters in the hospital
- `popular_for`: Hospital's popular services
- `team_and_speciality`: Hospital's team and speciality (data should be html format)
- `infrastructure`: Hospital's infrastructure
- `state`: Hospital's state
- `url_safe`: Hospital's URL safe name
- `email`: Hospital's email
- `other_emails`: Hospital's other emails
- `is_top`: Hospital's top status
- `source`: Hospital's data source

The data should be organized in a structured manner to facilitate easy access and analysis.
