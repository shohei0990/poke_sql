import sqlite3

def create_type_combination_table():
    db_path = 'pokemon_database.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # タイプ組み合わせテーブルの作成
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS タイプ組み合わせテーブル (
        タイプ組み合わせID INT PRIMARY KEY NOT NULL,
        タイプ1名称 TEXT,
        タイプ2名称 TEXT,
        ノーマルタイプダメージ率 REAL,
        ほのおタイプダメージ率 REAL,
        みずタイプダメージ率 REAL,
        くさタイプダメージ率 REAL,
        でんきタイプダメージ率 REAL,
        じめんタイプダメージ率 REAL,
        いわタイプダメージ率 REAL,
        どくタイプダメージ率 REAL,
        はがねタイプダメージ率 REAL,
        ひこうタイプダメージ率 REAL
    );
    """)

    # 変更をコミット
    conn.commit()
    # 接続のクローズ
    conn.close()

    print("タイプ組み合わせテーブルが作成されました。")

# テーブル作成関数の呼び出し
create_type_combination_table()