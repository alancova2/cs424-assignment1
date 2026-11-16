# Evaluation protocol

## How a session works

Each session is a 10 minute video call. The person shares their screen and opens the page from a link I send. I read each question out loud, they answer out loud, and I time them with a stopwatch. Before every question I reload the page so the sliders go back to 1 and 1. Each person gets up to two minutes per question.
For each version I ask a practice question that doesn't count, then Task 1, then Task 2. After each version I ask for a difficulty rating from 1 (very easy) to 5 (very hard). At the end I ask what was helpful or confusing.

## Questions

Each task has an A and a B version with different limits, so nobody gets the same question twice. Set A is Task 1A and 2A, and Set B is Task 1B and 2B. I checked the answers against processed_data/observations_clean.csv.

| Task | Version | Question | Answer |
|---|---|---|---|
| 1 | A | Noise limit is 3. When the crowd limit goes from 3 to 4, which space gains the most good bet visits? | Daley 4th Floor (+4) |
| 1 | B | Noise limit is 3. When the crowd limit goes from 2 to 3, which space gains the most good bet visits? | Student Center Lounge (+3) |
| 2 | A | Noise limit 3, crowd limit 4. How many spaces have at least 4 good bet visits out of 6? | 4 |
| 2 | B | Noise limit 3, crowd limit 3. How many spaces have at least 4 good bet visits out of 6? | 2 |

## Groups

Everyone does both versions, I switch the order. I'm aiming for 12 people, 3 per group, and I give out groups in order.

| Group | First | Second |
|---|---|---|
| G1 | Static, Set A | Interactive, Set B |
| G2 | Static, Set B | Interactive, Set A |
| G3 | Interactive, Set A | Static, Set B |
| G4 | Interactive, Set B | Static, Set A |

## Scoring

An answer is right (1) or wrong (0), and if they change their mind the last answer counts. Time is the seconds from the end of the question to their final answer. The limit is 120 seconds. If they hit it, I mark it wrong, record 120, and set timed_out to 1.
