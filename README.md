# Finding Australia's fastest parkrun
Parkrun is a free, community event where you can walk, jog, run, volunteer or spectate. Parkruns take place weekly in parks across the world. Originating in the UK, Australia's first parkrun took place https://www.parkrun.com.au/ in 2011 on the Gold Coast. Currently, there are 463 locations with weekly parkruns, which is an astonishing success to get people moving for a nonprofit organization

Events are timed and results are posted online a couple hours after. With so many events to choose from, it is a natural question to ask if we can find the fastest parkrun, that is, the parkrun with the flattest course without sharp turns, fully on asphalt, solid competition but not overcrowded, and decent weather (no wind, not too hot etc.). Inspired by Tim Grose's analysis of retrieving UK's fastest parkruns https://www.thepowerof10.info/content/itemdisplay.aspx?itemid=1702, we attempt to find Australia's fastest parkruns.

First, one could simply compute the average of all times ever ran at any course and compare. This, however, mainly indicates whether the parkrun is mainly attended by elite runners or by recreational runners. We thus have to find a way to remove the distribution-dependence.

Tim Grose ranks parkruns by their Standard Scratch Score, a term used in golf to compare the difficulty of courses. The 'handicap' between players is the difference between their PBs. Events are scored relative to how far runners perform away from their best times.

Rather than considering the times of all parkruns ever ran, we only consider personal bests recorded per age-group and event, and try to find the parkrun where participants have ran on average the time closest to their PB. 

This solves two problems at once: it is difficult to retrieve this mass of data, and not every runner gives an all-out effort at every event.

The code is organized as follows:
- 01_scrape: scrape data from parkrun.com.au. This code takes a while to run (~10-12 hours) since there is data to pull across more than 8000 webpages. On every page we find the PBs of runners to have ever recorded a PB in a particular agegroup at a particular parkrun. One does not have to rerun this notebook, since the processed and cleaned data is already stored on Github.
- 02_process: combine all individual parkruns into a single dataframe
- 03_clean: remove participants with shared name and gender if the maximum age between datapoints exceeds the time that parkrun has existed for (certainly not the same person so could be very different PB adding noise to the data) and parkruns with less than 100 PBs, which is too few for reliable statistics
- 04_analyze: analyze methods on how to best rank parkruns
- 05_visualize_distributions: visualize data grouped per parkrun across a few dimensions
- 06_rank_parkruns: a widget to choose parameters to find the fastest parkrun in a state

TODO: deploy notebooks 05_visualize_distributions / 06_rank_parkruns using the free MyBinder.