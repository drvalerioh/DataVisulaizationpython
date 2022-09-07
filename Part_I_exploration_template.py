#!/usr/bin/env python
# coding: utf-8

# # Part I - Prosper Loan Data
# ## by (Valerian Lunale Makanga)
# 
# ## Introduction
# > This dataset contains number of loans in loans amounts, borrower rate /interest rate, current loan status, and borrower income.
# 
# >From the loans borrowerd, all are determined from different ratings ,terms of paymenst and status of specific LoanAmounts.
# 
# >However, their different listings which are associated with the loans for qualified applicants and categories.
# 
# 
# 
# ## Preliminary Wrangling
# 

# In[2]:


# import all packages and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')


# Data Wrangling process to access the data and deduce only neccesary data for exploration of the dataset.

# > Load in your dataset and describe its properties through the questions below. Try and motivate your exploration goals through this section.
# 

# In[3]:


df =pd.read_csv('prosperLoanData.csv')


# In[4]:


df.head()


# In[5]:


df.info()


# #Describe the dataset this enables the overview of the data.

# In[6]:


df.describe()


# due to the exploration process , i'll need to get specific columns/variables which may only be usefull to analyse through the dataset.
# assess the new dataset before exploration.

# In[7]:


data_columns= ['Term','LoanStatus','BorrowerAPR','BorrowerRate','ProsperRating (numeric)','ProsperRating (Alpha)','ListingCategory (numeric)',
              'Occupation','EmploymentStatus', 'TotalInquiries','StatedMonthlyIncome', 'TotalProsperLoans', 'LoanOriginalAmount',
    'LoanOriginationDate','MemberKey', 'Recommendations', 'Investors']


# In[8]:


data_df =df[data_columns]


# In[9]:


data_df.head(10)


# In[10]:


data_df.tail()


# In[11]:


data_df.info()


# In[12]:


data_df.describe()


# In[ ]:





# ### What is the structure of your dataset?
# 
# > The dataset of properLoansData contains information/data consisting of a series of records from Prosper Loans records.
# >The dataset consists of loans amounts, borrower rate and current loan status and loans details.
# 
# ### What is/are the main feature(s) of interest in your dataset?
# 
# >Loan status: the current status of the loan, cancelled,chargedOff,Completed,current,Defaulted,FinalPaymentInProgress,PastDue.
# >The PastDue status is accompanied by a deliquency Bucket.
# >ProsperRating :assigned at the time the listing was created and applicable for loans originated after July 2009.
# >BorrowerAPR :during the exploration i would like to check the Borrower's Annual Performance Rating(APR) for the Loan
# >Employement status.
# >StatedMonthlyIncome data in the listings.
# 
# ### What features in the dataset do you think will help support your investigation into your feature(s) of interest?
# 
# >The Loan status feature with different status describe the various dataset findings and reasons in each series of data.
# >The Prosper Rating identify the listings assigned at the every time created for loans originated since July2009.
# >For the Borrower APR, the Percentage Rate of annual loans and Borrower Rate which has the interest rate for the loan.

# ## Univariate Exploration
# In this uniavariate exploartions, i will fo us on the key variables that eil lead to the main findings of the analysis and the 
# further data discoveries.
# 
# Based on the different variables stated in the dataset.
# 

# Univariate exploration on Propser loan status on main variables: loan status:employement status and Term.

# In[13]:


#Let's start our exploration by looking at the main variable of interest: loan status:Employment status
plt.title('Distribution of Loanstatus');
base_color = sb.color_palette()[0]
plt.xticks(rotation=90)
sb.countplot(data = data_df,  y= 'LoanStatus', color = base_color);


# Explanations:
#     
#     in the prosper dataset, the current loans status are the most.
#     
#     the completed loans are the second largest section in Prosper.
#     
#     all the PastDue loans are the least in the dataset and they are listed according to their days past due with (1-15 days) being the most.
#     
#     the cancelled loan status have a nill/0 value count.
#     
#     chargedOff loans and Defaulted loans are still a high value of count in the LoansData.
#     
#     Observation.
#     
#     In general , PropserData loans are completed than at higher rate as compared to Defaulted status.

# In[14]:


#the length of loan expressed in months as from the dataset needed.
plt.title('LoansAmount Duration');
plt.xticks(rotation=90)
sb.countplot(data = data_df, x = 'Term', color = base_color);


# Explanations and observations.
# 
# most of loans took 36 months and second taken was 60 months then 12 months.

# In[ ]:





# In[15]:


#the employment status of the borrower at the time they posted the listings.
plt.title('Distribution of EmploymentStatus');
plt.xticks(rotation=90)
sb.countplot(data = data_df, y = 'EmploymentStatus', color = base_color);


# Explanations.
# 
# Employment status shows the status of the borrowers as at the time they posted the listings.
# 
# Observations:
#     
#     the employed are the most listings in ProsperData set and those whose employment status is Full-time.
#     
#     the Self-employed and those whose EmployementStatus is Not-available have relatively equal rating.
#     
#     Not-employed ,Part-time and Retired are the list available for listings in ProsperData.
#     
#     those whose status is 'Other' also have a relatively higher rating as compred to Not-emplyed,Part-time and Retired.

# ### Loan Ordinal Amount

# Loan ordinal amount is the origination amount of the loan from the borrower

# In[16]:


#LoanOrdinalAmounts
plt.figure(figsize=[8, 5])
plt.hist(data_df['LoanOriginalAmount']);
plt.xlabel('Original loan amount ($)');
plt.ylabel('LoanCount')
plt.title('Distribution ofLoanOrdinalAmounts');


# From the underlying visual the loan amounts are  from estimated from 10k to 35k hence ordinal loan amounts must be in the range of 5k
# from the distribution hence a co-relation with loans first acquired.
# that sums a loan status relation from the ordinal distributions and loans acquired.

# In[ ]:





# ### Discuss the distribution(s) of your variable(s) of interest. Were there any unusual points? Did you need to perform any transformations?
# 
# > The StatedMonthlyIncome, the histogram gets clustered to the left due to uneven distribution of data.
# 
# >the Employed are the most borrowers in the prosperLoanData then the Full-time borrowers whereas other categories are small parts of borrowers.
# >most of the loans borrowerd from prosperLoanData set are Current Loans and in Term variable most of loans took 36 months as the longest period of borrowers. 
# 
# ### Of the features you investigated, were there any unusual distributions? Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did you do this?
# 
# >Looking at the main variables in the dataset, most of the loans borrowerd are Currentloans.
# >in the dataset we are exploring the factors that contfribute to loans borrowed and the different instances that lead to it.
# >What factors affect a loan’s outcome status?
# >What affects the borrower’s APR or interest rate?

# ## Bivariate Exploration
# 
# > In this section, investigate relationships between pairs of variables in your
# data. Make sure the variables that you cover here have been introduced in some
# fashion in the previous section (univariate exploration).

# In[17]:


# univariate plots of LoanStatus, to further explore the data i wouldtranslate  the Loanstatus to view the fields counts.
#view the sum count of Loanstatus in Completed,Defaulted,Chargedoff using function
condition = ( data_df['LoanStatus'] == 'Completed') | (data_df['LoanStatus'] == 'Defaulted') |(data_df['LoanStatus'] == 'Current')|                  (data_df['LoanStatus'] == 'Chargedoff')
data_df = data_df[condition]

def change_to_defaulted(row):
    if row['LoanStatus'] == 'Chargedoff':
        return 'Defaulted'
    else:
        return row['LoanStatus']
    
data_df['LoanStatus'] = data_df.apply(change_to_defaulted, axis=1)
data_df['LoanStatus'].value_counts()


# Observations from the plotting
# 
# >Loans status, completed borrowed loans are 38076 while Defaulted loans are 17010.

# In[18]:


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


# >In the listing Category, Debt Consolidation, Home Improvement, Business, Auto and Other have less loans borrowed.
# >the Auto listings category has the list borrowed numberand Debt Consolidation the highest number in the listing 

# >1.using Loanstatus and Propser Rating i will compare the Defaulted and Completed datasets Loans.

# In[19]:



plt.title('ProsperRating Counts');
sb.countplot(data = data_df, x = 'LoanStatus', hue = 'ProsperRating (Alpha)', palette = 'Blues')


# >Explanations and Observations:
#     >in the current the most ProsperRating is C and according to the findings while HR is the list at the time the listing created.
#     >in Completed Rating, D is the highest ProsperRating since the loan listing was created.
#     >the A ProsperRatings appear relatively higher for the Completed and the Current.
#     >In the Loanstatus, the current borrowed loans have the highest ProsperRating in all the other ProsperLoanData set.

# >2.Analyse Loanstatus using the ListingsCategory and listings from date created.

# In[20]:


sb.countplot(data = data_df, x = 'LoanStatus', hue = 'ListingCategory (numeric)', palette = 'Blues');
plt.title('Distribution of Loanstatus');


# >Explanation and Observations.
# 
# >In the Loanstatus Listings: the Current Loanstatus is the highest in the Graphs of Borrowers Completed and Completed Loan status.
#     
# >Debt Consolidation Graph is the Highest in Current Loans and relatiely low in Completed and Defaulted Loans in the prosperLoanData set.
# 

# In[21]:


#Using Loanstatus to analyse overview graphs in LoanAmounts.
plt.title('LoanStatus division');
sb.boxplot(data = data_df, x = 'LoanStatus', y = 'LoanOriginalAmount', color = base_color);


# Observations and Explanantions.
# 
# >From the Graph plotting visual, its noticed that the Current Loanstatus in the listings are the largest scores in the dataset as 
# compared to Defaulted and Completed LoansAmounts.

# In the last dataset Ratings i will plot and compare thye graphs between Employment status and how this relates to the Propser Rating
# 
# >Employment Status is the employment status of the borrower at the time they posted the listings.
# 
# >Prosper Ratings are the assigned at the time the listigs were done.

# In[22]:


#Employment status and Prosper Rating graphs to compare.
plt.figure(figsize = [12, 10])
plt.title('EmployementStatus and Rating');
sb.countplot(data = data_df, x = 'ProsperRating (Alpha)', hue = 'EmploymentStatus');


# Observations and Explanations.
# 
# >from the dataset Graph plotting, the Borrowers with the status Retired, Part-time, Not-Employed and others are lower in loans Ratings
# as compared to Self employed.
# 
# >the Borrowers with the status of Employed have a higher rating of Loans from prosperLoanData company across all the other Ratings and 
# listings since created in July 2009.

# In[ ]:





# In[ ]:





# ### Talk about some of the relationships you observed in this part of the investigation. How did the feature(s) of interest vary with other features in the dataset?
# 
# > In the prosperLoanData set, when i plot LoanStatus, its evident that Current Loan Borrowers are the majority in the Listings since July 2009, and relatively Loans that are Completed are equally higher as compared to Defaulted Loans.
# 
# >in Employment Status against Loans borrrowerd, its noticed that most borrowers who's status is Employed tend to have the highest propability of acquiring Loans with prosper loaning company, consiquently when Not -Employed, Retired or Part-Time you have little chances of borrowing Loans from propser company.
# 
# >Its evident that ,for a good and higher Loans Rating ,you need Employment status hence their is a co-relation between Loans status and Term used in paying which is 36 months for most borrowers.
# 
# ### Did you observe any interesting relationships between the other features (not the main feature(s) of interest)?
# 
# > from the dataset Graph plotting, the Borrowers with the status Retired, Part-time, Not-Employed and others are lower in loans Ratings as compared to Self employed.
# 
# >the Borrowers with the status of Employed have a higher rating of Loans from prosperLoanData company across all the other Ratings and listings since created in July 2009.

# ## Multivariate Exploration
# 
# > Create plots of three or more variables to investigate your data even
# further. Make sure that your investigations are justified, and follow from
# your work in the previous sections.

# Investigate more on Loanstatus in Relation to PropserRating and bring out more insights on the dataset.

# In[23]:


#using seaborn as sb, 
plt.figure(figsize = [12, 8])
sb.boxplot(data=data_df,
           x='ProsperRating (Alpha)',
           y='LoanOriginalAmount', 
           hue='LoanStatus' ,palette = 'Blues');
plt.title('Distribution of LoanOriginalAmount');


# > Explanation and Observation: 
#     
# >from prosperLoanData plotting, LoanOrdinalAmount is the Origination amount of the Loan.
#     
# >in the dataset, most loans that are Defaulted have relatively high LoanOrdinalAmount than Completed but lower rating than 
#     current Loans in the dataset.
#     
# >Current loans will still be the highest amounts of loans in prosper company, similarly its noticed that HR loan Ordinal ratings
#     are the list ratings for both the Current, Defaulted and Completed loans in the dataset prosper company which is different case for 
#     E PropserRatings that Curent loans appeare to be the list hence list that E as the least prefered Rating by any of the Loans status
#     by borrowers.

# Using ProsperRating ill further get an overview of LoansStatus

# In[24]:


pip install -U seaborn


# In[25]:


pip install seaborn --upgrade


# In[26]:


#checking the listing Category ofLoans in Amounts od borrowerd Loans using Violins plots
plt.figure(figsize = [12, 8])
sb.violinplot(data=data_df, 
               x='ListingCategory (numeric)', 
               y='LoanOriginalAmount', 
               hue='LoanStatus');
plt.title('Distribution shwowing Listing Category');


# >In LoanOrdinalAmounts, Auto Listing Category in prosper Company tend to have a simillar trend in borrowing of Loans, besides the 
#  loan credits Business and Home Improvements have a similar size in Loans borrowing amounts.
# 
# >Debt Consolidation Category in prosper company is similar and of lower ratings is completed and Defaulted Loans as compared to  Curent
# Loans which have a higher Listing Amounts across all the Other, HomeImprovement, Auto and Business ratings.
# 
# >Consiquently, all the ListingCategories are above the quartely threshold of the highest rating whish are the Current Loans.

# In[27]:


#further exploration using Term of loans stated earlier in the bivariate analysis
fig, ax = plt.subplots(ncols=2, figsize=[12,6])
plt.title('ProsperRating vs Income');
sb.pointplot(data = data_df, x = 'ProsperRating (Alpha)', y = 'StatedMonthlyIncome', hue = 'Term',
           palette = 'Purples', linestyles = '', dodge = 0.4, ax=ax[0])
plt.title('ProsperRating vs Income');
sb.pointplot(data = data_df, x = 'ProsperRating (Alpha)', y = 'LoanOriginalAmount', hue = 'Term',
           palette = 'Greens', linestyles = '', dodge = 0.4, ax=ax[1]);


# >StatedMonthlyIncome is the income the Borrower stated at the time the listing was created.
# 
# >Similarly the loan Term of 36 months is still dorminant in the dataset of loan Borrowers, hence with propser rating the three Loan Terms 
# of 12, 36 and 60 in months which co-relates with the amounts of loans significantly.
# 
# >However, the Term and the effect do not co-relate in the borrowing of loans and monthly terms associated.

# In[ ]:





# ### Talk about some of the relationships you observed in this part of the investigation. Were there features that strengthened each other in terms of looking at your feature(s) of interest?
# 
# > There are no exisiting relationships between the Term of loans and Rating rather the Status which is either , Employed, Self-Employed,Part-time among others that determine.
# 
# >in the analysis, with beteer ratings the loan amounts of the Terms increases as the terms and loan amounts also increases.
# 
# ### Were there any interesting or surprising interactions between features?
# 
# > In the prosper rating its noticed that , from HR listings, in StatedMonthlyIncome and LoanOrdinalRating, 60 months loans have a higher Ordinal rating as compared to 36 months for LoanAmountsIncome dataset, Therefore, the multivariate explorartion reveals that In Loan duartion of 36 months ismost prefered for the Current loans which are also the highest in the borrowing of loans.
# 
# >positivelt i can relate the term on 36 months to Employed stattus borrowers who are also the more prefreable in the prosper company since they also are the majority of the loans borrowers in the dataset.

# ## Conclusions
# >First load od dataset into the working environment as a df defines by the df =pd.read_csv('prosperLoanData.csv').
# >this defines all the working data for the explorartions.
# 
# >From Univariate, Bivariate and  Multivariate.
# >Observation 1.
# the employed are the most listings in ProsperData set and those whose employment status is Full-time.
# 
# >the Self-employed and those whose EmployementStatus is Not-available have relatively equal rating.
# 
# >Not-employed ,Part-time and Retired are the list available for listings in ProsperData.
# 
# >those whose status is 'Other' also have a relatively higher rating as compred to Not-emplyed,Part-time and Retired.
# 
# >Observation 2.
# 
# >Employment Status is the employment status of the borrower at the time they posted the listings.
# 
# >Prosper Ratings are the assigned at the time the listigs were done
# 
# Conclusion:
# 
# From prosperloandata, there binding factors that determine the loan borrowing and the ratings that determine the allocations interms of months in loans.
# 
# However, all the loans from prosper company depend on the loanstatus of Employed since its evident from the explorations that all borrowers from that category are the most preferd for loans in the company.
# 
# most loans in the company are also current loans borrowerd and defaulated loans being the least in the loaning from the company.

# In[28]:


get_ipython().system('jupyter nbconvert notebook_name.ipynb --to slides --post serve --no-input --no-prompt')


# In[ ]:


get_ipython().system('jupyter nbconvert Part_I_exploration_template.ipynb --to slides --post serve --no-input --no-prompt')


# In[ ]:




