import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import os
from io import StringIO


st.title("Keeper League Decision Tool")
leagues = st.slider('How Many Teams are in your League?', 8, 1, 16)
st.write("You Selected ", leagues, 'Teams')
st.header("Upload Rankings Here :point_down:")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # Can be used wherever a "file-like" object is accepted:
    data = pd.read_csv(uploaded_file)
    player_list = data['Player Name'].tolist()
    
    Round_1_Value = round(data[data['Rank'] <= leagues]['Value'].mean(), 2)
    Round_2_Value = round(data[data['Rank'].between((leagues+1),(leagues*2))]['Value'].mean(), 2)
    Round_3_Value = round(data[data['Rank'].between((((leagues*2)+1)),(leagues*3))]['Value'].mean(), 2)
    Round_4_Value = round(data[data['Rank'].between((((leagues*3)+1)),(leagues*4))]['Value'].mean(), 2)
    Round_5_Value = round(data[data['Rank'].between((((leagues*4)+1)),(leagues*5))]['Value'].mean(), 2)
    Round_6_Value = round(data[data['Rank'].between((((leagues*5)+1)),(leagues*6))]['Value'].mean(), 2)
    Round_7_Value = round(data[data['Rank'].between((((leagues*6)+1)),(leagues*7))]['Value'].mean(), 2)
    Round_8_Value = round(data[data['Rank'].between((((leagues*7)+1)),(leagues*8))]['Value'].mean(), 2)
    Round_9_Value = round(data[data['Rank'].between((((leagues*8)+1)),(leagues*9))]['Value'].mean(), 2)
    Round_10_Value = round(data[data['Rank'].between((((leagues*9)+1)),(leagues*10))]['Value'].mean(), 2)
    Round_11_Value = round(data[data['Rank'].between((((leagues*10)+1)),(leagues*11))]['Value'].mean(), 2)
    Round_12_Value = round(data[data['Rank'].between((((leagues*11)+1)),(leagues*12))]['Value'].mean(), 2)
    Round_13_Value = round(data[data['Rank'].between((((leagues*12)+1)),(leagues*13))]['Value'].mean(), 2)
    Round_14_Value = round(data[data['Rank'].between((((leagues*13)+1)),(leagues*14))]['Value'].mean(), 2)
    Round_15_Value = round(data[data['Rank'].between((((leagues*14)+1)),(leagues*15))]['Value'].mean(), 2)
    Round_16_Value = round(data[data['Rank'].between((((leagues*15)+1)),(leagues*16))]['Value'].mean(), 2)
    Round_17_Value = round(data[data['Rank'].between((((leagues*16)+1)),(leagues*17))]['Value'].mean(), 2)
    Round_18_Value = round(data[data['Rank'].between((((leagues*17)+1)),(leagues*18))]['Value'].mean(), 2)
    Round_19_Value = round(data[data['Rank'].between((((leagues*18)+1)),(leagues*19))]['Value'].mean(), 2)
    Round_20_Value = round(data[data['Rank'].between((((leagues*19)+1)),(leagues*20))]['Value'].mean(), 2)
    
    round_value_dfs = [Round_1_Value, Round_2_Value, Round_3_Value, Round_4_Value, Round_5_Value, Round_6_Value, Round_7_Value, Round_8_Value, Round_9_Value, Round_10_Value,
                 Round_11_Value, Round_12_Value, Round_13_Value, Round_14_Value, Round_15_Value, Round_16_Value, Round_17_Value, Round_18_Value, Round_19_Value, Round_20_Value]
    
    round_dfs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    round_df = pd.DataFrame(
    {"Round": round_dfs,
     "Round Value": round_value_dfs
    })

    
    ### Keepers ###
    starting_player = player_list.index("Random Player")
    keeper_01 = st.selectbox('Keeper #1', player_list, key = "1", index = starting_player)
    keeper_round_01 = st.number_input("Round You're Keeping Keeper #1", min_value = 1,max_value = 20, step = 1)
    keeper_value_01 = (round(data[data['Player Name'] == keeper_01]['Value'].reset_index(drop=True)[0] - float(round_df[round_df['Round'] == keeper_round_01]['Round Value'].reset_index(drop=True)[0]),2))
    st.write("Value Gained by Keeping", keeper_01, ":" , keeper_value_01)
    keeper_02 = st.selectbox('Keeper #2', player_list, key = "2", index = starting_player)
    keeper_round_02 = st.number_input("Round You're Keeping Keeper #2", min_value = 1,max_value = 20, step = 1)
    keeper_value_02 = (round(data[data['Player Name'] == keeper_02]['Value'].reset_index(drop=True)[0] - float(round_df[round_df['Round'] == keeper_round_02]['Round Value'].reset_index(drop=True)[0]),2))
    st.write("Value Gained by Keeping", keeper_02, ":" , keeper_value_02)
    keeper_03 = st.selectbox('Keeper #3', player_list, key = "3", index = starting_player)
    keeper_round_03 = st.number_input("Round You're Keeping Keeper #3", min_value = 1,max_value = 20, step = 1)
    keeper_value_03 = (round(data[data['Player Name'] == keeper_03]['Value'].reset_index(drop=True)[0] - float(round_df[round_df['Round'] == keeper_round_03]['Round Value'].reset_index(drop=True)[0]),2))
    st.write("Value Gained by Keeping", keeper_03, ":" , keeper_value_03)    
    keeper_04 = st.selectbox('Keeper #4', player_list, key = "4", index = starting_player)
    keeper_round_04 = st.number_input("Round You're Keeping Keeper #4", min_value = 1,max_value = 20, step = 1)
    keeper_value_04 = (round(data[data['Player Name'] == keeper_04]['Value'].reset_index(drop=True)[0] - float(round_df[round_df['Round'] == keeper_round_04]['Round Value'].reset_index(drop=True)[0]),2))
    st.write("Value Gained by Keeping", keeper_04, ":" , keeper_value_04)
    keeper_05 = st.selectbox('Keeper #5', player_list, key = "5", index = starting_player)
    keeper_round_05 = st.number_input("Round You're Keeping Keeper #5", min_value = 1,max_value = 20, step = 1)
    keeper_value_05 = (round(data[data['Player Name'] == keeper_05]['Value'].reset_index(drop=True)[0] - float(round_df[round_df['Round'] == keeper_round_05]['Round Value'].reset_index(drop=True)[0]),2)) 
    st.write("Value Gained by Keeping", keeper_05, ":" , keeper_value_05)
    keeper_06 = st.selectbox('Keeper #6', player_list, key = "6", index = starting_player)
    keeper_round_06 = st.number_input("Round You're Keeping Keeper #6", min_value = 1,max_value = 20, step = 1)
    keeper_value_06 = (round(data[data['Player Name'] == keeper_06]['Value'].reset_index(drop=True)[0] - float(round_df[round_df['Round'] == keeper_round_06]['Round Value'].reset_index(drop=True)[0]),2))
    st.write("Value Gained by Keeping", keeper_06, ":" , keeper_value_06)
    keeper_07 = st.selectbox('Keeper #7', player_list, key = "7", index = starting_player)
    keeper_round_07 = st.number_input("Round You're Keeping Keeper #7", min_value = 1,max_value = 20, step = 1)
    keeper_value_07 = (round(data[data['Player Name'] == keeper_07]['Value'].reset_index(drop=True)[0] - float(round_df[round_df['Round'] == keeper_round_07]['Round Value'].reset_index(drop=True)[0]),2))
    st.write("Value Gained by Keeping", keeper_07, ":" , keeper_value_07)
    keeper_08 = st.selectbox('Keeper #8', player_list, key = "8", index = starting_player)
    keeper_round_08 = st.number_input("Round You're Keeping Keeper #8", min_value = 1,max_value = 20, step = 1)
    keeper_value_08 = (round(data[data['Player Name'] == keeper_08]['Value'].reset_index(drop=True)[0] - float(round_df[round_df['Round'] == keeper_round_08]['Round Value'].reset_index(drop=True)[0]),2))
    st.write("Value Gained by Keeping", keeper_08, ":" , keeper_value_08)
    keeper_09 = st.selectbox('Keeper #9', player_list, key = "9", index = starting_player)
    keeper_round_09 = st.number_input("Round You're Keeping Keeper #9", min_value = 1,max_value = 20, step = 1)
    keeper_value_09 = (round(data[data['Player Name'] == keeper_09]['Value'].reset_index(drop=True)[0] - float(round_df[round_df['Round'] == keeper_round_09]['Round Value'].reset_index(drop=True)[0]),2))
    st.write("Value Gained by Keeping", keeper_09, ":" , keeper_value_09)
    keeper_10 = st.selectbox('Keeper #10', player_list, key = "10", index = starting_player)
    keeper_round_10 = st.number_input("Round You're Keeping Keeper #10", min_value = 1,max_value = 20, step = 1)
    keeper_value_10 = (round(data[data['Player Name'] == keeper_10]['Value'].reset_index(drop=True)[0] - float(round_df[round_df['Round'] == keeper_round_10]['Round Value'].reset_index(drop=True)[0]),2))
    st.write("Value Gained by Keeping", keeper_10, ":" , keeper_value_10)
    
    ### Sorted Table ###
    all_keeper_players = [keeper_01, keeper_02, keeper_03, keeper_04, keeper_05, keeper_06, keeper_07, keeper_08, keeper_09, keeper_10]
    all_keeper_rounds = [keeper_round_01, keeper_round_02, keeper_round_03, keeper_round_04, keeper_round_05, keeper_round_06, keeper_round_07, keeper_round_08, keeper_round_09, keeper_round_10]
    all_keeper_values = [keeper_value_01, keeper_value_02, keeper_value_03, keeper_value_04, keeper_value_05, keeper_value_06, keeper_value_07, keeper_value_08, keeper_value_09, keeper_value_10]
    options = pd.DataFrame(
    {"Player": all_keeper_players,
     "Round Kept": all_keeper_rounds,
     "Value Gained by Keeping": all_keeper_values})
    options = options.sort_values(by = "Value Gained by Keeping", ascending = False).reset_index(drop = True)
    st.dataframe(options)

### Sidebar ###
st.sidebar.image('ffa_red.png', use_column_width=True)
st.sidebar.markdown(" ## About This App:")
st.sidebar.markdown("This app is designed to help you make decisions about what players to keep in keeper leagues! The most important thing to know is this will only work with my rankings! If you try and upload rankings that you didn't download from my website then it won't work! You can download the rankings you want to use with the links below.")

st.sidebar.markdown("## Steps:")
st.sidebar.markdown("1) Use the slider to set the number of teams in your league.")
st.sidebar.markdown("2) Go to the rankings page you want to use. All pages are linked below.")
st.sidebar.markdown("3) Click the button that says 'CSV' directly above the search bar. That will download the rankings to the 'Downloads' folder on your computer.")
st.sidebar.markdown("4) Click 'Browse files' on this page.")
st.sidebar.markdown("5) Find the rankings you just downloaded and open them.")
st.sidebar.markdown("6) Select each player you're considering keeping, plus the round pick it will cost you to keep them! The best keeper is the one that gives you the highest value gained!")
st.sidebar.markdown("7) There's a table at the bottom that shows the results, sorted from best to worst.")

st.sidebar.markdown("## Quick Links to Rankings:")
st.sidebar.info("Download PPR Rankings [Here](https://www.thefantasyfootballadvice.com/draft-package/2023-ppr-rankings/).")
st.sidebar.info("Download HPPR Rankings [Here](https://www.thefantasyfootballadvice.com/draft-package/2023-half-ppr-rankings/)")
st.sidebar.info("Download Standard Rankings [Here](https://www.thefantasyfootballadvice.com/draft-package/2023-standard-rankings/)")
st.sidebar.info("Download TE Premium Rankings [Here](https://www.thefantasyfootballadvice.com/draft-package/2023-te-premium-rankings/)")
st.sidebar.info("Download PPR SuperFlex Rankings [Here](https://www.thefantasyfootballadvice.com/draft-package/2023-ppr-superflex-rankings/)")
st.sidebar.info("Download FFPC Rankings [Here](https://www.thefantasyfootballadvice.com/draft-package/2023-ffpc-rankings/)")
st.sidebar.info("Download PPR 6 Pt Pass TD Rankings [Here](https://www.thefantasyfootballadvice.com/draft-package/2023-ppr-6-pt-pass-rankings/)")
