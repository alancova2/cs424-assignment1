# cs424-assignment1

## Task 1: Observation and data collection plan

**What I want to observe and why it's interesting.**
I want to observe how students use different study spaces on campus and how that use changes across places, days and times of days. For me personally when I have to study I usually have to guess where to go. Will the library be packed? Is the quiet floor really quiet? Will the lounge be too loud to focus? I never know for sure. In the library the wall signs say "quiet zone" and "collaborative zone" but that doesn't tell me if people actually follow those policies. I decided to visit the same spaces over and over and write down how full, how loud, and how social each one was. That way I could figure out which spaces I can count on at different times. I picked spaces that are different from each other such as, two floors from the library, a lounge in the student center, a lounge in the CS building, and the office hour area. This lets me compare places as well as times of day.

**Initial domain questions**

How does occupancy change across the day and the week in each space? Do some spaces fill up at predictable times while others stay quiet?

Do spaces follow their posted policy? is a quiet zone actually quieter than a collaborative zone, and what about spaces with no rule?

Is noise mostly explained by how many people are in a space, or do some spaces stay quiet or loud no matter how crowded they are?

How does the mix of people working alone compared to in groups change across spaces and time, and does it relate to how loud the space is?

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


