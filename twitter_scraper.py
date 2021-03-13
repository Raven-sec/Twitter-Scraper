#!/bin/python3

import csv 
import pandas as pd 
import pyfiglet
import snscrape.modules.twitter as sntwitter
import sys 

script_name = pyfiglet.figlet_format("Twitter Scraper")
print(script_name)

tweets_list = []

try:
	if len(sys.argv) <1:
		print(f"Usage: python3 {sys.argv[0]} <twitter profile name>")
	else:
		print(f"[] Scraping tweets from {sys.argv[1]}...")
		for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{sys.argv[1]}').get_items()):
			if i > 500:
				break
			tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.username]) 
		for item in tweets_list:
			print (item)
		print("\n")
		print("[+] Tweets retrieved")
		print("\n")

	decision = input('Write to CSV?? y or n ')
	if decision == "y":
		PrintList = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
		with open(f'{sys.argv[1]}.csv', 'w', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(['Datetime', 'Tweet Id', 'Text', 'Username'])
			writer.writerows(tweets_list)
			print("[+] CSV Created")
			print("\n")
			print(f"Goodbye from {sys.argv[0]}!")
			sys.exit()
	elif decision == "n":
		print(f"Exiting {sys.argv[0]}...")
		sys.exit(1)
	else:
		print("Please supply \'y\' or \'n\'")
		sys.exit(1)

except KeyboardInterrupt:
	print(f"{sys.argv[0]} interrupted...")
	sys.exit(1)

