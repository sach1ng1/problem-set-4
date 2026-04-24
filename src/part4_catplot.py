'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def catplot_felony(felony_charge_pred_universe):
    sns.catplot(data=felony_charge_pred_universe, x="has_felony_charge", y="prediction_felony", kind="bar")
    plt.savefig("./data/part4_plots/catplot_felony.png")
# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
def catplot_non_felony(felony_charge_pred_universe):
    sns.catplot(data=felony_charge_pred_universe, x="has_felony_charge", y="prediction_nonfelony", kind="bar")
    plt.savefig("./data/part4_plots/catplot_nonfelony.png")

# In a print statement, answer the following question: What might explain the difference between the plots?
    print("Well it seems that it for the first bar plot there is a higher prediction for felony rearrest whereas for non-rearrest plot it seems to be not as high a prediction for non felony rearrest as there is in comparison to felony re-arrest. Therefore it seems based on the results of the prediction we can see that a felony rearrest is more likely than nonfelony-rearrest.")

# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
def catplot_felony_hue(felony_charge_pred_universe):
    sns.catplot(data=felony_charge_pred_universe, x="has_felony_charge", y="prediction_felony", kind="bar", hue="y_felony")
    plt.savefig("./data/part4_plots/catplot_felony_hue.png")
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?
    print("It means that since there was an instance of a felony charge, the prediction is placing more likliehood of being rearrested than someone who did not have a felony charge but later gets rearrested now for a felony charge. I believe that being arrested for a felony charge in the first place has allowed for the precitions to be more probable for future felony rearrests than intial non feloy arrests.")