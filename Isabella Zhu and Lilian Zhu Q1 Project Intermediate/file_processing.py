import pandas as pd

# get rid of instances with missing class variables
df = pd.read_csv('covid.csv', nrows = 1000000) # read in the csv file into pandas dataframe
# limited data to first one million cases because we don't want too much data
print(df.shape) # check how many total instances there are
df_yes = df[df['death_yn'] == "Yes"] # filter only instances that died from COVID
print(df_yes.shape) # 8889 instances
df_no = df[df['death_yn'] == "No"] # filter only instances that didn't die from COVID
print(df_no.shape) # 166663 instances
df_new = pd.concat([df_yes, df_no]) # merging two datasets df_yes and df_no
df_new.to_csv("covid_clean.csv", index = False)

# check for redundancy
df = pd.read_csv('covid_clean.csv')
print(df.shape) # before removing duplicates (output: 175552 instances)
df.drop_duplicates() # removing duplicates
print(df.shape) # after removing duplicates (output: 175552 instances)
df.to_csv("covid_clean_2.csv", index = False)

# delete derivable attributes
df = pd.read_csv('covid_clean_2.csv')
print(df.shape) # 21 attributes
df.drop('state_fips_code', inplace=True, axis=1)
df.drop('county_fips_code', inplace=True, axis=1)
print(df.shape) # 19 attributes 
df.to_csv("covid_clean_3.csv", index = False)
