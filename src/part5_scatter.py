'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
def scatterplot_prediction(felony_charge_pred_universe):
    sns.lmplot(data=felony_charge_pred_universe, x="prediction_felony", y="prediction_nonfelony", hue="has_felony_charge")
    plt.savefig("./data/part5_plots/scatterplot_prediction.png")
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
    print("It seems there is a strong positive correlation between having an intial felony charge where as likelihood for felony rearrest increase so does the likelihood for non felony rearrest.")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
def scatterplot_prediction_rearrest(felony_charge_pred_universe):
    sns.lmplot(data=felony_charge_pred_universe, x="prediction_felony", y="y_felony")
    plt.savefig("./data/part5_plots/scatterplot_prediction_rearrest.png")
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
    print("Based on the plot, the model is not calibrated as the points in the predicted felony rearrests and actual felony arrests do not interact or align around the regression line.")