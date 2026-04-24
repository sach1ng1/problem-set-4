'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def barplot_fta (pred_universe):
    sns.barplot(data=pred_universe, x="fta")
    plt.savefig("./data/part3_plots/fta_barplot.png", bbox_inches="tight")
    


# 2. Hue the previous barplot by sex
def barplot_fta_by_sex(pred_universe):
    sns.barplot(data=pred_universe, x="fta", hue="sex")
    plt.savefig("./data/part3_plots/fta_barplot_by_sex.png", bbox_inches="tight")


# 3. Plot a histogram of age_at_arrest
def histplot_age(pred_universe):
    sns.histplot(data=pred_universe,x="age_at_arrest", bins=10)
    plt.savefig("./data/part3_plots/histplot_age_arrest.png")

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def histplot_age_bins(pred_universe):
    sns.histplot(data=pred_universe, x="age_at_arrest", bins=[18,21,30,40,100])
    plt.savefig("./data/part3_plots/histplot_age_arrest_bins.png")