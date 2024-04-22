import sqlite3

def insert_customer():
    # データベースファイルのパス
    db_path = 'local_database.db'

    # データベースへの接続
    conn = sqlite3.connect(db_path)
    
    # カーソルの作成
    cursor = conn.cursor()
    
    # データ挿入のSQLクエリ
    query = """
    INSERT INTO Customer (Customer_ID, Name, Email, Address) VALUES (?, ?, ?, ?)
    """
    data = (1000, '技術太郎', 'techtaro@techo.co.jp', '東京都新宿区')
    
    # クエリの実行
    cursor.execute(query, data)
    
    # 変更をコミット
    conn.commit()
    
    print("データが挿入されました。")
    
    # 接続のクローズ
    conn.close()

# データ挿入関数の呼び出し
insert_customer()