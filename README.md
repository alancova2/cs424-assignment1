# cs424-assignment1

## Task 1: Observation and data collection plan

**What I want to observe and why it's interesting.**
I want to observe how students use different study spaces on campus and how that use changes across places, days and times of days. For me personally when I have to study I usually have to guess where to go. Will the library be packed? Is the quiet floor really quiet? Will the lounge be too loud to focus? I never know for sure. In the library the wall signs say "quiet zone" and "collaborative zone" but that doesn't tell me if people actually follow those policies. I decided to visit the same spaces over and over and write down how full, how loud, and how social each one was. That way I could figure out which spaces I can count on at different times. I picked spaces that are different from each other such as, two floors from the library, a lounge in the student center, a lounge in the CS building, and the office hour area. This lets me compare places as well as times of day.

**Initial domain questions**

How does occupancy change across the day and the week in each space? Do some spaces fill up at predictable times while others stay quiet?

Do spaces follow their posted policy? is a quiet zone actually quieter than a collaborative zone, and what about spaces with no rule?

Is noise mostly explained by how many people are in a space, or do some spaces stay quiet or loud no matter how crowded they are?

How does the mix of people working alone compared to in groups change across spaces and time, and does it relate to how loud the space is?

** Data collection plan**

I plan to collect my data by visiting 5 study spaces and writing down what each one is like at that moment. One observation will be one visit of about 5 minutes to one space. At each visit I will record how full the space is, how loud it is, and whether people are mostly alone or in groups. I will estimate how many people are there and write a some notes about what I see and hear. For every visit I will note the building, the exact space, and the posted rule whether a quiet zone, collaborative zone, or no posted rule. The spaces I chose were based off my life as a student. Most of my classes are in the CS building, and I want to find good places there to study, so the places I will look at is the lounge, and the office hour area. I usually study in the library during my 1 hour break, the 2nd floor of the library is full and loud, so I go to the 4th floor, which I find to be full also but it's much quieter. I'm adding the Student Center lounge to see if there is a good place to study near the food area. I also want a mix of space types and posted rules so I can compare them.

I will collect data on a few different days and  go whenever I have a break between classes. I don't have class on Fridays so I plan to collect in the morning that day. What I'm going to do every time is look around, rate the space, estimate the head count, and write some notes of what I see. I think I'll have a couple weak spots since it's a few days out of the week, and I will only visit during the day so I'll miss evenings and weekends. I picked spaces I already know so there could be better spots I am not aware of. My ratings and head counts will be my own estimates. Since my schedule decides when I go some spaces I visit could be at different times than others.

| Attribute | Type | Description | Example |
|---|---|---|---|
| obs_id | Identifier | Unique number for each observation | 12 |
| building | Categorical | Building the space is in | Library |
| location | Categorical | Space observed | Daley 2nd Floor |
| space_type | Categorical | Kind of space: Library, Lounge, or Office Hour Area | Library |
| posted_policy | Categorical | Rule posted in the space: Quiet Zone, Collaborative zone, or No posted rule | Quiet Zone |
| date | Temporal | Date of observation (YYYY-MM-DD) | 2026-10-01 |
| day_of_week | Ordinal | Day of the week | Thursday | 
| time | Temporal | Start time of observation | 1:05PM |
| occupancy_level | Ordinal | How full the space was, from 1 (mostly empty) to 5 (completely full) | 4 |
| noise_level | Ordinal | How loud the space was, from 1 (silent apart from typing), to 5 (very loud) | 2 |
| group_solo | Ordinal | Mix of people working alone or in groups, from 1 (everyone is solo) to 5 (mostly groups) | 3 |
| head_count_min | Quantitative | Lowest estimate of people present | 150 |
| head_count_max | Quantitative | Highest estimate of people present | 170 |
| minutes_to_record | Quantitative | Minutes spent observing | 5 |
| occupancy_notes | Text | My wording for the occupancy rating | Mostly full, couple of seats empty |
| noise_note | Text | My wording for noise rating | Can hear people talking, not yelling | 
| group_solo_notes | Text | My wording for solo/group rating | Most people are in groups |

## Task 2: Pilot and data collection

In my pilot collection the easy attributes to record were posted policy, space type, time, and noise level. Occupancy level, head count, and the solo versus group mix were harder, because I had to walk around and estimate. If I had teammates, I think they would have come up with different numbers for those, since they were my own estimates. I didn't feel any important attribute was missing, a unnecessary attribute would be the minutes to record. The pilot didn't change which questions I thought I could answer. It did help me plan how much data to collect. For the full dataset I recorded 30 observations of about five minutes each at five spaces, the 2nd and 4th floors of the library, the Student Center lounge, the CS building lounge, and the CS building office hour area. I went on Tuesday, September 29, Thursday, October 1, and Friday, October 2, going whenever I had a break and on Friday morning. After I collected my data I made a few changes. I turned my written descriptions of occupancy, noise, and the people mix into 1 to 5 scores and kept my original wording in notes columns. I turned my head counts into min and max estimates.

## Task 3: Data descriptions and domain questions

My dataset has 30 observations from five study spaces, the 2nd and 4th floors of the library, the Student Center lounge, the CS building lounge, and the CS building office hour area. I collected data in rounds I visited all five spaces within about an hour, three rounds on Tuesday, two on Thursday, and one on Friday morning. Each observation has the space, its type and posted rule, the date and time, 1 to 5 ratings for occupancy, noise, and the solo versus group mix, a head count range, and my original notes. The spaces changed a lot, from nearly empty the office hour area, with 5 to 20 people to full the library floors, with 100 to 200. For time/dates I saw only three days, nothing in the evening, and Friday has just one round. The limits are that every rating and count is my own estimate, and that each posted rule belongs to just one space. The quiet zone is only the library's 4th floor and the collaborative zone is only the 2nd floor, so I can't separate the effect of the rule from the effect of the space. Occupancy, head count, and the solo versus group mix were also the hardest to record. Turning a visit into a row meant I had to squeeze a lot into a few numbers. My attributes captured how full, how loud, and how social each space was, but they lost the kind of noise, how long people stayed, and how many seats the space had. I kept my written notes to preserve some detail but the 1 to 5 scores flatten it.

1. How does occupancy change across the day in each space? The library floors were busiest around midday on Tuesday and dropped by late afternoon, while the office hour area stayed mostly empty. This uses date, time, location, and occupancy level. I changed this from "day and week" to "across the day," because three days isn't enough to say much about the week.

2. Do spaces follow their posted policy? In the library they did, the 4th floor (quiet zone) had a noise level of 1 every time, while the 2nd floor (collaborative zone) was a 3 to 5. I can't tell whether the rule or the space causes this, since each rule belongs to one space. This uses posted policy, location, and noise level.

3. Is noise explained by how many people are there? No not quite the quiet 4th floor had 120 to 200 people but a noise level of 1, while the CS lounge with about 15 to 25 people was a 2 or 3. This compares the head count and the occupancy against noise level by space.

4. How does the solo versus group mix relate to noise? Spaces with more groups were louder, and my two ratings moved together closely. Since the differences are mostly between spaces and not between visits this can say more about the type of space than about group work itself. It uses the people rating, noise level, location, and time.

## Task 4: Task abstractions

1. How does occupancy change across the day in each space? The action is to compare, and the target is trends in occupancy over time one for each space. Someone using the visualization needs to see when each space peaks or drops off and how those shapes differ between spaces, so they are comparing trends, not reading single values. Because I only have a few visits per day it is also partly about finding the extremes meaning the busiest and emptiest times.

2. Do spaces follow their posted policy? The action is to compare, and the target is the distribution of noise levels across categories of posted policy and across spaces. It is also a verification task since I'm checking an expectation where a quiet zone should be quiet against what I observed. The person also needs to spot outliers, like a visit that was louder than its rule suggests. I treated this as comparing groups not looking at time because the question is about the rule not about when I visited.

3. Is noise explained by how many people are there? The action is to discover, and the target is the relationship correlation between head count or occupancy and noise level. Someone needs to see whether noise goes up as crowding goes up and which spaces break the pattern, so spotting outliers and groups of similar visits matters too. This is how two attributes depend on each other.

4. How does the solo versus group mix relate to noise? The action is again to discover, and the target is the relationship between the people rating and noise level. It differs from question 3 because the person also needs to tell whether the pattern comes from differences between spaces or from changes within a space over time so they are comparing groupings as well as relating two attributes.

Writing these showed me that questions 3 and 4 are the same kind of task, finding a relationship between two attributes with different attributes plugged in. Question 1 is about time, and question 2 is about comparing categories. I also noticed that my questions asked two things at once, what the pattern is and whether something explains it. A visualization can show the pattern, but my data can't prove an explanation especially with 30 observations and ratings I estimated myself. That made me more careful about what I expect a visualization to show.

## Task 5: Visualization sketches

## Task 6: Summary

## Task 7: Collaboration process



