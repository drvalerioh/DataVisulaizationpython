#!/usr/bin/env python
# coding: utf-8

# # Part II - Prosper Loan Data
# ## by Valerian Lunale Makanga

# 
# 
# 
# ## Investigation Overview
# 
# 
# > From Univariate, Bivariate and Multivariate. Observation 1. the employed are the most listings in ProsperData set and those whose employment status is Full-time.
# 
# the Self-employed and those whose EmployementStatus is Not-available have relatively equal rating.
# 
# Not-employed ,Part-time and Retired are the list available for listings in ProsperData.
# 
# those whose status is 'Other' also have a relatively higher rating as compred to Not-emplyed,Part-time and Retired.
# 
# Observation 2.
# 
# Employment Status is the employment status of the borrower at the time they posted the listings.
# 
# Prosper Ratings are the assigned at the time the listigs were done
# 
# 
# 
# ## Dataset Overview
# 
# From prosperloandata, there binding factors that determine the loan borrowing and the ratings that determine the allocations interms of months in loans.
# 
# However, all the loans from prosper company depend on the loanstatus of Employed since its evident from the explorations that all borrowers from that category are the most preferd for loans in the company.
# 
# most loans in the company are also current loans borrowerd and defaulated loans being the least in the loaning from the company.

# ### Univariate  and Multivariate

# In[67]:


# import all packages and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

# suppress warnings from final output
import warnings
warnings.simplefilter("ignore")


# In[68]:


# load in the dataset into a pandas dataframe
df = pd.read_csv('prosperLoanData.csv')


# > Loads the dataset and describes the next explorations findings.

# In[69]:


data_columns= ['Term','LoanStatus','BorrowerAPR','BorrowerRate','ProsperRating (numeric)','ProsperRating (Alpha)','ListingCategory (numeric)',
              'Occupation','EmploymentStatus', 'TotalInquiries','StatedMonthlyIncome', 'TotalProsperLoans', 'LoanOriginalAmount',
    'LoanOriginationDate','MemberKey', 'Recommendations', 'Investors']


# In[70]:


data_df =df[data_columns]


# ### LOAN STATUS 
# 
# This is the distribution between the main status attributes and the loans status in complted, cancelled,chargedoff and Defaulted.

# In[71]:


#Let's start our exploration by looking at the main variable of interest: loan status:Employment status
plt.title('LoanStatus distribution');
base_color = sb.color_palette()[0]
plt.xticks(rotation=90)
sb.countplot(data = data_df,  y= 'LoanStatus', color = base_color);


# ### StatedMonthly Income ratings against Ratings
# 
# This plotting illustrates the changes and how Rating affects the income distributions.

# In[72]:


#plt.yticks('StatedIncome')
plt.title('StatedMonthlyIncome and Rating');
income_std = data_df['StatedMonthlyIncome'].std()
income_mean = data_df['StatedMonthlyIncome'].mean()
boundary = income_mean + income_std * 3
#len(target_df[target_df['StatedMonthlyIncome'] >= boundary])
plt.hist(data=data_df, x='StatedMonthlyIncome', bins=1000);
plt.xlim(0, boundary);
plt.xlabel('Original loan amount ($)');
plt.ylabel('IncomeCount');


# In[73]:


#from the category of the listings that the borrower selected when posting their listings in Debt Consolidation,Home Improvement, Busines Auto,Other,
categories = { 1: 'Debt Consolidation', 2: 'Home Improvement', 3: 'Business', 6: 'Auto' , 7: 'Other' }
def reduce_categorie(row):
    loan_category = row['ListingCategory (numeric)']
    if  loan_category in categories:
        return categories[loan_category]
    else:
        return categories[7]
    
data_df['ListingCategory (numeric)'] = data_df.apply(reduce_categorie, axis =1)
data_df['ListingCategory (numeric)'].value_counts()


# In[ ]:





# ## (Visualization 1)
# 
# >Explanations.
# 
# Employment status shows the status of the borrowers as at the time they posted the listings.
# 
# Observations:
# 
# the employed are the most listings in ProsperData set and those whose employment status is Full-time.
# 
# the Self-employed and those whose EmployementStatus is Not-available have relatively equal rating.
# 
# Not-employed ,Part-time and Retired are the list available for listings in ProsperData.
# 
# those whose status is 'Other' also have a relatively higher rating as compred to Not-emplyed,Part-time and Retired.
# 
# Explanations:
# 
# in the prosper dataset, the current loans status are the most.
# 
# the completed loans are the second largest section in Prosper.
# 
# all the PastDue loans are the least in the dataset and they are listed according to their days past due with (1-15 days) being the most.
# 
# the cancelled loan status have a nill/0 value count.
# 
# chargedOff loans and Defaulted loans are still a high value of count in the LoansData.
# 
# Observation.
# 
# In general , PropserData loans are completed than at higher rate as compared to Defaulted status.

# In[ ]:





# ## (Visualization 2)
# 
# > Explanations and Observations: in the current the most ProsperRating is C and according to the findings while HR is the list at the time the listing created. in Completed Rating, D is the highest ProsperRating since the loan listing was created. the A ProsperRatings appear relatively higher for the Completed and the Current. In the Loanstatus, the current borrowed loans have the highest ProsperRating in all the other ProsperLoanData set.

# ### Term and Ratings Loans co-relations
# 
# this is a plot that defines the factors in loans terms and rating which contribute to the general loans borrowings.

# In[74]:


plt.title('Term and Rating');
plt.xticks(rotation=90)
sb.countplot(data = data_df, x = 'LoanStatus', hue = 'ProsperRating (Alpha)', palette = 'Blues')


# ### Bivariate

# ## (Visualization 3)
# 
# 

# ### Employment and loans Ratings
# 
# accroding to the prosper, empoyement is a major determinant in the acquisition of loans from the company.

# In[75]:


#Employment status and Prosper Rating graphs to compare.
plt.figure(figsize = [12, 10])
plt.title('EmploymentStatus and ProsperRating');
sb.countplot(data = data_df, x = 'ProsperRating (Alpha)', hue = 'EmploymentStatus');


# ### Generate Slideshow
# Once you're ready to generate your slideshow, use the `jupyter nbconvert` command to generate the HTML slide show.  

# In[ ]:


# Use this command if you are running this file in local
get_ipython().system('jupyter nbconvert Part_II_exploration_template.ipynb --to slides --post serve --no-input --no-prompt')


# > In the classroom workspace, the generated HTML slideshow will be placed in the home folder. 
# 
# > In local machines, the command above should open a tab in your web browser where you can scroll through your presentation. Sub-slides can be accessed by pressing 'down' when viewing its parent slide. Make sure you remove all of the quote-formatted guide notes like this one before you finish your presentation! At last, you can stop the Kernel. 

# ### Submission
# If you are using classroom workspace, you can choose from the following two ways of submission:
# 
# 1. **Submit from the workspace**. Make sure you have removed the example project from the /home/workspace directory. You must submit the following files:
#    - Part_I_notebook.ipynb
#    - Part_I_notebook.html or pdf
#    - Part_II_notebook.ipynb
#    - Part_I_slides.html
#    - README.md
#    - dataset (optional)
# 
# 
# 2. **Submit a zip file on the last page of this project lesson**. In this case, open the Jupyter terminal and run the command below to generate a ZIP file. 
# ```bash
# zip -r my_project.zip .
# ```
# The command abobve will ZIP every file present in your /home/workspace directory. Next, you can download the zip to your local, and follow the instructions on the last page of this project lesson.
# 

# In[ ]:


get_ipython().system('jupyter nbconvert Part_II_exploration_template.ipynb --to slides --post serve --no-input --no-prompt')


# In[ ]:




