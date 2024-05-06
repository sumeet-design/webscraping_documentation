import time
import pandas as pd
import re
import numpy as np
import mysql.connector


hos_cols = ['name', 'address', 'city_id', 'country_id', 'category', 'treatment_availability', 'description', 'logo', 'hospital_logo', 'profile_views', 'latitude', 'longitude', 'key_points', 'created_by', 'created_at', 'updated_at', 'status', 'visible', 'estb_year', 'no_of_beds', 'no_icu_beds', 'operation_theaters', 'popular_for', 'team_and_speciality', 'infastructure', 'state', 'url_safe', 'email', 'other_emails', 'is_top']#, 'source']
doc_cols = ['name', 'email', 'phone_extension', 'phone_number', 'user_id', 'gender', 'designation', 'experience_years', 'about', 'slug_name', 'education', 'experience', 'specialization', 'list_of_treatments', 'papers_published', 'awards', 'surgeries', 'rating', 'address', 'latitude', 'longitude', 'state', 'city', 'city_id', 'country_id', 'profile_views', 'status', 'created_at', 'updated_at', 'avatar', 'profile_link', 'telemedicine_status', 'telemedicine_fee', 'created_by', 'updated_by', 'is_top']#, 'source']
#Aopllo xyz = aopllo-xyz-

def doctors_slug(x, df):
    name_counts = {}
    def slug(name):
        name = re.sub(r'\s+', ' ', name)
        slug_name = name.replace('. ', '-').replace('.', '-').replace(' ', '-').lower()
        if slug_name not in name_counts:
            name_counts[slug_name] = 1
        elif name_counts[slug_name] == 1:
            pass
        else:
            name_counts[slug_name] += 1
            slug_name += '-' + str(name_counts[slug_name])
        slug_name += str(x)
        return slug_name
    
    df['slug_name'] = df['name'].apply(slug)
    
    return df

def hospital_insertion(connection, cursor, d, current_timestamp):
    original_slug = d['url_safe']
    new_slug = original_slug
    suffix = 1

    check_query = "SELECT id FROM hospitals WHERE url_safe = %s"
    cursor.execute(check_query, (new_slug,))
    result = cursor.fetchone()

    while result:
        new_slug = f"{original_slug}-{suffix}"
        cursor.execute(check_query, (new_slug,))
        result = cursor.fetchone()
        suffix += 1
    d['url_safe'] = new_slug
    d['created_at'] = current_timestamp
    d['updated_at'] = current_timestamp
    
    d['country_id'] = 101
    d['city_id'] = 1558

    #adding more coloumns for hospital data
    d["status"] = 2
    d["visible"] =0
    d["is_top"] = 0
#         d["source"] = [1,1]
    d["is_partner"] = 0
    d["created_by"] = 1
    d["category"] = 1
    d["treatment_availability"] = 3
    temp_data = []
    for x in hos_cols:
        temp_data.append(d[x])
        
    hospital = [tuple(temp_data)]
    print("length and hospital data",temp_data,len(temp_data))

    insertion_query = """
        INSERT INTO hospitals (
            name, address, city_id, country_id, category, treatment_availability, description, logo, hospital_logo, profile_views, latitude, longitude, key_points, created_by, created_at, updated_at, status, visible, estb_year, no_of_beds, no_icu_beds, operation_theaters, popular_for, team_and_speciality, infastructure, state, url_safe, email, other_emails, is_top
        ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    num_placeholders = insertion_query.count('%s')
    print(f"Number of placeholders in the query: {num_placeholders}")
    
    cursor.executemany(insertion_query, hospital)
    connection.commit()
    print("Hospital Data inserted successfully.")
    
    return d['city_id'], d['country_id']
    
def doctor_insertion(connection, cursor, df, country_id, city_id, current_timestamp):
    print("Now I am inserting data into Doctors db...........")
    doctors = []
    for i in range(len(df)):
        temp = []
        for x in doc_cols:
            if x == 'country_id':
                temp.append(country_id)
            elif x == 'city_id':
                temp.append(city_id)
            elif x == 'created_at' or x == 'updated_at':
                temp.append(current_timestamp)
            elif x == 'created_by' or x == 'updated_by':
                temp.append(1)
                
            elif pd.isna(df[x][i]):
                temp.append(None)
            else:
                if x == 'experience_years':
                    temp.append(str(int(df[x][i])))
                elif x in ['gender', 'profile_views', 'status', 'is_top', 'source']:
                    temp.append(int(str(int(df[x][i]))))
                else:
                    temp.append(df[x][i])
        doctors.append(tuple(temp))
    insertion_query = """
        INSERT INTO doctors (
            name, email, phone_extension, phone_number, user_id, gender, designation, experience_years, about, slug_name, education, experience, specialization, list_of_treatments, papers_published, awards, surgeries, rating, address, latitude, longitude, state, city, city_id, country_id, profile_views, status, created_at, updated_at, avatar, profile_link, telemedicine_status, telemedicine_fee, created_by, updated_by, is_top
        ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    #checking length 
    
    
    cursor.executemany(insertion_query, doctors)
    connection.commit()
    print("Doctors Data inserted successfully.")
    
def dtd_insertion(connection, cursor, slug_names, safe_url, current_timestamp):
    query = f'''SELECT id FROM hospitals WHERE url_safe=%s;'''
    cursor.execute(query, (safe_url,))
    result = cursor.fetchone()
    if result:
        hospital_id = result[0]
    else:
        hospital_id = None
    doctor_ids = []
    for slug_name in slug_names:
        query = f'''SELECT max(id) FROM doctors WHERE slug_name=%s;'''
        cursor.execute(query, (slug_name,))
        result = cursor.fetchone()
        if result: 
            doctor_ids.append(result[0])
        else:
            doctor_ids.append(None)
    doctor_hospital = []
    for x in doctor_ids:
        doctor_hospital.append(tuple([hospital_id, x, 1, 1, None, None, None, None, None, None, None, 2, current_timestamp, current_timestamp, 1, 1]))
    print("dtd",doctor_hospital)
    insertion_query = """
        INSERT INTO doctors_treatment_details (
            hospital_id, doctor_id, disease_department_id, diseases_id, min_price, max_price, approximate_price_inr, cost_remark, stay_hospital, stay_india, description, status, created_at, updated_at, created_by, updated_by
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
   
    cursor.executemany(insertion_query, doctor_hospital)
    connection.commit()
    print("Doctor Treatment Details Data inserted successfully.")
    

        
def data_transaction(df, d):
    host = "localhost"
    username = "root"
    password = "1234"
    database = "hosptial_details_db"
    print("I am above try button")
    try:
        print("I am in try")
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        print("connection secured")
        if connection.is_connected():
            print("Connected to MySQL")

            cursor = connection.cursor()

            current_timestamp = int(time.time())
            
            # Generating Slug Name
            df = doctors_slug(current_timestamp, df)   #x = timestamp
            
            
            # Inserting hospital data 
            city_id, country_id = hospital_insertion(connection, cursor, d, current_timestamp)

            
            # Inserting doctors data
            doctor_insertion(connection, cursor, df, country_id, city_id, current_timestamp)
            print("dtd insertion",list(df['slug_name']),d['url_safe'])
            # Inserting Doctor treatment details data
            dtd_insertion(connection, cursor, list(df['slug_name']), d['url_safe'], current_timestamp)
            
            print("Transaction completed successfully!!!!!")
            
    except mysql.connector.Error as error:
        print("Error: {}".format(error))

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")




# d = {}
# for i, x in enumerate(hos_cols): 
#     d[x] = None

# d["name"] = hospital_name #
# d["no_of_beds"] = bed
# d["hospital_logo"] = hospital_logo
# d["address"] = address
# d["latitude"] = latitude
# d["longitude"] = longitude
# d["description"] = desc
# d["team_and_speciality"] = team_and_specialty

# d['city_id'] = 'Mumbai'
# d['country_id'] = 'India'

# d['estb_year'] = estb
# d['logo'] = None
# d['created_by'] = 1
# d['source'] = 1
# d['is_top'] = 0
# d['url_safe'] = d['name'].replace('. ', '-').replace('.', '-').replace(' ', '-').lower()
# d['category'] = 1
# d['treatment_availability'] = 3
# d['status'] = 2
# d['visible'] = 0
# d['profile_views'] = 0

# data_transaction(df, d)  #df = doctor  dic  d = hospital


# d = {"name ":"hosa"}
# df = {name:["doc1","doc2","doc3"]}