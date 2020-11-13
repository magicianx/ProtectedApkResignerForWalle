#!/usr/bin/python  
#-*-coding:utf-8-*-
import configparser

conf = configparser.ConfigParser()
conf.read('config.ini', encoding='utf-8')

def getSection(section):
	return conf[section]
