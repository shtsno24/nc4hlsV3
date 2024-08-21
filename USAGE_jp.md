# nc4hlsV2の使い方

## 始めに

nc4hlsはtf.kerasで記述されたモデルをC++コードに変換するツールです．
このC++コードは高位合成(HLS)を用いることでFPGA向けのHDLへ変換することができます．
このツールで学習することはできないので，その際はtf.kerasを使ってください．

## 対応する演算と注意事項

丸め等の機能はないので，出力サイズについては余りが発生しないようにフィルタのサイズ・スライド量等を設定してください．
1D系，3D系の操作は未対応です．LSTM，RNN等の時系列系の操作も未対応です．

|演算|対応|備考|
|:---:|:---:|:---|
|Add|✅*|入力形状はすべてが完全に一致する必要|
|AveragePooling2D|✅||
|GlobalAveragePooling2D|✅*|AveragePooling2Dに変換|
|BatchNormalization|✅||
|Dense|✅||
|Conv2D|✅*|dilation_rateは(1,1)固定|
|SeparableConv2D|✅*|dilation_rateは1固定，depth_multiplierは1固定, DepthwiseConv2D + PointwiseConv(Conv2D:1x1)に変換|
|DepthwiseConv2D|✅*|dilation_rateは1固定，depth_multiplierは1固定|
|MaxPooling2D|✅*|padding=validのみ|
|GlobalMaxPooling2D|✅*|MaxPooling2Dに変換|
|PointwiseConv|✅*|Conv2Dと同じ|
|LeakyReLU|✅||
|ReLU|✅*|negative_slopeは0.0固定, thresholdも0.0固定|
|UpSampling2D|✅*|interpolationは'nearest'のみ|
|ZeroPadding2D|✅||
|Activation|✅*|ReLUのみ|

Dropout，SpatialDropout1D，SpatialDropout2D，flattenに関してはモデル変換時に削除されます．

## もう少し詳しく

### データ形状

回路内部において，データはNHWCの1Dデータとして保持されます．

### 回路構造

* 計算パイプライン群をFPGAのロジック側に、データ並び替えをDRAM+CPUで行います。
  * モデル変換時にデータ幅と並列数を指定できます(制約あり)。
  * 最大512bit幅のパイプラインを複数実行することで計算速度を確保します。

### 実行の流れ

1. データをロード
2. レイヤに合わせて、CPU上でデータを並び替え
3. DMA転送でFPGAへデータを流す
4. レイヤに合わせてパイプラインを選択し計算実行
5. 計算結果をDMAでCPUから書き戻す

### 変換時に生成されるファイル

変換後，以下のようなフォルダが生成されます．

(root)  
|-cpu(CPU実行時に使うファイル)  
|-xilinx(Xilinx社製高位合成コンパイラで使うファイル)  
|-pynq(PYNQ環境下で使うファイル)  
`-log(ログ)  

### 変換手順

1. kerasのh5ファイルを読み込み(モデルと重みデータ)
2. レイヤ変換等を実行
3. メモリ・レジスタ割り付けを実行
4. 必要なC++コード・バイナリコードを生成orコピー
5. (CPU実行時)共有ライブラリを生成
6. (HLS実行時)HLSコンパイラに生成物を入れ，IPを生成
