# J7432_final-project
A scraper for all oilfield incidents listed on the North Dakota Department of Health website (http://www.ndhealth.gov/ehs/spills/), using the mechanize and Beautiful Soup 4 packages for python.

Run combined.py to scrape for all oilfield environmental incidents, which writes to a csv called output.csv.

Run new_contained.py to scrape for "oilfield environmental incidents that occurred within the last 12 months which were contained within the boundaries of the production or exploration facility." This program writes to a csv file called output1.csv.

Run new_notcontained.py to scrape for "oilfield environmental incidents that occurred within the last 12 months which were not contained, for example, an overflow of the boundaries of the facility or a leak from a facility pipeline." This program writes to a csv file called output2.csv.

Run older_all.py to scrape for "oilfield incidents older than 12 months." This program writes to a csv file called output3.csv.