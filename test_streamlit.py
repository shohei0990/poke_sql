import sqlite3
import pandas as pd
import streamlit as st

# データベースからデータを読み込む関数
def load_data():
    db_path = 'pokemon_database.db'
    conn = sqlite3.connect(db_path)

    # 種族テーブルを読み込む
    query_species = "SELECT * FROM 種族テーブル"
    species_df = pd.read_sql_query(query_species, conn)

    # タイプ組み合わせテーブルを読み込む
    query_types = "SELECT * FROM タイプ組み合わせテーブル"
    types_df = pd.read_sql_query(query_types, conn)

    # データベースのクローズ
    conn.close()

    return species_df, types_df


# データベースからデータを読み込み、結合する関数
def load_and_merge_data():
    db_path = 'pokemon_database.db'
    conn = sqlite3.connect(db_path)
    query = """
    SELECT 種族テーブル.種族ID, 種族テーブル.種族名, 種族テーブル.タイプ組み合わせID, 
            タイプ組み合わせテーブル.タイプ1名称 AS タイプ1, 
            タイプ組み合わせテーブル.タイプ2名称 AS タイプ2, 
            種族テーブル.特性ID
    FROM 種族テーブル
    JOIN タイプ組み合わせテーブル ON 種族テーブル.タイプ組み合わせID = タイプ組み合わせテーブル.タイプ組み合わせID
    """
    merged_df = pd.read_sql_query(query, conn)
    conn.close()
    return merged_df

# Streamlitアプリのメイン関数
def main():
    st.title('ポケモンデータベース')

    # データの読み込み
    species_df, types_df = load_data()

    # 種族テーブルを表示
    st.header('種族テーブル')
    st.dataframe(species_df)

    # タイプ組み合わせテーブルを表示
    st.header('タイプ組み合わせテーブル')
    st.dataframe(types_df)


    # データの読み込みと結合
    merged_df = load_and_merge_data()

    # 結合したデータフレームを表示
    st.header('結合されたデータフレーム')
    st.dataframe(merged_df)

if __name__ == "__main__":
    main()

