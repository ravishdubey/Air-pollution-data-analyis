#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#reading the file and dataframes as per the requirement.
df=pd.read_csv('grimmvsopc.csv')
pd.options.display.float_format = "{:.2f}".format
df_pm = df.drop(['Temperature_dht11_1',
       'RH_dht11_1', 'Temperature_dht11_2', 'RH_dht11_2',
       'Temperature_kestrel', 'RH_kestrel', 'Wind_Speed_KESTREL'], axis=1)
df_pm10=df_pm.drop(['PM25_GRIMM', 'PM1_GRIMM','PM25_OPC_N2_1', 'PM1_OPC_N2_1', 'PM25_OPC_N2_2',
       'PM1_OPC_N2_2', 'PM25_NOVA','PM25_EVM7'],axis=1)
df_pm25=df_pm.drop(['PM10_GRIMM', 'PM1_GRIMM', 'PM10_OPC_N2_1',
        'PM1_OPC_N2_1', 'PM10_OPC_N2_2',
       'PM1_OPC_N2_2', 'PM10_NOVA'],axis=1)
df_pm1=df_pm.drop(['PM10_GRIMM', 'PM25_GRIMM', 'PM10_OPC_N2_1',
       'PM25_OPC_N2_1', 'PM10_OPC_N2_2', 'PM25_OPC_N2_2',
        'PM25_NOVA', 'PM10_NOVA','PM25_EVM7'],axis=1)
df_t=df.drop(['PM10_GRIMM', 'PM25_GRIMM', 'PM1_GRIMM', 'PM10_OPC_N2_1',
       'PM25_OPC_N2_1', 'PM1_OPC_N2_1', 'PM10_OPC_N2_2', 'PM25_OPC_N2_2',
       'PM1_OPC_N2_2', 'PM25_NOVA', 'PM10_NOVA','Wind_Speed_KESTREL','RH_dht11_1', 'RH_dht11_2', 'RH_kestrel','PM25_EVM7'],axis=1)
df_met=df.drop(['PM10_GRIMM', 'PM25_GRIMM', 'PM1_GRIMM', 'PM10_OPC_N2_1',
       'PM25_OPC_N2_1', 'PM1_OPC_N2_1', 'PM10_OPC_N2_2', 'PM25_OPC_N2_2',
       'PM1_OPC_N2_2', 'PM25_NOVA', 'PM10_NOVA','Wind_Speed_KESTREL','PM25_EVM7'],axis=1)
df_pm_t = df.drop(['Temperature_dht11_1',
       'RH_dht11_1', 'Temperature_dht11_2', 'RH_dht11_2', 'Wind_Speed_KESTREL','PM25_EVM7'], axis=1)

#plotting the violin plot

plt.figure(figsize=(8,6))
sns.set(font_scale=1.2,style='whitegrid')
fig=sns.violinplot(data=df_pm10)
fig.set_ylabel('PM$_{10}$ concentration ($\mu g m^{-3}$)')
fig.set_xticklabels(['GRIMM', 'OPC N2(1)','OPC N2(2)','PM NOVA'])
fig.set_title('Violin plot for PM$_{10}$ concentration')
plt.tight_layout
