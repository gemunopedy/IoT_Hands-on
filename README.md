# IoTハンズオン
IoTハンズオンの手順書です。Raspberry Pi OSの起動が完了し、インターネット接続及びターミナル起動が完了している状態からの手順となります。- 

## 1.データ収集(Rasberry Pi構築)
### 1.1 SSH/I2C有効化
raspi-configコマンドを使用して機能を有効化<br>
 `morita@raspberrypi:~ $ sudo raspi-config`<br><br>
「3 Inteface Options」を選択<br>
<img width="1076" alt="スクリーンショット 2024-03-05 14 59 27" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/adbf8873-d6d3-41ef-b1d3-58e6f7aa3c74">
<br>
「I1 SSH」を選択<br>
<img width="1079" alt="スクリーンショット 2024-03-05 23 58 06" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/cc2d7749-7952-44a0-baa4-a8f3c3deabe8">
<br>
「はい」を選択<br>
<img width="542" alt="スクリーンショット 2024-03-06 0 00 16" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/f71c2c71-674e-476c-a407-39b8a107ae73">
<br>
下記のような画面が表示されればssh設定は完了<br>
<img width="537" alt="スクリーンショット 2024-03-06 0 01 15" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/65c09556-a49a-4b01-9382-13122bce6c2b">
<br>
<br>
続いてIC2の有効化。先ほどと同様に「3 Interface Options」を選択し、「I4 I2C」を選択<br>
<img width="1078" alt="スクリーンショット 2024-03-06 0 05 48" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/9bc1db5a-ed61-454c-8c1d-a770ca4b4a36">
<br>
「はい」を選択<br>
<img width="540" alt="スクリーンショット 2024-03-06 0 05 57" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/ffa0b7e5-1a22-4937-9c52-e51f2cffdf01">
<br>
下記のような画面が表示されればI2C設定は完了<br>
<img width="539" alt="スクリーンショット 2024-03-06 0 06 05" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/13972599-791c-4440-93c4-5672fd372a36">
<br>
以上でSSH/I2Cの設定は完了したので、「finish」を選択<br>
<img width="1078" alt="スクリーンショット 2024-03-06 0 06 23" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/3cac61ce-3224-4550-9709-7fbd116c5bf2">
<br>

### 1.2 Python仮想化環境構築(venv)  
データ収集する際に必要なモジュールやその他ツールのインストール(pip install)をする際、仮想環境で実施しないとRasberry Pi OSだとエラーが発生するため、仮想環境を構築し、今後は仮想環境上で作業を実施する<br>
<br>
下記コマンドにて仮想環境構築。「hands-on」の箇所は任意の文字で問題なし。ターミナルの先頭に(hands-on)のように表示されれば作業環境が仮想環境上になっているので問題なし<br>
`morita@raspberrypi:~ $ python -m venv hands-on`  
`morita@raspberrypi:~ $ source ./hands-on/bin/activate`  
`(hands-on) morita@raspberrypi:~ $ `  
<br>






