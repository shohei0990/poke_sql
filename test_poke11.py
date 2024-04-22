import sqlite3

def create_database_and_table():
    db_path = 'pokemon_database.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 外部キー制約を有効にする
    cursor.execute("PRAGMA foreign_keys = ON")

    # 種族テーブルの作成
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS 種族テーブル (
        種族ID INT PRIMARY KEY NOT NULL,
        種族名 CHAR NOT NULL,
        タイプ組み合わせID INT,
        HPステータスID INT,
        こうげきステータスID INT,
        ぼうぎょステータスID INT,
        とくこうステータスID INT,
        とくぼうステータスID INT,
        すばやさステータスID INT,
        特性ID INT,
        付与努力値ID INT,
        FOREIGN KEY (タイプ組み合わせID) REFERENCES タイプ組み合わせテーブル (タイプ組み合わせID),
        FOREIGN KEY (HPステータスID) REFERENCES ステータスマスタ (ステータスID),
        FOREIGN KEY (こうげきステータスID) REFERENCES ステータスマスタ (ステータスID),
        FOREIGN KEY (ぼうぎょステータスID) REFERENCES ステータスマスタ (ステータスID),
        FOREIGN KEY (とくこうステータスID) REFERENCES ステータスマスタ (ステータスID),
        FOREIGN KEY (とくぼうステータスID) REFERENCES ステータスマスタ (ステータスID),
        FOREIGN KEY (すばやさステータスID) REFERENCES ステータスマスタ (ステータスID),
        FOREIGN KEY (特性ID) REFERENCES 特性マスタ (特性ID),
        FOREIGN KEY (付与努力値ID) REFERENCES 努力値テーブル (努力値ID)
    )
    """)

    # 変更をコミット
    conn.commit()
    # 接続のクローズ
    conn.close()

    print("データベースとテーブルが作成されました。")

# データベースとテーブル作成関数の呼び出し
create_database_and_table()