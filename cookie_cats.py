import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

df = pd.read_csv('cookie_cats.csv')
# df.info()
# print(df)
# print(df.groupby('version').count())

duplicateRows = df[df.duplicated()]
print(duplicateRows)

df['retention_1'] = df['retention_1'].astype(int)
df['retention_7'] = df['retention_7'].astype(int)
df['version'] = df['version'].replace(['gate_30'],'A')
df['version'] = df['version'].replace(['gate_40'],'B')
print(df)
print(df['sum_gamerounds'].describe())
sns.boxplot(x=df['sum_gamerounds'])
plt.show()
df = df[df['sum_gamerounds']<10000]
# print(df['sum_gamerounds'].describe())
# sns.boxplot(x=df['sum_gamerounds'])
# plt.show()

########### RETENTION RATES ###########

mean_retention1_A = ((df[df['version'] == 'A'].groupby('version')['retention_1'].mean())*100).values[0]
mean_retention1_B = ((df[df['version'] == 'B'].groupby('version')['retention_1'].mean())*100).values[0]
mean_retention7_A = ((df[df['version'] == 'A'].groupby('version')['retention_7'].mean())*100).values[0]
mean_retention7_B = ((df[df['version'] == 'B'].groupby('version')['retention_7'].mean())*100).values[0]

print(f'\nRetention rate D1 for group A: {mean_retention1_A:.2f}\nRetention rate D1 for group B: {mean_retention1_B:.2f}\nRetention rate D7 for group A: {mean_retention7_A:.2f}\nRetention rate D7 for group B: {mean_retention7_B:.2f}')
print("\n TWO WAY Z-TEST TEST for retention rate D1\n")
control_results_1= df[df['version'] == 'A'].drop(columns=['sum_gamerounds','retention_7','userid'])['retention_1']
treatment_results_1= df[df['version'] == 'B'].drop(columns=['sum_gamerounds','retention_7','userid'])['retention_1']

n_con = control_results_1.count()
n_treat = treatment_results_1.count()
successes = [control_results_1.sum(), treatment_results_1.sum()]
nobs = [n_con, n_treat]

z_stat, pval = proportions_ztest(successes, nobs=nobs)
(lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(successes, nobs=nobs, alpha=0.05)


print(f'z statistic: {z_stat:.2f}')
print(f'p-value: {pval:.3f}')
print(f'ci 95% for control group: [{lower_con:.3f}, {upper_con:.3f}]') 
print(f'ci 95% for treatment group: [{lower_treat:.3f}, {upper_treat:.3f}]')

print("\n TWO WAY Z-TEST TEST for retention rate D7\n")
control_results_7= df[df['version'] == 'A']['retention_7']
treatment_results_7= df[df['version'] == 'B']['retention_7']

n_con = control_results_7.count()
n_treat = treatment_results_7.count()
successes = [control_results_7.sum(), treatment_results_7.sum()]
nobs = [n_con, n_treat]

z_stat, pval = proportions_ztest(successes, nobs=nobs)
(lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(successes, nobs=nobs, alpha=0.05)


print(f'z statistic: {z_stat:.2f}')
print(f'p-value: {pval:.3f}')
print(f'ci 95% for control group: [{lower_con:.3f}, {upper_con:.3f}]') 
print(f'ci 95% for treatment group: [{lower_treat:.3f}, {upper_treat:.3f}]')

########### GAME ROUNDS ###########
df_sumrounds = df.drop(columns=['retention_1','retention_7','userid'])
sns.boxplot(x="version", y="sum_gamerounds", data=df_sumrounds)
plt.show()
df_sumrounds_A = df_sumrounds[df_sumrounds['version'] == 'A'].describe()
df_sumrounds_B = df_sumrounds[df_sumrounds['version'] == 'B'].describe()
print(f'\nDESCRIPTION OF GAME ROUNDS _ GROUP A:\n{df_sumrounds_A}')
print(f'\nDESCRIPTION OF GAME ROUNDS _ GROUP B:\n{df_sumrounds_B}')
