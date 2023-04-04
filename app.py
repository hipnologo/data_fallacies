import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

# Handling Streamlit 
st.set_option('deprecation.showPyplotGlobalUse', False)

# Set the page title
st.set_page_config(page_title='Data Fallacies Demonstration')

np.random.seed(123)  # For reproducibility

# Create a DataFrame with 100 students and their grades in three subjects
df = pd.DataFrame({
    'StudentID': range(1, 101),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Math': np.random.randint(60, 101, 100),
    'Science': np.random.randint(60, 101, 100),
    'English': np.random.randint(60, 101, 100)
})

# Define the list of data fallacies
fallacies = [
    'Cherry Picking',
    'Cobra Effect',
    'Sampling Bias',
    'Regression Towards the Mean',
    'Overfitting',
    'Data Dredging',
    'False Causality',
    'Gambler’s Fallacy',
    'Simpson’s Paradox',
    'Publication Bias',
    'Survivorship Bias',
    'Gerrymandering',
    'Hawthorne Effect',
    'McNamara Fallacy',
    'Danger of Summary Metrics'
]        

# Create the Streamlit app
def main():
    st.title('Data Fallacies')
    st.write('Select a data fallacy from the dropdown menu to see a demonstration.')

    # Add a dropdown menu for selecting the fallacy
    selected_fallacy = st.selectbox('Select a fallacy', fallacies)

    # Generate a plot demonstrating the selected fallacy
    if selected_fallacy == 'Cherry Picking':
        st.subheader('Cherry Picking')
        # Select the top 10 students in Math and plot their grades in Science
        top_students = df.nlargest(10, 'Math')
        sns.scatterplot(data=top_students, x='Math', y='Science')
        st.pyplot()
        st.write('The above plot demonstrates the fallacy of cherry picking. The top 10 students in Math are selected and their grades in Science are plotted, while ignoring the grades of other students.')
    elif selected_fallacy == 'Cobra Effect':
        st.subheader('Cobra Effect')
        # Plot the number of rats killed by people over time
        rats_killed = [100, 120, 140, 160, 180, 200, 220, 240, 260, 280]
        incentives = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        sns.lineplot(x=incentives, y=rats_killed)
        st.pyplot()
        st.write('The above plot demonstrates the fallacy of the Cobra Effect. In this scenario, an incentive was provided to people to kill rats, but it led to an increase in the number of rats instead.')
    elif selected_fallacy == 'Sampling Bias':
        st.subheader('Sampling Bias')
        # Collect data only from students who scored above 80 in Math and plot their grades in Science
        biased_sample = df[df['Math'] > 80]
        sns.scatterplot(data=biased_sample, x='Math', y='Science')
        st.pyplot()
        st.write('The above plot demonstrates the fallacy of sampling bias. Only students who scored above 80 in Math are selected and their grades in Science are plotted, leading to a biased conclusion.')
    elif selected_fallacy == 'Regression Towards the Mean': 
        st.subheader('Regression Towards the Mean')
        # Select the top 10 students in Math and plot their grades in the next test
        top_students = df.nlargest(10, 'Math')
        next_test = top_students.apply(lambda x: np.random.normal(x.mean(), 10), axis=1)
        sns.scatterplot(x=top_students['Math'], y=next_test)
        st.pyplot()
        st.write('The above plot demonstrates the regression towards the mean fallacy. It shows the grades of top 10 students in Math plotted against their grades in the next test, where the unusually high grades in the first test are expected to be closer to the average in the next test.')
    elif selected_fallacy == 'Overfitting':
        st.subheader('Overfitting')
        # Fit a curve to the Math grades and plot it
        sns.regplot(data=df, x='StudentID', y='Math', order=10)
        st.pyplot()
        st.write('The above plot demonstrates the overfitting fallacy. A curve is fit to the Math grades, which is too complex and highly tailored to the data, instead of representing the general trend.')
    elif selected_fallacy == 'Data Dredging':
        st.subheader('Data Dredging')
        # Collect data on the correlation between Math grades and random variables and plot only significant correlations
        p_values = []
        for i in range(1000):
            rand_var = np.random.randint(1, 101, 100)
            _, p_value = stats.pearsonr(df['Math'], rand_var)
            p_values.append(p_value)
        df_p = pd.DataFrame({'RandomVar': np.random.randint(1, 101, 1000), 'PValue': p_values})
        significant_p_values = df_p[df_p['PValue'] < 0.05]
        sns.scatterplot(data=significant_p_values, x='RandomVar', y='PValue')
        st.pyplot()
        st.write('The above plot demonstrates the data dredging fallacy. Multiple hypotheses are tested on the correlation between Math grades and different random variables, and only significant correlations are plotted, which are the result of chance.')
    elif selected_fallacy == 'False Causality':
        st.subheader('False Causality')
        # Plot the number of books read by students and their Math grades
        num_books = np.random.randint(0, 11, 100)
        math_grades = df['Math']
        sns.scatterplot(x=num_books, y=math_grades)
        st.pyplot()
        st.write('The above plot demonstrates the false causality fallacy. It shows the Math grades of students plotted against the number of books they read, leading to a conclusion that reading more books causes higher grades, which is not necessarily true.')
    elif selected_fallacy == 'Gambler’s Fallacy':
        st.subheader('Gambler’s Fallacy')
        # Flip a coin 100 times and plot the frequency of heads and tails over time
        flips = np.random.choice(['Heads', 'Tails'], 100)
        freqs = []
        for i in range(len(flips)):
            freqs.append((flips[:i+1] == 'Heads').sum() / (i+1))
        sns.lineplot(x=range(1, 101), y=freqs)
        st.pyplot()
        st.write('The above plot demonstrates the gambler’s fallacy. It shows the frequency of heads and tails over time in 100 coin flips, leading to the conclusion that the outcome of a flip is dependent on previous flips, which is not true.')
    elif selected_fallacy == 'Simpson’s Paradox':
        st.subheader('Simpson’s Paradox')
        # Plot the average Math and Science grades for male and female students, and then for the entire population
        male_avg = df[df['Gender'] == 'Male'][['Math', 'Science']].mean()
        female_avg = df[df['Gender'] == 'Female'][['Math', 'Science']].mean()
        all_avg = df[['Math', 'Science']].mean()
        averages = pd.DataFrame({'Male': male_avg, 'Female': female_avg, 'All': all_avg})
        sns.barplot(data=averages)
        st.pyplot()
        st.write('The above plot demonstrates Simpson’s paradox. It shows the average Math and Science grades for male and female students and then for the entire population, leading to a conclusion that the overall population has a different trend than the subgroups, which is misleading.')
    elif selected_fallacy == 'Publication Bias':
        st.subheader('Publication Bias')
        # Collect data on the effectiveness of a drug and plot the number of published studies vs. the effect size
        effect_sizes = np.random.normal(1.0, 0.5, 100)
        num_studies = np.random.poisson(10, 100)
        df_p = pd.DataFrame({'EffectSize': effect_sizes, 'NumStudies': num_studies})
        sns.scatterplot(data=df_p, x='EffectSize', y='NumStudies')
        st.pyplot()
        st.write('The above plot demonstrates the publication bias fallacy. It shows the number of published studies plotted against the effect size of a drug, leading to a conclusion that the drug has a stronger effect than it actually does, due to studies with small effect sizes being less likely to be published.')
    elif selected_fallacy == 'Survivorship Bias':
        st.subheader('Survivorship Bias')
        # Plot the height and weight of people who have survived a plane crash
        heights = np.random.normal(170, 10, 50)
        weights = np.random.normal(70, 10, 50)
        survived = np.random.choice([0, 1], 50, p=[0.2, 0.8])
        df_s = pd.DataFrame({'Height': heights, 'Weight': weights, 'Survived': survived})
        df_survived = df_s[df_s['Survived'] == 1]
        sns.scatterplot(data=df_survived, x='Height', y='Weight')
        st.pyplot()
        st.write('The above plot demonstrates the survivorship bias fallacy. It shows the height and weight of people who survived a plane crash, leading to a conclusion that the survivors have a different height and weight distribution than the entire population, which is misleading.')
    elif selected_fallacy == 'Gerrymandering':
        st.subheader('Gerrymandering')
        # Create a scatterplot of voter turnout vs. party affiliation, and then manipulate the data to favor one party
        voter_turnout = np.random.normal(0.5, 0.1, 100)
        party_affiliation = np.random.choice(['Republican', 'Democrat'], 100, p=[0.4, 0.6])
        df_g = pd.DataFrame({'VoterTurnout': voter_turnout, 'Party': party_affiliation})
        df_rep = df_g[df_g['Party'] == 'Republican']
        df_dem = df_g[df_g['Party'] == 'Democrat']
        df_dem['VoterTurnout'] += 0.1
        df_combined = pd.concat([df_rep, df_dem])
        sns.scatterplot(data=df_combined, x='VoterTurnout', y='Party')
        st.pyplot()
        st.write('The above plot demonstrates the gerrymandering fallacy. It shows the voter turnout and party affiliation plotted together and then manipulated to favor one party, leading to a conclusion that the party has more support than it actually does.')
    elif selected_fallacy == 'Hawthorne Effect':
        st.subheader('Hawthorne Effect')
        # Plot the effect of a new teaching method on student grades
        grades_old_method = np.random.normal(70, 5, 100)
        grades_new_method = np.random.normal(75, 5, 100)
        df_h = pd.DataFrame({'OldMethod': grades_old_method, 'NewMethod': grades_new_method})
        sns.boxplot(data=df_h)
        st.pyplot()
        st.write('The above plot demonstrates the Hawthorne effect fallacy. It shows the effect of a new teaching method on student grades, leading to a conclusion that the new method is more effective, without controlling for other variables.')
    elif selected_fallacy == 'McNamara Fallacy':
        st.subheader('McNamara Fallacy')
        # Plot the number of new customers and the number of customer complaints over time
        num_customers = np.random.poisson(100, 10)
        num_complaints = np.random.poisson(5, 10)
        df_m = pd.DataFrame({'NewCustomers': num_customers, 'Complaints': num_complaints})
        sns.lineplot(data=df_m)
        st.pyplot()
        st.write('The above plot demonstrates the McNamara fallacy. It shows the number of new customers and customer complaints plotted over time, leading to a conclusion that the company is improving, without considering other factors.')
    elif selected_fallacy == 'Danger of Summary Metrics':
        st.subheader('Danger of Summary Metrics')
        # Plot the Math grades of all students, and then plot the grades of the top 10% separately
        top_10 = df.nlargest(int(len(df) * 0.1), 'Math')
        sns.histplot(df, x='Math')
        sns.histplot(top_10, x='Math', color='red')
        st.pyplot()
        st.write('The above plot demonstrates the danger of summary metrics. It shows the distribution of Math grades of all students and then of the top 10%, leading to a conclusion that the top 10% has significantly higher grades, without considering the full context of the data. This can be misleading, as it ignores the fact that the rest of the students may also have high grades, and the top 10% may not be representative of the overall population. It is important to analyze the full dataset and consider the context in order to avoid the danger of summary metrics.')

if __name__ == '__main__':
    main()