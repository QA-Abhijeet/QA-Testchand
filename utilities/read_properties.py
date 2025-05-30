#to read common hardcoded data. like username password url

import configparser


config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
