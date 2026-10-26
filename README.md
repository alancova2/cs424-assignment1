# cs424-assignment2

Path to assignment1 README: 

## Task 1: Revisit your data and questions

Looking at my data it’s messier than I thought some labels don’t match, like “Daley 2nd Floor” and “Daley 2nd floor,” and some have extra spaces. There’s a typo, an empty column, and my times are in 12 hour format so 1:05 could be morning or afternoon. I have 30 observations from three days. Each posted rule is tied to one space, so I can’t tell if the rule or the space makes the difference. I also never counted how many seats each space has, occupancy is hard to compare between big and small spaces. I’ll redo the cleaning in a script that starts from my original observations.csv, where anyone can get the same cleaned file. It will fix the labels, change the times to 24 hour format, and add a “round” column for visits I made around the same time. I’m keeping my four questions from Assignment 1 with two changes. For the policy question I’m only going to describe the pattern since I can’t prove the rule is the cause. For the crowding question I’ll use head count as the main measure. I'm adding one new question. Which space is the best bet for a quiet seat, and how much does it change from visit to visit?

## Task 2: Prepare the data

I wrote a Python script in code/clean_data.py that cleans my original data. It reads observations.csv, which I never change and saves a cleaned copy to processed_data/observations_clean.csv. Anyone can run it and get the same file. The script gives the columns shorter names and drops the empty column from my Google Sheets. It cleans up extra spaces and fixes the labels, each space has one name and one type and it fixes the typo “Quite zone.” It changes the times to 24 hour format. I collected between about 9 AM and 5 PM, so a time like 1:05 must mean 13:05. The day of the week now comes from the date which fixes the “Thursady” typo. I added three new columns. One is the middle of each head count range. The second is a “round,” which groups visits I made around the same time. If more than 45 minutes pass between two visits a new round starts. That gave me six rounds with five visits each one for every space. The third labels each round as morning, midday, or afternoon. Towards the end of the script it checks that every rating is between 1 and 5 and that no head count minimum is higher than its maximum. If something is wrong it stops and tells me.

I ran it through CodeSpace and this is how I did it. Install pandas with pip install pandas. Then run python code/clean_data.py from the main folder of the repo. It reads observations.csv and saves the cleaned data to processed_data/observations_clean.csv.

## Task 3: Explore the data


## Task 4: Implement visualization alternatives






