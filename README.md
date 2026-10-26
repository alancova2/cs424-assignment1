# cs424-assignment2

## Task 1: Revisit your data and questions

Looking at my data it’s messier than I thought some labels don’t match, like “Daley 2nd Floor” and “Daley 2nd floor,” and some have extra spaces. There’s a typo, an empty column, and my times are in 12 hour format so 1:05 could be morning or afternoon. I have 30 observations from three days. Each posted rule is tied to one space, so I can’t tell if the rule or the space makes the difference. I also never counted how many seats each space has, occupancy is hard to compare between big and small spaces. I’ll redo the cleaning in a script that starts from my original observations.csv, where anyone can get the same cleaned file. It will fix the labels, change the times to 24 hour format, and add a “round” column for visits I made around the same time. I’m keeping my four questions from Assignment 1 with two changes. For the policy question I’m only going to describe the pattern since I can’t prove the rule is the cause. For the crowding question I’ll use head count as the main measure. I'm adding one new question. Which space is the best bet for a quiet seat, and how much does it change from visit to visit?

## Task 2: Prepare the data

I wrote a Python script in code/clean_data.py that cleans my original data. It reads observations.csv, which I never change and saves a cleaned copy to processed_data/observations_clean.csv. Anyone can run it and get the same file. The script gives the columns shorter names and drops the empty column from my Google Sheets. It cleans up extra spaces and fixes the labels, each space has one name and one type and it fixes the typo “Quite zone.” It changes the times to 24 hour format. I collected between about 9 AM and 5 PM, so a time like 1:05 must mean 13:05. The day of the week now comes from the date which fixes the “Thursady” typo. I added three new columns. One is the middle of each head count range. The second is a “round,” which groups visits I made around the same time. If more than 45 minutes pass between two visits a new round starts. That gave me six rounds with five visits each one for every space. The third labels each round as morning, midday, or afternoon. Towards the end of the script it checks that every rating is between 1 and 5 and that no head count minimum is higher than its maximum. If something is wrong it stops and tells me.

I ran it through CodeSpace and this is how I did it. Install pandas with pip install pandas. Then run python code/clean_data.py from the main folder of the repo. It reads observations.csv and saves the cleaned data to processed_data/observations_clean.csv.

## Task 3: Explore the data

### Noise, groups, and space 
My first chart of noise against the group/solo rating looked almost empty. That was misleading, because many visits had the same two numbers and their dots sat on top of each other.

First noise vs. group mix chart, dots overlapping
After I added jitter every visit showed up and a clear pattern appeared. Visits with more groups were louder, and this was the strongest link in my data a rank correlation of about 0.81.

Noise vs. group mix with jitter
But groups don’t explain everything. At a group rating of 4, noise ranged from 2 to 5, and the loudest visits were all in the library’s collaborative zone. Splitting noise up by space makes this clearer. The Daley 4th Floor was a 1 on all six visits, and the Daley 2nd Floor was always 3 to 5. I still can’t say the posted rule is the reason because each rule belongs to one space.

Noise level in every visit, by space
One visit stood out as odd. On Thursday at 11:15, the CS Lounge was a 1 for noise with 15 to 20 people there while other visits with the same head count were a 2 or 3.

Crowds over the day
I plotted occupancy over the six rounds to look at Question 1. The library floors were fullest on Tuesday morning and midday, dropped on Tuesday afternoon, and went back up on Thursday. The CS Office Hours never got above a 2.

Occupancy rating for each space across the six rounds
This chart is limited by how I collected the data. There are only six rounds, they aren’t evenly spaced, and day and time are mixed together. Friday morning was lower than Tuesday morning but I can’t tell if that’s because of Friday or just that one day.

A problem with my ratings
I expected head count and my occupancy rating to say the same thing. They mostly agree since every visit with 150 or more people got a 4 or 5. But the rating isn’t the same across spaces. About 22 people in the CS Lounge got a 4 while 55 people on the 4th floor got a 2.

Head count compared with my occupancy rating
My rating is really how full a space felt for its size, and I never counted seats, I can’t compare big and small spaces fairly. My ratings also weren’t always consistent. The CS Lounge had 15 to 20 people on four visits and I rated it a 2 on some and a 3 on others.

A good bet for a quiet seat
For my new question I counted a visit as a good bet if noise was 2 or lower and occupancy was 3 or lower. CS Office Hours was a good bet on all six visits, the CS Lounge on three, the Daley 4th Floor and Student Center Lounge on two each and the Daley 2nd Floor on none.

Number of good bet visits for each space
The surprise was the quiet floor which only got 2 out of 6 because it was quiet every time but usually crowded. This result depends a lot on where I draw the line. If I allow occupancy up to 4 the 4th floor goes to 6 out of 6. The counts also hide how close each miss was since a visit that just missed the cutoff counts the same as a very loud, packed one.


## Task 4: Implement visualization alternatives

# Direction 1: Occupancy over time

Occupancy over time, one line per space. This line chart is for Question 1 how each space changes during the day. It uses the round, my occupancy rating, and the space. Each dot is one visit, how high it sits shows how full the space was, and each space has its own color and line. I tried it because I wanted changes over time to look like a shape, which is easier to compare than the colored boxes in my Sketch 1. It worked for the big changes like the library dropping on Tuesday afternoon and the CS Office Hours staying low. But I only have six rounds, they aren’t spaced evenly, and the lines connect Tuesday to Thursday like no time passed. When two spaces have the same number their lines cover each other. I’m going to change it by breaking the lines between days and adding head count so the size of the crowd shows up.

# Direction 2: Noise by space

Noise in every visit, one column per space. This dot plot is for Question 2 whether spaces follow their posted rules. It uses the space and the noise level. Each dot is one visit, and I moved them a little so they don’t hide each other. My Sketch 2 used averages, this time I wanted to see every visit and how much each space changes. It worked well. The quiet floor sits at 1 every time, the collaborative floor is 3 to 5, and the odd CS Lounge visit really stands out. But it only shows noise, it says nothing about crowds or time, and it can’t tell me if the rule or the space causes the difference. I’m keeping it because it answers Question 2 clearly and I’ll add each space’s posted rule under its name.

# Direction 3: Noise vs group mix

Noise vs group mix, one dot per visit. This scatterplot is for Question 4 whether the mix of groups and solo people is connected to noise. It uses the group/solo rating, the noise level, and the space. Each dot is one visit, where it sits shows group mix and noise, and the color shows the space. After Assignment 1, I noticed none of my sketches showed single visits, so this one gives every visit its own dot. It shows a clear pattern more groups means more noise. Adding jitter also fixed my first version where dots were hiding behind each other. The problem is that most of the pattern comes from differences between spaces, not changes inside one space, and both ratings are just my own guesses. I’ll combine it with Question 3 by making each dot bigger when the head count is bigger.

# Direction 4: Good bet for a quiet seat

Number of good bet visits for each space. This bar chart is for my new question, which space is the best bet for a quiet seat. It uses the space, the noise level, and my occupancy rating, which I turn into a yes or no for “good bet.” A longer bar means more visits were a good bet. I wanted a direct answer to the question I ask myself, where should I go? It’s easy to read, and it shows the surprise that the quiet floor only got 2 out of 6. But the cutoff is fixed the bars don’t show how close a miss was and with only six visits per space, one visit changes a bar a lot. It also doesn’t show how a space changes from visit to visit which my question asks about. I’ll change it so people can pick their own noise and crowd limits.


## Task 5: Interaction and multiple views

I only want to add interaction when it helps me answer one of my questions. I have 30 visits, so zooming and panning wouldn’t help. Everything fits on the screen already. Sliders for noise and crowd limits. This is the one I care about most. When I counted occupancy up to 3, the quiet floor was a good bet on only 2 out of 6 visits. When I counted up to 4, it was a good bet on all 6. So the answer changes depending on where I draw the line and different people can handle different amounts of noise and crowding. My good bet chart will have two sliders, one for the most noise someone will put up with and one for the most crowding. The bars will change as they move. That way people can find the best place for themselves and don’t have to trust my cutoff.

Hover for details when you point at a dot, a small box will pop up with the space, the date and time, the head count, and my notes about how loud and full it was. I saved those notes when I cleaned the data, and this is where they’ll be useful. Like in the CS Lounge visit on Thursday at 11:15 had a noise level of 1 with 15 to 20 people there. Reading my notes next to that dot tells you more than the number does. Linked views, I want to use two or three charts together the good bet bars, the noise vs group mix dots, and the occupancy over time lines. They’ll be connected, so clicking a space or a dot lights up the same visits in every chart. I want this because a lot of the pattern between noise and groups comes from differences between spaces. If one space is highlighted in every chart, you can check if the pattern shows up inside that space too. Without the link, you’d have to match the colors by eye.

What I’m leaving out is I won’t put all six of my exploring charts on one panel. The head count vs occupancy chart was for checking my data, and the first noise chart was only an early try and neither one answers a question. Two or three charts that each have a job will be easier to read than six that just sit next to each other.



## Task 6: Iterate and refine




## Task 7: Current design 








