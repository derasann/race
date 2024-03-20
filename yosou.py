import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title('県別予想割合と出場選手数のグラフ')
    
    # 各県の予想割合データ
    prefectures = ['Fukushima', 'Iwate', 'Yamagata', 'Kanto', 'Miyagi', 'Akita']
    percentages = [4.76, 4.76, 38.10, 23.81, 19.05, 9.52]
    
    # 各県の出場選手数データ
    players = [2, 3, 6, 2, 4, 4]  
    
    # グラフを描画
    fig, ax1 = plt.subplots()
    ax1.bar(prefectures, percentages, color='b', label='Yosou Wariai')
    ax1.set_ylabel('Wariai (%)')
    ax1.set_xlabel('Pref')
    ax1.set_title('Predicted percentage for each prefecture and Prayer number ')
    ax1.legend(loc='upper left')
    
    # 出場選手数を折れ線グラフとして描画
    ax2 = ax1.twinx()
    ax2.plot(prefectures, players, color='r', marker='o', label='Prayer number')
    ax2.set_ylabel('Player number')
    ax2.legend(loc='upper right')
    
    # グラフを表示
    st.pyplot(fig)

if __name__ == "__main__":
    main()
