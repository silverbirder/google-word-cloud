# google-word-cloud

googleのマイアクティビティから、検索履歴を月別にwordCloudで表示する

例えば、2019年1月のGoogle検索履歴では、golangとvueにハマっていた  
![output](https://res.cloudinary.com/silverbirder/image/upload/v1551595196/google-word-cloud/%E3%83%9E%E3%82%A4%E3%82%A2%E3%82%AF%E3%83%86%E3%82%A3%E3%83%92%E3%82%99%E3%83%86%E3%82%A3.json.201901.json.txt.png)

# どうやって使う？

1. Takeoutファイルを取得する

1.1. https://takeout.google.comにアクセスする  

1.2. ダウンロードするファイルを「マイアクティビティ」のみにする。  

※ 出力形式をjsonにする  
※ マイアクティビティのコンテンツは「検索」のみにする。
検索結果が含まれているコンテンツなら他を選択しても良い.   
・Gmail, Google Apps, YouTube, ドライブ, マップ, 画像検索, 検索, 動画検索, etc  

1.3. アーカイブを作成し、ローカルにダウンロードする  

1.4. ダウンロードしたファイルをTakeoutのフォルダにリネームし、このリポジトリのルートディレクトリに保存する。  

2. コマンドを実行する (python 3.7の環境)

※ main.pyにあるROOT_PATHを、自身の環境に合わせて下さい。

```
$ pip install -r requirements.txt
$ python main.py
```

Takeout以下のフォルダにpng画像が作成されている。
