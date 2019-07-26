
from tkinter import *

root = Tk()
from bs4 import BeautifulSoup
import requests
import random
from difflib import get_close_matches
import webbrowser

def __init__(self):
    self.var = StringVar()
    self.city_name = StringVar()

    label = Label(text='Enter any city')
    label.grid(row=5, column=2)
    entry = Entry(textvariable=self.var)
    entry.grid(row=5, column=3)

    button_find = Button(text='Search', bd=4)
    button_find.grid(row=7, column=2, sticky=W, pady=8)

def cities_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    cities = soup.find_all("td", class_="cityOrCountryInIndicesTable")
    return self.city_name



def info_pollution(city):
    self.city_name = city.a.contents[0]
    pollution_level = city.span.contents[0]
    pollution_url = 'https://www.numbeo.com/pollution/rankings_current.jsp'+ city.a['href']
    pollution_level_page = requests.get(url)
    soup = BeautifulSoup(pollution_level_page.text, 'html.parser')
    return soup.find("div", class_="sorting_1").contents[0].strip()
    return self.city_name,pollution_level,pollution_url

def info_health(city):
    self.city_name = city.contents[0]
    health_index = city.contents[0]
    health_url = 'https://www.numbeo.com/health-care/rankings_current.jsp'+ city.a['href']
    health_index_page = requests.get(url)
    soup = BeautifulSoup(pollution_level_page.text, 'html.parser')
    return soup.find("div", class_="sorting_1").contents[0].strip()
    return self.city_name,health_index,health_url

def info_crime(city):
    self.city_name = city.contents[0]
    crime_rate = city.contents[0]
    crime_url = 'https://www.numbeo.com/crime/rankings_current.jsp'+ city.a['href']
    crime_rate_page = requests.get(url)
    soup = BeautifulSoup(pollution_level_page.text, 'html.parser')
    return soup.find("div", class_="sorting_1").contents[0].strip()
    return self.city_name,crime_rate,crime_url

def choose_city():
    self.city_name, pollution_level= info_pollution(city)
    self.city_name, health_index = info_health(city)
    self.city_name, crime_rate = info_crime(city)
    pollution_level= info_pollution(pollution_url)
    health_index = info_health(health_url)
    crime_rate= info_crime(crime_url)
    with open("cityfile.txt", "a+") as file:
        file.write(self.city_name)
        file.write(pollution_leve)
        file.write(health_index)
        file.write(crime_rate)
        file.write("\n")



def func1():
    if __name__ == '__main__':
        choose_city()


func1()
__init__()
label0 = Label(root, text="CHOOSE CITIES", bg="black", fg="white", font=("Arial", 20))
label0.grid(row=0)

root.title('CityInfo')
root.mainloop()
