import requests
from bs4 import BeautifulSoup as bs
import datetime
import os
import csv
# Program tracks amazon prices

# get url and create BeautifulSoup
def create_soup():
    url = input("Enter Amazon item url:\n")
    html = requests.get(url)
    soup = bs(html.text, 'html.parser')
    return soup

def find_date():
    # returns the current month/day/year
    now = datetime.datetime.now()
    return "{}\\{}\\{}".format(now.month,now.day,now.year)

def grab_item_info(soup):
    '''
    Grabs the itemsname, price, and the date Checked
    and stores those values. Date info is stored in
    date_info in the format of [Month,Day,Year]
    '''
    item_name = soup.title.text
    item_price = soup.find(id="priceblock_ourprice").text
    date_info = find_date()

    return [item_name, item_price, date_info]

def add_content_empty():
    '''
    Adds title headers to newly created csv file_exists
    '''
    csvfile = open("amazonPriceTracker.csv", 'a')
    writer = csv.writer(csvfile,delimiter=',')
    writer.writerow(['Item Name','Item Price','Date Checked'])
    csvfile.close()

def make_csv():
    '''
    Makes csv file if one is not present in the cwd
    '''
    working_directory = os.getcwd()
    os.chdir(working_directory)
    csv_file = open('amazonPriceTracker.csv', 'w')
    csv_file.close()
    add_content_empty()

def csv_file_check():
    # checks if csv file already made, make one if not
    working_directory = os.getcwd()
    if not os.path.exists('amazonTracking'):
        make_csv()

def add_content(info_list):
    working_directory = os.getcwd()
    os.chdir(working_directory)
    csvfile = open("amazonPriceTracker.csv", 'a')
    writer = csv.writer(csvfile)
    writer.writerow([info_list[0],info_list[1],info_list[2]])
    csvfile.close()
    

def csv_updater(info_list):
    '''
    info_list in the form of [item name,price,date checked]
    '''
    csv_file_check()
    add_content(info_list)

def notify_user():
    print("Price recorded in amazonPriceTracker.csv")

def main():
    soup = create_soup()
    info_list = grab_item_info(soup)
    csv_updater(info_list)
    notify_user()

main()
