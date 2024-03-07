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
必要モジュールのインストール。最後にSuccessfully installedと表示されれば完了<br>
`(hands-on) morita@raspberrypi:~/raphael-kit/python $ pip install RPi.GPIO`

### 1.3 センサー接続
Rasberry Piとサーミスタをブレッドボードを利用して接続。まずはブレッドボードとRasberry Piを接続。接続完了後のイメージは下写真<br>
![IMG_1578](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/04273b0a-e8ba-4f99-aaf9-4e9270091087)
<br>
<br>
用意するのはブレッドボード、40pinケーブル、GPIO拡張ボード
![IMG_1570](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/911650b5-1e4b-42d8-91d7-a2c9c27e3170)
<br>
ブレッドボードとGPIO拡張ボードとの接続を行う。3V3と記載されているpinがブレッドボードの1cに入るように挿入する。だいぶ強く押し込む必要あり。<br>
ピンが見えなくなるまで押し込めたら完了。（※2枚目の写真上は1dに刺さっているように見えるが、別撮りのため1cに刺して問題なし）
![IMG_1571](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/733efd03-84c1-48a5-9d82-5f7eb661d18c)
<br>
![IMG_1573](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/02bc7a94-2e30-4219-9c04-45c15b89082a)
<br>
続いてGPIO拡張ボードと40pinケーブルを接続。オスメスが合うように接続<br>
![IMG_1574](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/18ffb4ca-c7ea-48c4-b4ca-8cb0d0337e10)
<br>
![IMG_1575](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/c94c2270-9579-40f9-ac24-b084a8d9924a)
<br>
次にラズパイと40pinケーブルを接続。これでラズパイとブレッドボードの接続は完了<br>
![IMG_1576](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/56d73873-8303-4542-8968-b8828dc4e174)
<br>
![IMG_1577](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/02b80563-07fb-478a-ad8a-26e7ca723fd7)
<br>
<br>
ブレッドーボード上にサーミスタ等を配線していく<br>
(https://docs.sunfounder.com/projects/raphael-kit/ja/latest/python/2.2.2_thermistor_python.html)
<br>
下図リストの物品を準備<br>
![list_2](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/db6555e8-365d-4eed-b454-eacea39d39c7)
<br>
下図を参考に配線作業を実施。現物と図とで番号にずれがあるので正確に同じ場所に配線することはできないが、ブレッドボードないの配線を意識して縦のライン/横のラインが同じであれば問題なし<br>
![image202](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/e849707a-9ff8-427e-bb61-f53cca8031a7)
<br>
<img width="674" alt="スクリーンショット 2024-03-07 10 05 16" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/b335e6a4-02b7-43a6-9459-ef0ec58de618">
<br>
完成した際のイメージ<br>
![IMG_1593](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/4e7e64d1-56a4-4549-8fad-35852bec4ebd)
<br>
![IMG_1595](https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/e897429e-c7df-4a02-bb6c-ec6bbffb9db8)
<br>

### 1.4 温度情報収集





