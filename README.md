# experiment_template
Template for experiment on text classification.
(English var. readme is comming soon)
実験をする時のオレオレテンプレート．  
テキスト分類を例に，どこにデータを置くか，どこにconfigを書くか，どこに結果を吐くかを雛形にしています．  
ダミーのtrain.pyを使うと，それっぽい結果が/expt/以下に出力されます．  
  
もっと良いやり方あるよ，という場合はissueとかで教えてください．  

## 構造
### /data/
`/data/dataset1/dataset1.json`に学習，評価用データを詰め込んでいます．  
`dataset1.json`はjson形式で，フォーマットは以下の通りです．  
```
{
  'train': [{'text':string, 'label':int}, ...],
  'valid': [{'text':string, 'label':int}, ...],
  'test': [{'text':string, 'label':int}, ...]
}
```

### /expt/
実験ごとの設定と，結果を保存するディレクトリです．  
`/expt/test1/`には，ある設定での実験に関するコンフィグと実験結果が保存されます．  
コンフィグは`/expt/test1/config.yaml`とし，yaml形式で記述します．  
使用するデータセットや実験設定をコンフィグに記述します．  

### /src/
実験に用いるソースコードです．  
#### dataset.py
dataset.jsonを読み込んだり，語彙数やラベル数などの情報を抜き出したりします．  
### model.py
分類器のダミーコードです．    
文に0が含まれたらラベル0，それ以外は1を返します．  
update関数はダミーです．  
### handler.py
modelとdatasetを使って学習，評価を行うための処理が書かれています．  
trainとevaluateの二つが同時に存在しているのは微妙かもしれない．  
## train.py
handlerを使ってモデルを学習し，結果とモデルを吐き出すコードです．
以下のコマンドでダミーを動かせます．
```
experiment_template$ python train.py -td ../expt/test1
```
`/expt/test1/`以下に，実行した日時で`.log`と`.model`が吐き出されることを確認してください．

## お気持ち
誰も実験のお作法的なものを教えてくれないので，一つの参考に．
