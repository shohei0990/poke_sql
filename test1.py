import sqlite3

def create_customer_table():
    # データベースファイルのパス
    db_path = 'local_database.db'

    # データベースへの接続（ファイルが存在しない場合は新規作成される）
    conn = sqlite3.connect(db_path)
    
    # カーソルの作成
    cursor = conn.cursor()
    
    # テーブル作成のSQLクエリ
    sql_query = """
    CREATE TABLE IF NOT EXISTS Customer (
        Customer_ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        Address TEXT NOT NULL
    )
    """
    # クエリの実行
    cursor.execute(sql_query)
    
    # 変更をコミット
    conn.commit()
    
    # 接続のクローズ
    conn.close()
    
    print("テーブルが作成され、データベースファイルが保存されました。")

# テーブル作成関数の呼び出し
create_customer_table()