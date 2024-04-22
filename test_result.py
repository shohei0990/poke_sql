
import sqlite3

def fetch_customers():
    # データベースファイルのパス
    db_path = 'pokemon_database.db'

    # データベースへの接続
    conn = sqlite3.connect(db_path)
    
    # カーソルの作成
    cursor = conn.cursor()
    
    # データの取得クエリ
    query = "SELECT * FROM タイプ組み合わせテーブル"
    
    # クエリの実行
    cursor.execute(query)
    
    # カラム名の取得
    columns = [description[0] for description in cursor.description]
    print("カラム名:", columns)
    
    # 結果の取得
    rows = cursor.fetchall()
    
    # 結果の表示
    for row in rows:
        print(row)

    print("テーブル参照完了")
    
    # 接続のクローズ
    conn.close()

# データ取得関数の呼び出し
fetch_customers()

