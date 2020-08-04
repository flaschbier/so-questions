#!/usr/bin/env python
# coding: utf-8

"""
https://stackoverflow.com/questions/63249142/web-scraping-content-not-showing-in-page-source
"""
# Created: 04.08.20

import json
# import bs4

if __name__ == "__main__":

    if 1 == 0: # Selenium -> takes ages
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager

        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver = webdriver.Chrome(ChromeDriverManager().install())

        url = 'https://foreclosures.cabarruscounty.us/'
        driver.get(url)

        # https://stackoverflow.com/a/63249528/3991164
        all_cards = driver.find_elements_by_xpath("//div[@class='card-body']/div[1]")
        for card in all_cards[:3]:
            print(card.text)  # do as you will
            print()
        print(f"total: {len(all_cards)}")

    else: # requests to API -> takes a few seconds
        import requests

        url = 'https://foreclosures.cabarruscounty.us/dataForeclosures.json'
        data = requests.get(url).json()
        data # place breakpoint here

