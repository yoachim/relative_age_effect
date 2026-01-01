
setting up environ:

conda create --channel conda-forge --name rae python=3.13
conda install numpy astropy matplotlib notebook requests bs4 pandas selenium




Looks like https://www.sports-reference.com/ has a lot of the data that I want. Looks like they let folks scrape as long as they stay below 10 requests per minute. So, 10s wait is plenty.

example url for baseball:
https://www.baseball-reference.com/leagues/majors/1938-births.shtml#all_misc_batting
https://www.baseball-reference.com/leagues/majors/1938-births.shtml#all_misc_pitching

Looks like baseball is all MLB players

Basketball is NBA and ABA grouped, and then also WNBA

