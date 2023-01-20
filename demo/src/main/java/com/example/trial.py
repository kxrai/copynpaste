# Selenuim imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as selexcept

#try this code to see if it works

# Pandas imports using Pandas for structuring our data
import pandas as pd
from datetime import datetime
import os.path
import re
import sys
import glob

# Time and date-time (mainly for using delays between clicks)
import time

# Change this to your own chromedriver path!
chromedriver_path = 'Insert your own path'
    
# This will open the Chrome window
browser = webdriver.Chrome(executable_path=chromedriver_path)

# Setting Round Trip type path
return_ticket = "//label[@id='flight-type-roundtrip-label-hp-flight']"

def ticket_chooser(ticket):
    try:
        ticket_type = browser.find_element_by_xpath(ticket)
        ticket_type.click()
    except Exception as e:
        pass

def more_details(details):
    try:
        details_type = browser.find_element_by_xpath(details)
        details_type.click()
    except Exception as e:
        pass

def dep_country_chooser(dep_country):
    fly_from = browser.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")
    time.sleep(3)
    fly_from.clear()
    time.sleep(3)
    fly_from.send_keys('  ' + dep_country)
    time.sleep(3)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(3)
    first_item.click()

def arrival_country_chooser(arrival_country):
    fly_to = browser.find_element_by_xpath("//input[@id='flight-destination-hp-flight']")
    time.sleep(3)
    fly_to.clear()
    time.sleep(3)
    fly_to.send_keys('  ' + arrival_country)
    time.sleep(3)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(3)
    first_item.click()

def dep_date_chooser(month, day, year):
    dep_date_button = browser.find_element_by_xpath("//input[@id='flight-departing-hp-flight']")
    dep_date_button.clear()
    dep_date_button.send_keys(str(month) + "/" + str(day) + "/" + str(year))

def return_date_chooser(month, day, year):
    return_date_button = browser.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")
    for i in range(11):
        return_date_button.send_keys(Keys.BACKSPACE)
    return_date_button.send_keys(str(month) + "/" + str(day) + "/" + str(year))


def ProcessJourney(journeyDetails, i):
    ChooseFlight(journeyDetails, i)
    DataProcessing()            
    AmendTimeAndDate()    
    SaveDfToCsv(journeyDetails,i)
def DataProcessing():
    global df
    df = df[0:0]
    number_element_to_ignore = 0   
    
    # departure times
    dep_times = browser.find_elements_by_xpath("//span[@data-test-id='departure-time']")
    dep_times_list = [value.text for value in dep_times]
    
    # arrival times
    arr_times = browser.find_elements_by_xpath("//span[@data-test-id='arrival-time']")
    arr_times_list = [value.text for value in arr_times]
    
    # airline name
    airlines = browser.find_elements_by_xpath("//span[@data-test-id='airline-name']")
    airlines_list = [value.text for value in airlines]
        
    # durations
    durations = browser.find_elements_by_xpath("//span[@data-test-id='duration']")
    durations_list = [value.text for value in durations]
    
    # stops
    stops = browser.find_elements_by_xpath("//span[@class='number-stops']")
    stops_list = [value.text for value in stops]
    
    # layovers
    layovers = browser.find_elements_by_xpath("//span[@data-test-id='layover-airport-stops']")
    layovers_list = [value.text for value in layovers]
    
    # prices
    prices = browser.find_elements_by_xpath("//span[@data-test-id='listing-price-dollars']")
    price_list = [value.text for value in prices]
    
    # last flight to scrape according to the price differences (here we choose multiply by 2)  
    last_flight_index = CheckLastFlightIndexByPrice(price_list, 2)
    
    #Genrate flight to igonre according to the last_flight_index
    bad_indexes = GenerateBadIndex(dep_times_list, last_flight_index)

    # delete the non relevant flights
    for i in range(len(bad_indexes)):
        dep_times_list.pop(int(bad_indexes[i]))
        arr_times_list.pop(int(bad_indexes[i]))
    
    # Insert data to our DF
    for i in range(last_flight_index):
        try:
            df.loc[i, 'departure_time'] = dep_times_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'arrival_time'] = arr_times_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'airline'] = airlines_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'duration'] = durations_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'stops'] = stops_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'layovers'] = layovers_list[i]
        except Exception as e:
            pass
        try:
            df.loc[i, 'price'] = price_list[i]
        except Exception as e:
            pass
        try:
            # Adding flight details data
            number_element_to_ignore = AddingFlightDetails(i, stops_list, bad_indexes, number_element_to_ignore)
        except Exception as e:
            pass

def GetPathForExcelsOutPut(journeyDetails,i):
    dep_arr_name = journeyDetails.at[i,'dep_country_chooser'] + "_" + journeyDetails.at[i,'arrival_country_chooser']
    sampleTime   = "sampleTime_" + str(pd.to_datetime('today').strftime("%d/%m/%Y")).replace("/", "_")
    dep_date     = str("%02d" % journeyDetails.at[i,'dep_month']) + "_" + str("%02d" % journeyDetails.at[i,'dep_day']) + "_" + str(journeyDetails.at[i,'dep_year'])
    arr_date     = str("%02d" % journeyDetails.at[i,'arr_month']) + "_" + str("%02d" % journeyDetails.at[i,'arr_day']) + "_" + str(journeyDetails.at[i,'arr_year'])
    conc_date    = "depDate_" + dep_date + "_arrDate_" + arr_date 
    data_path = "Insert your data results folder here (the Parent folder that contain the all automatic subdir that will be created)"
    folderPath   = os.path.join(data_path,dep_arr_name, conc_date, 'sampleTime\\')
    return [folderPath, conc_date]
 
def SaveDfToCsv(journeyDetails,i):
    checkPathExist(journeyDetails,i)
    [pathForDepArrDate, nameOfFolder] = GetPathForExcelsOutPut(journeyDetails,i)
    df['departure_date'] = GetDepartDateUsingFolderName(nameOfFolder) # send file path to function
    df['arrival_date'] = GetReturnDateUsingFolderName(nameOfFolder) # send file path to function
    df.to_csv(str(GetPathForExcelsOutPut(journeyDetails,i)[0]) + "_" + dt.datetime.today().strftime('%y%m%d-%H%M%S')+ ".csv", index = False)
