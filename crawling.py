from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import re

def news_crawling():
    pass

def weather_crawling(city):
    browser = webdriver.Chrome()

    url = f'https://www.accuweather.com/ko/search-locations?query={city}'
    browser.get(url)

    link_list = browser.find_elements(By.XPATH, '/html/body/div/div[6]/div[1]/div[1]/div[1]/a[1]')
    link_data_list = []

    for elem in link_list:
        link = elem.get_attribute('href')
        link_data_list.append(link)

    browser.get(link_data_list[0])

    time.sleep(1)
    forecast_link = browser.find_element(By.CLASS_NAME, 'cur-con-weather-card').get_attribute('href')
    browser.get(forecast_link)

    time.sleep(1)
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    day_phrase = browser.find_element(By.XPATH, '/html/body/div/div[7]/div[1]/div[1]/div[4]/div[2]/div[1]').text
    night_phrase = browser.find_element(By.XPATH, '/html/body/div/div[7]/div[1]/div[1]/div[5]/div[2]/div[1]').text

    day_temperature = browser.find_element(By.XPATH, '/html/body/div/div[7]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div').text
    day_tprt_int = re.findall(r'\d+', day_temperature)
    day_tprt = [int(number) for number in day_tprt_int]

    night_temperature = browser.find_element(By.XPATH, '/html/body/div/div[7]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div').text
    night_tprt_int = re.findall(r'\d+', night_temperature)
    night_tprt = [int(number) for number in night_tprt_int]

    weather_info = f"{year}년 {month}월 {day}일 {city}의 최고기온은 {day_tprt[0]}°C, 최저기온은 {night_tprt[0]}°C입니다. 낮에는 {day_phrase}이고, 밤에는 {night_phrase}입니다."
    print(weather_info)

    return weather_info