# Task 1

I picked my “good bet for a quiet seat” chart because the answer depends on where you draw the line. A visit counts as a good bet when its noise and crowd scores are under your limits. The quiet floor of the library had 2 good visits with a crowd limit of 3, but 6 with a limit of 4. Both versions use the same data and the same dot charts. There’s one small chart for each space, a dot for every visit, and bigger dots mean more people were there.

In the interactive version you move two sliders to set the most noise and the most crowding you’ll put up with. A green box moves across the dot charts, the dots inside it turn green, and a bar chart shows how many good visits each space has. I picked this interaction because it lets you filter the visits. I left out hover boxes since they would only repeat what’s already on the screen. The static version can’t change the limits, I put the answers on the page ahead of time. It has the same dot charts without the box, plus nine small bar charts for noise limits of 1 to 3 and crowd limits of 2 to 4, with the counts written on the bars. Every question in my study can be answered from the page, so I didn’t make this version weaker on purpose.

I think the sliders will help most with questions that compare limits like which space gains the most good visits when the crowd limit goes up. With sliders, you watch the bars change. With the static page, you have to find two charts and compare them by eye. I’m not sure which will be faster and the study will help me find out.

### Graphs 
[study_static.py](code/study_static.py),  [study_interactive.py](code/study_interactive.py), [study_common.py](code/study_common.py) 
