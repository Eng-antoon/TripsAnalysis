#!/usr/bin/env python3
import pandas as pd
from io import StringIO

# Define input and output file paths
input_file = 'mixpanel_export.xlsx'       # Your original Mixpanel export file
output_file = 'data/data.xlsx'  # Final consolidated output

# Read the Mixpanel export Excel file
df = pd.read_excel(input_file)

# Consolidate the data: group by 'tripId' and take the last record per trip
df_consolidated = df.groupby('tripId', as_index=False).last()

# --- Define the mobile specs table as CSV ---
mobile_specs_csv = """Original Model,Brand,Device Name,Release Year,Android Version,Fingerprint Sensor,Accelerometer,Gyro,Proximity Sensor,Compass,Barometer,Background Task Killing Tendency,Chipset,RAM,Storage,Battery (mAh)
220733SFG,Xiaomi,Xiaomi 12 Lite,2022,12,True,True,True,True,True,False,High,Qualcomm Snapdragon 778G 5G,8GB,128GB,4300
23028RNCAG,Xiaomi,Xiaomi 13 Lite,2023,12,True,True,True,True,True,False,High,Qualcomm Snapdragon 7 Gen 1,8GB,128GB,4500
23106RN0DA,Xiaomi,Redmi 13C,2023,13,False,True,False,True,True,False,High,MediaTek Helio G85,4GB,128GB,5000
23129RAA4G,Xiaomi,Redmi Note 13 Pro 5G,2023,13,True,True,True,True,True,False,High,Qualcomm Snapdragon 7s Gen 2,8GB,256GB,5100
23129RN51X,Xiaomi,Redmi Note 13 Pro+ 5G,2023,13,True,True,True,True,True,False,High,MediaTek Dimensity 7200-Ultra,8GB,256GB,5000
2409BRN2CA,Xiaomi,Redmi 13,2024,14,False,True,False,True,True,False,High,MediaTek Helio G85,4GB,128GB,5030
BKK-LX2,Huawei,Y7 2019,2019,8.1 (Oreo),False,True,False,True,True,False,High,Qualcomm Snapdragon 450,3GB,32GB,4000
CPH1729,Oppo,A71 (2017),2017,7.1 (Nougat),False,True,False,True,True,False,High,MediaTek MT6750,2GB,16GB,3000
CPH1823,Oppo,A3s,2018,8.1 (Oreo),False,True,False,True,True,False,High,Qualcomm Snapdragon 450,2GB,16GB,4230
CPH1909,Oppo,A5 (2020),2020,9.0 (Pie),True,True,False,True,True,False,High,Qualcomm Snapdragon 665,3GB,64GB,5000
CPH1911,Oppo,A9 (2020),2019,9.0 (Pie),True,True,False,True,True,False,High,Qualcomm Snapdragon 665,4GB,128GB,5000
CPH1923,Oppo,A31,2020,9.0 (Pie),True,True,False,True,True,False,High,MediaTek Helio P35,4GB,64GB,4230
CPH1989,Oppo,A91,2020,9.0 (Pie),True,True,True,True,True,False,High,MediaTek Helio P70,8GB,128GB,4025
CPH2015,Oppo,A52,2020,10,True,True,False,True,True,False,High,Qualcomm Snapdragon 665,4GB,64GB,5000
CPH2095,Oppo,A73 5G,2020,10,True,True,False,True,True,False,High,MediaTek Dimensity 720,4GB,64GB,4040
CPH2121,Oppo,Reno5 4G,2020,11,True,True,True,True,True,False,High,Qualcomm Snapdragon 720G,8GB,128GB,4310
CPH2127,Oppo,A53,2020,10,True,True,False,True,True,False,High,Qualcomm Snapdragon 460,4GB,64GB,5000
CPH2159,Oppo,A74 4G,2021,11,True,True,False,True,True,False,High,Qualcomm Snapdragon 662,4GB,64GB,5000
CPH2185,Oppo,Reno6 5G,2021,11,True,True,True,True,True,False,High,MediaTek Dimensity 900 5G,8GB,128GB,4300
CPH2203,Oppo,A15s,2020,10,True,True,False,True,True,False,High,MediaTek Helio P35,3GB,32GB,4230
CPH2219,Oppo,A54,2021,10,True,True,False,True,True,False,High,MediaTek Helio P35,4GB,64GB,5000
CPH2239,Oppo,A16,2021,11,True,True,False,True,True,False,High,MediaTek Helio G35,4GB,64GB,5000
CPH2325,Oppo,A96,2022,11,True,True,False,True,True,False,High,Qualcomm Snapdragon 680 4G,8GB,128GB,5000
CPH2333,Oppo,A76,2022,11.3,True,True,False,True,True,False,High,Qualcomm Snapdragon 680 4G,4GB,128GB,5000
CPH2477,Oppo,A77 5G,2022,12.1,True,True,False,True,True,False,High,MediaTek Dimensity 810,4GB,64GB,5000
CPH2481,Oppo,A57 (2022),2022,12.1,True,True,False,True,True,False,High,MediaTek Helio G35,4GB,64GB,5000
CPH2565,Oppo,A78 5G,2023,13,True,True,False,True,True,False,High,MediaTek Dimensity 700,4GB,128GB,5000
CPH2579,Oppo,A58 4G,2023,13,True,True,False,True,True,False,High,MediaTek Helio G85,6GB,128GB,5000
CPH2591,Oppo,A38,2023,13.1,True,True,False,True,True,False,High,MediaTek Helio G85,4GB,64GB,5000
CPH2631,Oppo,A2 Pro 5G,2023,13,True,True,True,True,True,False,High,MediaTek Dimensity 7050,8GB,256GB,5000
CPH2637,Oppo,A2m,2023,13,True,True,False,True,True,False,High,MediaTek Dimensity 6020,4GB,128GB,5000
CPH2669,Oppo,A3x 5G,2024,14,True,True,False,True,True,False,High,MediaTek Dimensity 6300,8GB,128GB,5000
Infinix X652A,Infinix,Smart 5 Pro,2021,11,True,True,False,True,False,False,High,Unisoc SC9863A,2GB,32GB,6000
Infinix X656,Infinix,Hot 10 Play,2021,10,True,True,False,True,False,False,High,MediaTek Helio G25/G35,2GB,32GB,6000
Infinix X657C,Infinix,Smart 6 HD,2022,Android 11 (Go edition),False,True,False,True,False,False,High,Unisoc SC9863A,2GB,32GB,5000
Infinix X680,Infinix,Note 7,2020,10,True,True,True,True,True,False,High,MediaTek Helio G70,6GB,64GB,5000
Infinix X653,Infinix,Smart 5,2020,10,True,True,False,True,False,False,High,MediaTek Helio A20,2GB,32GB,5000
itel A665L,itel,A27,2022,Android 11 (Go edition),False,True,False,False,False,False,High,Unisoc SC9832E,2GB,32GB,4000
JKM-LX1,Huawei,P Smart (2019),2019,9.0 (Pie),True,True,False,True,True,False,High,Hisilicon Kirin 710,3GB,32GB,3400
MRD-LX1F,Huawei,Y6p,2020,10,True,True,False,True,True,False,High,MediaTek Helio P22,3GB,32GB,5000
STK-LX1,Huawei,Y7p,2020,9.0 (Pie),True,True,False,True,True,False,High,Hisilicon Kirin 710F,4GB,64GB,4000
ELI-NX9,Huawei,P40 Pro+,2020,10,True,True,True,True,True,True,High,Hisilicon Kirin 990 5G,8GB,256GB,4200
M2006C3MG,Xiaomi,Redmi 9C,2020,10,True,True,False,True,False,False,High,MediaTek Helio G35,2GB,32GB,5000
M2007J20CG,Xiaomi,Poco M3,2020,10,True,True,False,True,True,False,High,Qualcomm Snapdragon 662,4GB,64GB,6000
M2101K6G,Xiaomi,Poco X3 Pro,2021,11,True,True,True,True,True,False,High,Qualcomm Snapdragon 860,6GB,128GB,5160
M2101K7BG,Xiaomi,Redmi Note 10 Pro (India),2021,11,True,True,True,True,True,False,High,Qualcomm Snapdragon 732G,6GB,64GB,5020
M2102J20SG,Xiaomi,Redmi Note 10S,2021,11,True,True,True,True,True,False,High,MediaTek Helio G95,6GB,64GB,5000
Pixel 6,Google,Pixel 6,2021,12,True,True,True,True,True,True,Low,Google Tensor G1,8GB,128GB,4614
Redmi K20 Pro,Xiaomi,Redmi K20 Pro,2019,9.0 (Pie),True,True,True,True,True,False,High,Qualcomm Snapdragon 855,6GB,64GB,4000
Redmi Note 7,Xiaomi,Redmi Note 7,2019,9.0 (Pie),True,True,True,True,True,False,High,Qualcomm Snapdragon 660,3GB,32GB,4000
Redmi Note 8,Xiaomi,Redmi Note 8,2019,9.0 (Pie),True,True,True,True,True,False,High,Qualcomm Snapdragon 665,4GB,64GB,4000
Redmi Note 9S,Xiaomi,Redmi Note 9S,2020,10,True,True,True,True,True,False,High,Qualcomm Snapdragon 720G,4GB,64GB,5020
RMX2040,Realme,C11 (2020),2020,10,False,True,False,True,True,False,High,MediaTek Helio G35,2GB,32GB,5000
RMX2085,Realme,C21,2021,10,True,True,False,True,True,False,High,MediaTek Helio G35,3GB,32GB,5000
RMX2180,Realme,7i (India),2020,10,True,True,False,True,True,False,High,MediaTek Helio G85,4GB,64GB,6000
RMX2185,Realme,Narzo 20,2020,10,True,True,False,True,True,False,High,MediaTek Helio G85,4GB,64GB,6000
RMX2189,Realme,C15,2020,10,True,True,False,True,True,False,High,MediaTek Helio G35,3GB,32GB,6000
RMX3231,Realme,C25Y,2021,11,True,True,False,True,True,False,High,Unisoc Tiger T610,4GB,64GB,5000
RMX3261,Realme,C21Y,2021,11,True,True,False,True,True,False,High,Unisoc T610,3GB,32GB,5000
RMX3263,Realme,Narzo 50i,2021,11 (Go edition),False,True,False,True,False,False,High,Unisoc SC9863A,2GB,32GB,5000
RMX3269,Realme,C25s,2021,11,True,True,False,True,True,False,High,MediaTek Helio G85,4GB,64GB,6000
RMX3363,Realme,9 Pro 5G,2022,12,True,True,True,True,True,False,High,Qualcomm Snapdragon 695 5G,6GB,128GB,5000
RMX3627,Realme,C30s,2022,Android 12 (Go edition),True,True,False,True,False,False,High,Unisoc SC9863A2,2GB,32GB,5000
RMX3710,Realme,C55,2023,13,True,True,False,True,True,False,High,MediaTek Helio G88,6GB,128GB,5000
RMX3834,Realme,Narzo N53,2023,13,True,True,False,True,True,False,High,Unisoc Tiger T612,4GB,64GB,5000
RMX3890,Realme,Narzo 60 5G,2023,13,True,True,True,True,True,False,High,MediaTek Dimensity 6020,8GB,128GB,5000
RMX3910,Realme,C67 5G,2023,13,True,True,False,True,True,False,High,MediaTek Dimensity 6100+,4GB,128GB,5000
RMX3939,Realme,C65,2024,14,True,True,False,True,True,False,High,MediaTek Helio G85,4GB,128GB,5000
RMX3997,Realme,Narzo N55,2023,13,True,True,False,True,True,False,High,MediaTek Helio G88,4GB,64GB,5000
SM-A022F,Samsung,Galaxy A02,2021,10,False,True,False,True,False,False,Moderate,MediaTek MT6739W,2GB,32GB,5000
SM-A025F,Samsung,Galaxy A02s,2020,10,False,True,False,True,False,False,Moderate,Qualcomm Snapdragon 450,3GB,32GB,5000
SM-A032F,Samsung,Galaxy A03 Core,2021,Android 11 (Go edition),False,True,False,True,False,False,Moderate,Unisoc SC9863A,2GB,32GB,5000
SM-A057F,Samsung,Galaxy A05s,2023,13,True,True,False,True,False,False,Moderate,Exynos 850,4GB,64GB,5000
SM-A107F,Samsung,Galaxy A10s,2019,9.0 (Pie),True,True,False,True,False,False,Moderate,MediaTek Helio P22,2GB,32GB,4000
SM-A125F,Samsung,Galaxy A12,2020,10,True,True,False,True,False,False,Moderate,MediaTek Helio P35,4GB,64GB,5000
SM-A137F,Samsung,Galaxy A13 (4G),2022,12,True,True,True,True,True,False,Moderate,Exynos 850,4GB,64GB,5000
SM-A155F,Samsung,Galaxy A15 (5G),2023,14,True,True,True,True,True,False,Moderate,MediaTek Dimensity 6100+,4GB,128GB,5000
SM-A205F,Samsung,Galaxy A20,2019,9.0 (Pie),True,True,True,True,True,False,Moderate,Exynos 7884,3GB,32GB,4000
SM-A217F,Samsung,Galaxy A21s,2020,10,True,True,False,True,False,False,Moderate,Exynos 850,4GB,64GB,5000
SM-A235F,Samsung,Galaxy A23 (4G),2022,12,True,True,False,True,True,False,Moderate,Qualcomm Snapdragon 680 4G,4GB,64GB,5000
SM-A245F,Samsung,Galaxy A24 (4G),2023,13,True,True,False,True,True,False,Moderate,MediaTek Helio G99,6GB,128GB,5000
SM-A305F,Samsung,Galaxy A30,2019,9.0 (Pie),True,True,True,True,True,False,Moderate,Exynos 7904,4GB,64GB,4000
SM-A325F,Samsung,Galaxy A32 (4G),2021,11,True,True,True,True,True,False,Moderate,MediaTek Helio G80,4GB,64GB,5000
SM-A515F,Samsung,Galaxy A51,2019,10,True,True,True,True,True,False,Moderate,Exynos 9611,4GB,64GB,4000
SM-A750F,Samsung,Galaxy A7 (2018),2018,8.0 (Oreo),True,True,True,True,True,False,Moderate,Exynos 7885,4GB,64GB,3300
SM-M115F,Samsung,Galaxy M11,2020,10,True,True,False,True,False,False,Moderate,Qualcomm Snapdragon 450,3GB,32GB,5000
SM-M127F,Samsung,Galaxy M12,2021,11,True,True,False,True,False,False,Moderate,Exynos 850,4GB,64GB,6000
TECNO BG6,Tecno,Spark Go 2020,2020,Android 10 (Go edition),False,True,False,True,False,False,High,MediaTek Helio A20,2GB,32GB,4000
V2026,Vivo,Y20s (2020),2020,10.5,True,True,True,True,True,False,High,Qualcomm Snapdragon 460,4GB,128GB,5000
V2061,Vivo,Y51 (2020),2020,11,True,True,True,True,True,False,High,Qualcomm Snapdragon 665,4GB,128GB,5000
V2120,Vivo,Y72 5G,2021,11,True,True,True,True,True,False,High,MediaTek Dimensity 700 5G,8GB,128GB,5000
V2207,Vivo,Y55 5G,2022,12,True,True,True,True,True,False,High,MediaTek Dimensity 700 5G,4GB,128GB,5000
V2247,Vivo,Y02t,2023,13,False,True,False,True,False,False,High,MediaTek Helio P35,4GB,64GB,5000
RMX3085,Realme,C21,2021,10,True,True,False,True,True,False,High,MediaTek Helio G35,3GB,32GB,5000
V2352,Vivo,Y27 4G,2023,13,True,True,False,True,True,False,High,MediaTek Helio G85,4GB,128GB,5000
"""

# Read mobile specs into a DataFrame
mobile_specs_df = pd.read_csv(StringIO(mobile_specs_csv))

# --- Merge the consolidated data with mobile specs ---
# We use the consolidated 'model' field and the specs' 'Original Model' as key.
merged_df = pd.merge(df_consolidated, mobile_specs_df, left_on='model', right_on='Original Model', how='left')

# --- Reorder and select columns as required ---
# Desired column order:
desired_columns = [
    'tripId',
    'time',
    'app_build_number',
    'app_version',
    'brand',
    'carrier',
    'city',
    'has_nfc',
    'lib_version',
    'manufacturer',
    'model',
    'Device Name',
    'Release Year',
    'Android Version',
    'Fingerprint Sensor',
    'Accelerometer',
    'Gyro',
    'Proximity Sensor',
    'Compass',
    'Barometer',
    'Background Task Killing Tendency',
    'Chipset',
    'RAM',
    'Storage',
    'Battery (mAh)',
    'os',
    'os_version',
    'region',
    'user_id',
    'wifi',
    'PhoneNumber',
    'UserId',
    'UserName',
    'event'
]

# Filter to only those columns that exist in the merged DataFrame
final_columns = [col for col in desired_columns if col in merged_df.columns]
merged_df_final = merged_df[final_columns]

# Save the final consolidated DataFrame to Excel
merged_df_final.to_excel(output_file, index=False)
print(f"Consolidated file saved as '{output_file}'")
