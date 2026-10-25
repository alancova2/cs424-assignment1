# cs424-assignment2

Path to assignment1 README: 

## Task 1: Revisit your data and questions

Looking at my data it’s messier than I thought some labels don’t match, like “Daley 2nd Floor” and “Daley 2nd floor,” and some have extra spaces. There’s a typo, an empty column, and my times are in 12 hour format so 1:05 could be morning or afternoon. I have 30 observations from three days. Each posted rule is tied to one space, so I can’t tell if the rule or the space makes the difference. I also never counted how many seats each space has, occupancy is hard to compare between big and small spaces. I’ll redo the cleaning in a script that starts from my original observations.csv, where anyone can get the same cleaned file. It will fix the labels, change the times to 24 hour format, and add a “round” column for visits I made around the same time. I’m keeping my four questions from Assignment 1 with two changes. For the policy question I’m only going to describe the pattern since I can’t prove the rule is the cause. For the crowding question I’ll use head count as the main measure. I'm adding one new question. Which space is the best bet for a quiet seat, and how much does it change from visit to visit?


## Task 2: Prepare the data




