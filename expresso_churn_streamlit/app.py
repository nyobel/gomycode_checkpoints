import streamlit as st
import joblib
import pandas as pd

# Load artifacts
model = joblib.load('churn_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')
feature_names = joblib.load('feature_names.pkl')

st.title("Expresso Churn Prediction")
st.divider()

# Create input fields for ALL features used in training
st.header("Customer Details")
st.divider()


#categorical features
region = st.selectbox("Region", ['DAKAR', 'THIES', 'SAINT-LOUIS', 'LOUGA',
			'KAOLACK', 'DIOURBEL', 'TAMBACOUNDA', 'KAFFRINE', 'KOLDA', 'FATICK', 'MATAM', 'ZIGUINCHOR',
			'SEDHIOU', 'KEDOUGOU'])
tenure = st.selectbox("Tenure", ['K > 24 month', 'I 18-21 month', 'G 12-15 month', 'H 15-18 month',
       'J 21-24 month', 'F 9-12 month', 'D 3-6 month', 'E 6-9 month'])
top_pack = st.selectbox('the most active packs?', ['On net 200F=Unlimited _call24H', 'All-net 500F=2000F;5d',
       'On-net 1000F=10MilF;10d', 'Data:1000F=5GB,7d',
       'Mixt 250F=Unlimited_call24H',
       'MIXT:500F= 2500F on net _2500F off net;2d', 'On-net 500F_FNF;3d',
       'Data: 100 F=40MB,24H', 'MIXT: 200mnoff net _unl on net _5Go;30d',
       'Jokko_Daily', 'Data: 200 F=100MB,24H', 'Data:490F=1GB,7d',
       'Twter_U2opia_Daily', 'On-net 500=4000,10d', 'Data:1000F=2GB,30d',
       'IVR Echat_Daily_50F', 'Pilot_Youth4_490',
       'All-net 500F =2000F_AllNet_Unlimited', 'Twter_U2opia_Weekly',
       'Data:200F=Unlimited,24H', 'On-net 200F=60mn;1d',
       'All-net 600F= 3000F ;5d', 'Pilot_Youth1_290',
       'All-net 1000F=(3000F On+3000F Off);5d', 'VAS(IVR_Radio_Daily)',
       'Data:3000F=10GB,30d', 'All-net 1000=5000;5d',
       'Twter_U2opia_Monthly', 'MIXT: 390F=04HOn-net_400SMS_400 Mo;4h\t',
       'FNF2 ( JAPPANTE)', 'Yewouleen_PKG', 'Data:150F=SPPackage1,24H',
       'WIFI_Family_2MBPS', 'Data:500F=2GB,24H', 'MROMO_TIMWES_RENEW',
       'New_YAKALMA_4_ALL', 'Data:1500F=3GB,30D',
       'All-net 500F=4000F ; 5d', 'Jokko_promo', 'All-net 300=600;2d',
       'Data:300F=100MB,2d',
       'MIXT: 590F=02H_On-net_200SMS_200 Mo;24h\t\t',
       'All-net 500F=1250F_AllNet_1250_Onnet;48h', 'Facebook_MIX_2D',
       '500=Unlimited3Day', 'On net 200F= 3000F_10Mo ;24H',
       '200=Unlimited1Day', 'YMGX 100=1 hour FNF, 24H/1 month',
       'SUPERMAGIK_5000', 'Data:DailyCycle_Pilot_1.5GB', 'Staff_CPE_Rent',
       'MIXT:1000F=4250 Off net _ 4250F On net _100Mo; 5d',
       'Data:50F=30MB_24H', 'Data:700F=SPPackage1,7d',
       'Data: 490F=Night,00H-08H', 'Data:700F=1.5GB,7d',
       'Data:1500F=SPPackage1,30d', 'Data:30Go_V 30_Days',
       'MROMO_TIMWES_OneDAY', 'On-net 300F=1800F;3d',
       'All-net 5000= 20000off+20000on;30d', 'WIFI_ Family _4MBPS',
       'CVM_on-net bundle 500=5000', 'Internat: 1000F_Zone_3;24h\t\t',
       'DataPack_Incoming', 'Jokko_Monthly', 'EVC_500=2000F',
       'On-net 2000f_One_Month_100H; 30d',
       'MIXT:10000F=10hAllnet_3Go_1h_Zone3;30d\t\t', 'EVC_Jokko_Weekly',
       '200F=10mnOnNetValid1H', 'IVR Echat_Weekly_200F',
       'WIFI_ Family _10MBPS', 'Internat: 1000F_Zone_1;24H\t\t',
       'Jokko_Weekly', 'SUPERMAGIK_1000',
       'MIXT: 500F=75(SMS, ONNET, Mo)_1000FAllNet;24h\t\t',
       'VAS(IVR_Radio_Monthly)',
       'MIXT: 5000F=80Konnet_20Koffnet_250Mo;30d\t\t',
       'Data: 200F=1GB,24H', 'EVC_JOKKO30',
       'NEW_CLIR_TEMPALLOWED_LIBERTE_MOBILE', 'TelmunCRBT_daily',
       'FIFA_TS_weekly', 'VAS(IVR_Radio_Weekly)',
       'Internat: 2000F_Zone_2;24H\t\t', 'APANews_weekly', 'EVC_100Mo',
       'pack_chinguitel_24h', 'Data_EVC_2Go24H',
       'Mixt : 500F=2500Fonnet_2500Foffnet ;5d', 'FIFA_TS_daily',
       'MIXT: 4900F= 10H on net_1,5Go ;30d', 'CVM_200f=400MB',
       'IVR Echat_Monthly_500F', 'All-net 500= 4000off+4000on;24H',
       'FNF_Youth_ESN', 'Data:1000F=700MB,7d', '1000=Unlimited7Day',
       'Incoming_Bonus_woma', 'CVM_100f=200 MB', 'CVM_100F_unlimited',
       'pilot_offer6', '305155009', 'Postpaid FORFAIT 10H Package',
       'EVC_1Go', 'GPRS_3000Equal10GPORTAL',
       'NEW_CLIR_PERMANENT_LIBERTE_MOBILE', 'Data_Mifi_10Go_Monthly',
       '1500=Unlimited7Day', 'EVC_700Mo', 'CVM_100f=500 onNet',
       'CVM_On-net 1300f=12500', 'pilot_offer5', 'EVC_4900=12000F',
       'CVM_On-net 400f=2200F', 'YMGX on-net 100=700F, 24H',
       'CVM_150F_unlimited', 'EVC_MEGA10000F', 'pilot_offer7',
       'CVM_500f=2GB', 'SMS Max', '301765007', '150=unlimited pilot auto',
       'MegaChrono_3000F=12500F TOUS RESEAUX', 'pilot_offer4',
       'Go-NetPro-4 Go', '200=unlimited pilot auto',
       'ESN_POSTPAID_CLASSIC_RENT', 'Data_Mifi_10Go',
       'Data:New-GPRS_PKG_1500F', 'GPRS_BKG_1000F MIFI',
       'Data:OneTime_Pilot_1.5GB', 'FIFA_TS_monthly',
       'GPRS_PKG_5GO_ILLIMITE', 'Data_Mifi_20Go', 'APANews_monthly',
       'NEW_CLIR_TEMPRESTRICTED_LIBERTE_MOBILE', 'GPRS_5Go_7D_PORTAL',
       'Package3_Monthly'])


# numerical features
montant = st.number_input("Monthly Amount (MONTANT)", min_value=0)
frequence_rech = st.number_input('Number of times the customer refilled', min_value=0)
revenue = st.number_input('Monthly income of each client', min_value=0)
arpu_segment = st.number_input('Income over 90 days / 3', min_value=0)
frequence = st.number_input('Number of times the client has made an income', min_value=0)
data_volume = st.number_input('Number of connections', min_value=0)
on_net = st.number_input('Inter expresso call', min_value=0)
orange = st.number_input('call to orange', min_value=0)
tigo = st.number_input("Tigo", min_value=0)
zone1 = st.number_input("Zone 1", min_value=0)
zone2 = st.number_input("Zone 2", min_value=0)
regularity = st.number_input('number of times the client is active for 90 days', min_value=0)
freq_top_pack = st.number_input('number of times the client has activated the top pack packages', min_value=0)

st.divider()



if st.button("Predict Churn"):
    # Create input dataframe with CORRECT ORDER
    input_data = pd.DataFrame([{
        'REGION': region,
        'TENURE': tenure,
        'MONTANT': montant,
        'FREQUENCE_RECH': frequence_rech,
        'REVENUE': revenue,
        'ARPU_SEGMENT': arpu_segment,
        'FREQUENCE': frequence,
        'DATA_VOLUME': data_volume,
        'ON_NET': on_net,
        'ORANGE': orange,
        'TIGO': tigo,
        'ZONE1': zone1,
        'ZONE2': zone2,
        'REGULARITY': regularity,
        'TOP_PACK': top_pack,
        'FREQ_TOP_PACK': freq_top_pack
    }])


    # Encode categoricals using saved label encoders
    for col in ['REGION', 'TENURE', 'TOP_PACK']:  # Only categorical columns
        input_data[col] = label_encoders[col].transform(input_data[col])


    # Ensure EXACT feature order from training
    input_data = input_data[feature_names]

    # Predict
    try:
        proba = model.predict_proba(input_data)[0][1]
        st.success(f"Churn Probability: {proba:.2%}")
        st.write("Threshold: >50% indicates high churn risk")
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")