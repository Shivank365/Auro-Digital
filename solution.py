from bs4 import BeautifulSoup

import os

def read_file(file_name):
    file_handle = open(file_name, 'r')
    data = file_handle.read()
    file_handle.close()
    return data


file_data = read_file('orders.xml')

file_data = file_data.split("\n")