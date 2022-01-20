#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import statistics
import calendar

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 22}

def process_dataframe(filepath):
    DF = pd.read_csv(filepath)
    DF['date'] = pd.to_datetime(DF['date'])
    DF = DF.set_index("date")
    return(DF)


def main():
    
    
    plt.rc('font', **font)
    color_palette_list = ['#5cb85c', '#ffcc9a', '#5bc0de']

    #Figure 01
    
    users_raw = process_dataframe("../dataframes/users_usegalaxyeu.csv")
    
    plt.figure(1,figsize=(16, 10), dpi=300)
    ax1 = plt.gca()
    
    users_raw.plot(kind='line',
            #y='2020',
            ax=ax1,
            use_index=True,
            linewidth=2,
    )
    
    ax1.get_legend().remove()
    plt.title("Number of new users in usegalaxy.eu from 2013 to 2022\n")
    ax1.set_xlabel('\nYear')
    ax1.set_ylabel('Registered users\n')
    plt.tight_layout()
    plt.savefig('../plots/users_galaxyeu.png')

    #Figure 02
    
    
    plt.figure(2,figsize=(16, 10), dpi=300)
    ax2 = plt.gca()
    
    users_raw.plot(kind='bar',
            y='2021',
            ax=ax2,
            use_index=True,
            linewidth=2,
    )
    ax2.set_xticklabels(months)
    ax2.set_xlabel('Month\n')
    ax2.set_ylabel('Registered users\n')
    ax2.get_legend().remove()
    plt.title("Number of new users in usegalaxy.eu in 2021\n")
    plt.tight_layout()
    plt.savefig('../plots/users_galaxyeu_2021.png')



    #Figure 03

    users_total = process_dataframe("../dataframes/users_usegalaxy_accumulative.csv")
    
    plt.figure(3,figsize=(16, 10), dpi=300)
    ax3 = plt.gca()
    
    users_total.plot(kind='line',
            #y='2021',
            ax=ax3,
            use_index=True,
            linewidth=2,
    )
    ax3.get_legend().remove()
    plt.title("Accumulative number of new users in usegalaxy.eu from 2013 to 2022\n")
    ax3.set_xlabel('\nYear')
    ax3.set_ylabel('Registered users\n')
    plt.tight_layout()
    plt.savefig('../plots/total_users_galaxyeu.png')

    
"""

    #Figure 02

    plt.figure(2,figsize=(16, 10), dpi=300)
    ax2 = plt.gca()
    
    visits_two_months.plot(kind='line',
            y='2021',
            ax=ax2,
            use_index=True,
            linewidth=2,
    )
    ax2.get_legend().remove()
    plt.title("Visits last two months")
    plt.savefig('../plots/visits_two_months.png') 

    #Figure 03

    plt.figure(3,figsize=(16, 10), dpi=300)
    ax3 = plt.gca()
    
    visits_raw.plot(kind='line',
            y='Differences',
            ax=ax3,
            use_index=True,
            linewidth=2,
    )
    ax3.get_legend().remove()
    plt.title("Differences in the number of visits between 2021 and 2020")
    plt.savefig('../plots/differences.png') 

    #Figure 04

    plt.figure(4,figsize=(16, 10), dpi=300)
    ax4 = plt.gca()


                          
    visits_median.plot(kind='bar',
            x="Months",
            ax=ax4,
            color = color_palette_list,
            linewidth=2,
            align='center'
    )
    
    plt.title("Comparison of number of visits to help.galaxyproject.org (median)")
    plt.savefig('../plots/visits_median.png')

    #Figure 05
    
    plt.figure(5,figsize=(16, 10), dpi=300)
    ax5 = plt.gca()
    
    posts_sum.plot(kind='bar',
            x="Months",
            ax=ax5,
            color = color_palette_list,
            linewidth=2,
            align='center'
    )
    
    plt.title("Comparison of total number of new posts in posts help.galaxyproject.org")
    plt.savefig('../plots/posts_sum.png') 
    
    
    #Figure 06
    
    plt.figure(6,figsize=(16, 10), dpi=300)
    ax6 = plt.gca()
    
    posts_sum.plot(kind='box',
                   ax=ax6,
                   whiskerprops=dict(linewidth=2,color="black"),
                   boxprops = dict(linewidth=2,color="black"),
                   medianprops = dict(linewidth=2,color="black"),
                   capprops = dict(linewidth=2),
                   showfliers=False)
    
    plt.title("Comparison of number of new posts in posts help.galaxyproject.org")
    plt.savefig('../plots/posts_box.png') 
    
    #Figure 07

    plt.figure(7,figsize=(16, 10), dpi=300)
    ax7 = plt.gca()

    visits_edited = visits_raw.drop(columns=["Differences"])
    
    visits_edited.plot(kind='box',
                       ax=ax7,
                       whiskerprops=dict(linewidth=2,color="black"),
                       boxprops = dict(linewidth=2,color="black"),
                       medianprops = dict(linewidth=2,color="black"),
                       capprops = dict(linewidth=2),
                       showfliers=False)
    
    plt.title("Comparison of number of visits to help.galaxyproject.org")
    plt.savefig('../plots/visits_box.png') 
    
"""
if __name__ == "__main__":
    main()
