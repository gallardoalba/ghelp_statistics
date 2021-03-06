#!/usr/bin/python3

import pandas as pd
import calendar


def process_visits(total,crawler):
    crawler_raw = open(crawler).readlines()[1:]
    total_raw = open(total).readlines()[1:]
    dates = []; visits = []; visits_dictionary = {}
    for i in range(len(crawler_raw)):
        date,visits_crawler = crawler_raw[i].split(",")
        visits_total = total_raw[i].split(",")[-1]
        dates.append(date)
        visits_day = int(visits_total.strip()) - int(visits_crawler.strip())
        visits.append(visits_day)
        visits_dictionary[date] = visits_day 
    return(dates,visits,visits_dictionary)

def process_posts(posts_file):

    posts_raw = open(posts_file).readlines()[1:]
    posts = []; posts_dictionary={}
    for i in range(len(posts_raw)):
        date, post = posts_raw[i].split(",")
        posts.append(int(post.strip()))
        posts_dictionary[date] = int(post.strip())
    return(posts,posts_dictionary)

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 18}

def main():
    c21,t21 = "../raw_data/2021_crawler_view.csv","../raw_data/2021_total_view.csv"
    c20,t20 = "../raw_data/2020_crawler_view.csv","../raw_data/2020_total_view.csv"    
    c19,t19 = "../raw_data/2019_crawler_view.csv","../raw_data/2019_total_view.csv"
    c19,t19 = "../raw_data/2019_crawler_view.csv","../raw_data/2019_total_view.csv"
    c19,t19 = "../raw_data/2019_crawler_view.csv","../raw_data/2019_total_view.csv"
    dates_2021,visits_2021,db_2021 = process_visits(t21,c21)
    dates_2020,visits_2020,db_2020 = process_visits(t20,c20)
    dates_2019,visits_2019,db_2019 = process_visits(t19,c19)
    size = len(visits_2021)
    diff = [visits_2021[i] - visits_2020[i] for i in range(size)]

    posts_2019, pdb_2019 = process_posts("../raw_data/2019_posts.csv")
    posts_2020, pdb_2020 = process_posts("../raw_data/2020_posts.csv")
    posts_2021, pdb_2021 = process_posts("../raw_data/2021_posts.csv")
    dates_plot = pd.to_datetime(dates_2021)
    

    # Visits dataframe
    
    DF = pd.DataFrame()
    DF['Dates'] = dates_plot
    DF['2019'] = visits_2019
    DF['2020'] = visits_2020
    DF['2021'] = visits_2021
    DF = DF.set_index('Dates')

    
    # Visits montly dataframe
    
    GB=DF.groupby([(DF.index.month)]).median()
    months = []
    for idx in GB.index: months.append(calendar.month_name[idx])
    GB['Months'] = months
    GB.to_csv("../dataframes/DF_visits_median.csv")

    
    DF['Differences'] = diff
    DF.to_csv("../dataframes/DF_visits.csv")

    
    # Post dataframe
    
    PF = pd.DataFrame()

    PF['Dates'] = dates_plot
    
    PF['2019'] = posts_2019
    PF['2020'] = posts_2020
    PF['2021'] = posts_2021
    
    PF = PF.set_index('Dates')
    PF.to_csv("../dataframes/DF_posts.csv")
    
    PFM=PF.groupby([(PF.index.month)]).sum()
    months = []
    for idx in PFM.index: months.append(calendar.month_name[idx])
    PFM['Months'] = months
    PFM.to_csv("../dataframes/DF_posts_sum.csv")
    
    
if __name__ == "__main__":
    main()
