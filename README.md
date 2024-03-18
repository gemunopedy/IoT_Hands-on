<img width="721" alt="スクリーンショット 2024-03-16 0 28 50" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/d5c47581-ff80-49f4-9f6c-971f18746aae"># IoTハンズオン
IoTハンズオンの手順書です。

ハンズオンの内容としては、ラズパイで温度情報を取得し、そのデータをICGWサービスを利用してGoogle Cloude上にデータ送信を行い、クラウド上で温度情報をグラフ化（可視化）するハンズオンとなっています。


<img width="50%" alt="スクリーンショット 2024-03-11 13 56 38" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/cb529843-8a72-4529-a898-6892ccf400e7">


## 1 データ収集(Rasberry Pi構築)
### 1.1 モバイルルータ設定
モバイルルータ(Aterm MR05LN)にSIM(ICM TypeS)を挿入し、APN設定等初期設定を行います。

#### 1.1.1 SIM挿入
* SIMをnanoサイズで切り出し、モバイルルータのSIM1側に挿入します。
<img width="30%" alt="IMG_1684" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/8c459a01-fccd-4854-b929-3da84b346322">
<img width="30%" alt="IMG_1685" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/55e43b4c-f110-4e26-8b28-00ad16c3816c">
<img width="30%" alt="IMG_1686" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/c0c1be82-16a1-4776-9fbc-48c4285221ca">
<br>
<br>
<br>

#### 1.1.2 APN設定
* モバイルルータのAPN設定を行います。「つなぎかたガイド」の取扱説明書に従って設定していきます。
https://www.aterm.jp/function/mr05ln/guide/lte_3g.html
<img width="50%" alt="スクリーンショット 2024-03-11 16 28 38" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/e86f2d89-84ea-425a-a2e4-da11f5d0b4d8">
<img width="50%" alt="スクリーンショット 2024-03-11 16 28 51" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/cac3bb69-2196-44e4-8790-49455673ca1c">
<br>
<br>
<br>

* APN設定は下記情報を入れてください。  
APN: mobiledata.ntt.com  
ID: mobile@icms-p.ntt.com  
PASS: protconv

* 左上にアンテナピクトとLTEが表示されればAPN設定は完了となります。
<img width="30%" alt="IMG_1687" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/adb8240f-4967-435a-b3bb-f6aa5f083f7f">
<br>

### 1.2 ラズパイ設定
OSの初期設定を行います。

#### 1.2.1 OS初期設定
* 下記URLの「手順④：ラズベリーパイの初期設定」を参考に設定していきます。  
https://sozorablog.com/raspberrypi_initial_setting/

　　**WIFI選択時に、今回使用するモバイルルータのSSIDが表示されない場合があるが、その場合は「Skip」を選択してください。**


　　**Update Softwareの選択肢は「Skip」を選択してください。**

　　**（「Next」を選択してしまうとUpdateに時間がかかってしまうため、ハンズオンではskipします）**

* モバイルルータのSSID及びPW確認方法は「情報」→「端末情報」→「無線LAN情報」を選択して表示されるプライマリ　SSID及び暗号化キーが情報となります。
* user/password設定に関しては、ICGWのリモートアクセス機能を利用して参加者同士でssh実施するので、ハンズオン内においては、簡易なuser/password指定をお願いいたします。ハンズオン終了後はOS初期化致します。

* モニタ上にデスクトップ画面が表示されればOS初期設定は完了です。
<img width="50%" alt="IMG_1568" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/147102e7-97b8-4d22-9af6-30c9be749500">

#### 1.2.2 WIFI設定
* デスクトップ右上に表示される無線マークをクリックし、該当のSSIDを選択してPWを投入してください。（1.2.1でWIFIを選択できた場合はSKIP）

#### 1.2.3 SSH/I2C有効化
* ICGWのリモートアクセス機能に必要はssh及び温度センサからのデータ収集に必要なI2C通信の有効化を行います。
* GUIでも設定可能ですが、今回はCLIのraspi-configコマンドを利用して設定します。  
`morita@raspberrypi:~ $ sudo raspi-config`
* 下図のように画面が遷移するので、「3 Inteface Options」を選択します。  
<img width="50%" alt="スクリーンショット 2024-03-05 14 59 27" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/adbf8873-d6d3-41ef-b1d3-58e6f7aa3c74">  

* 「I1 SSH」を選択します。  
<img width="50%" alt="スクリーンショット 2024-03-05 23 58 06" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/cc2d7749-7952-44a0-baa4-a8f3c3deabe8">

* 「はい」を選択します。
<img width="50%" alt="スクリーンショット 2024-03-06 0 00 16" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/f71c2c71-674e-476c-a407-39b8a107ae73">

* 下記のような画面が表示されればssh設定は完了です。  
<img width="50%" alt="スクリーンショット 2024-03-06 0 01 15" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/65c09556-a49a-4b01-9382-13122bce6c2b">

* 了解を押して、「3 Interface Options」→「I4 I2C」を選択します。  
<img width="50%" alt="スクリーンショット 2024-03-06 0 05 48" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/9bc1db5a-ed61-454c-8c1d-a770ca4b4a36">

* 「はい」を選択します。  
<img width="50%" alt="スクリーンショット 2024-03-06 0 05 57" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/ffa0b7e5-1a22-4937-9c52-e51f2cffdf01">

* 下記のような画面が表示されればI2C設定は完了です。  
<img width="50%" alt="スクリーンショット 2024-03-06 0 06 05" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/13972599-791c-4440-93c4-5672fd372a36">

* 「finish」を選択して、SSH/I2C有効化設定は完了です。
<img width="50%" alt="スクリーンショット 2024-03-06 0 06 23" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/3cac61ce-3224-4550-9709-7fbd116c5bf2">
<br>

### 1.2.4 Python仮想化環境構築(venv)  
* データ収集する際に必要なモジュールやその他ツールのインストールを今回、pipコマンドを利用して実施しますが、python仮想環境上で実施しないとラズパイではエラーが発生してしまうため、仮想環境を構築して仮想環境上で以降の作業を実施します。
* 下記コマンドにて仮想環境構築を構築して、モジュールをインストールします。「hands-on」の箇所は任意の文字列となります。ターミナルの先頭に(hands-on)のように表示されれば作業環境が仮想環境上になっています。
* 今後、スクリプトを実行する際には先頭が(hands-on)になっていることを確認した上で実行してください。  
`morita@raspberrypi:~ $ python -m venv hands-on`  
`morita@raspberrypi:~ $ source ./hands-on/bin/activate`  
`(hands-on) morita@raspberrypi:~ $ `  
`(hands-on) morita@raspberrypi:~ $ pip install RPi.GPIO`  
* 最後にSuccessfully installedと表示されれば完了です。失敗した場合は、先頭に(hands-on)がついているかどうか、WIFI接続ができているかを確認してください。

### 1.3 センサー接続
* ラズパイとサーミスタをブレッドボードを利用して接続していきます。下図のような接続をまずは目指します。  
<img width="50%" alt="IMG_1578" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/04273b0a-e8ba-4f99-aaf9-4e9270091087">  

* 用意するのはブレッドボード、40pinケーブル、GPIO拡張ボード
<img width="50%" alt="IMG_1578" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/911650b5-1e4b-42d8-91d7-a2c9c27e3170"> 

* まずはブレッドボードにGPIO拡張ボードを差し込みます。差し込み先としては、数字の1やabcといったアルファベットが上に来るようにし、GPIO拡張ボードの3V3や5VOの記載のあるピンが「1」列目に差し込みます。
* 写真上では3V3が「c」や「d」に刺さるようになっていますが、ブレッドボードの仕組み上、どちらに挿しても問題ありません。それに合わせて配線する形になります。
* ピンが見えなくなるまで押し込んでください。かなり力を入れて押し込む形になります。
<img width="30%" alt="IMG_1571" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/733efd03-84c1-48a5-9d82-5f7eb661d18c">
<img width="30%" alt="IMG_1573" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/02bc7a94-2e30-4219-9c04-45c15b89082a">

* 続いてGPIO拡張ボードとラズパイを40pinケーブルを利用して接続します。オスメスが合うように接続します。
<img width="30%" alt="IMG_1574" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/18ffb4ca-c7ea-48c4-b4ca-8cb0d0337e10">
<img width="30%" alt="IMG_1575" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/c94c2270-9579-40f9-ac24-b084a8d9924a">  
<br>

<img width="30%" alt="IMG_1576" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/56d73873-8303-4542-8968-b8828dc4e174">
<img width="30%" alt="IMG_1577" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/02b80563-07fb-478a-ad8a-26e7ca723fd7">

* ブレッドボード上にセンサーキットの部品を配線していきます。詳細内容は下記URL参照をお願いします。
(https://docs.sunfounder.com/projects/raphael-kit/ja/latest/python/2.2.2_thermistor_python.html)
<br>

* まずは以下の物品をセンサーキットから探し出して準備します。  
<img width="50%" alt="IMG_list2" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/db6555e8-365d-4eed-b454-eacea39d39c7">

* 以下を参考に配線作業を実施していきます。実物と図とで番号のずれがありますが、全く同じ場所に配線しなくても問題ありません。ブレッドボード内部の配線を意識して縦のライン/横のラインを合わせた配線ができていれば問題ありません。
* 慣習としては、電源ラインを赤線、GNDラインを黒線で配線し、電源ラインを「+縦ライン」に、GNDラインを「-縦ライン」に接続すると切り分けの時など分かりやすかったりします。ただ決まりはないので最終的には個人の好みで配線して問題ありません。
<br>
(https://start-electronics.com/electronics/tools/breadboard-point/)

<br>
<img width="50%" alt="IMG_202" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/e849707a-9ff8-427e-bb61-f53cca8031a7">
<img width="50%" alt="IMG_0" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/b335e6a4-02b7-43a6-9459-ef0ec58de618">  

* 配線後の完成イメージは以下となります。

<img width="30%" alt="IMG_1593" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/4e7e64d1-56a4-4549-8fad-35852bec4ebd">  
<img width="30%" alt="IMG_1593" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/e897429e-c7df-4a02-bb6c-ec6bbffb9db8">


### 1.4 温度情報収集
センサーキット付属のpythonスクリプトを実行してターミナル上に温度情報が表示されることを確認していきます。

* スクリプトをダウンロードして、スクリプトを実行します。

`(hands-on) morita@raspberrypi:~/raphael-kit/python $ git clone https://github.com/sunfounder/raphael-kit.git`  
`(hands-on) morita@raspberrypi:~ $ cd raphael-kit/python`  
`(hands-on) morita@raspberrypi:~/raphael-kit/python $`  
`(hands-on) morita@raspberrypi:~/raphael-kit/python $ sudo python3 2.2.2_Thermistor.py `  

* 正しく温度情報が取れている場合は、以下のような形でターミナル上に温度情報が表示されます。スクリプトを止める際には、「Ctrl+C」を実行してください。
* 温度情報が正しく表示されず、スクリプトがエラーで止まってしまう場合には、配線が正しくない可能性があります。再度配線が正しいかご確認をお願いいたします。  

<img width="50%" alt="IMG_1" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/bc11801d-9ba8-4868-8631-7c1b3a6769dd">

* 正しく温度情報が取れているようでしたら、サーミスタを直接触って温度を上げてみてターミナル上の表示が変わることを確認してみてください。

## 2 データ送信（ICGWサービス利用）
ラズパイで取得したデータをNTTComのIoT Connect Gatewayサービスを利用してGoogle Cloud上に送信していきます。

### 2.1 リモートアクセス機能確認
* データ送信を行う前にICGWの特徴的な機能の一つであるリモートアクセス機能がどういった機能なのか実際に利用して確認していきたいと思います。
* リモートアクセス機能は端末にGlobal IP Addressを付与していなくても外部から端末に対してsshやRDPが可能となる機能になります。
<img width="80%" alt="スクリーンショット 2024-03-14 13 51 40" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/8033f0e8-8ebf-4cf4-9170-a2e83dd96ff9">

#### 2.1.1 モバイルルータ設定
* リモートアクセス機能を利用して外部からsshを実施するためには、モバイルルータでのポートフォワーディング機能を設定する必要があるため、その設定を行っていきます。
* ブラウザを起動して、URLに192.168.179.1を入力してクイック設定webにアクセスします。
<img width="50%" alt="スクリーンショット 2024-03-12 14 29 23" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/77cec42c-a51d-4fdd-90fc-02a43620d01b">

* 左部の「詳細設定」→「ポートマッピング設定」をクリックします。「ポートマッピング設定 エントリ一覧」が表示されたら「追加」
<img width="30%" alt="スクリーンショット 2024-03-12 14 29 45" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/fb7703fa-ed73-4e1a-9592-5245876533fc">
<img width="30%" alt="スクリーンショット 2024-03-12 14 30 03" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/1f32d3e5-1052-4ed7-bf12-ef84c91fcc44">

* LAN側端末のIPアドレスにはラズパイに払い出されているIP Address（おそらく192.168.179.2の可能性あり。確認方法はterminal上で「ip a」コマンドを実行）を入力し、優先度を「1」として設定をクリックします。
* ポートマッピング設定 エントリ一覧上に設定したリストが表示されていれば設定完了です。
<img width="1039" alt="スクリーンショット 2024-03-12 14 31 17" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/7ab8b141-87d8-41c4-a486-694a36a738f9">
<img width="1046" alt="スクリーンショット 2024-03-12 14 31 36" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/79f437b2-e5b3-4fa9-9dc3-28db9076b041">

 #### 2.1.2 ポータル設定
* SDPFポータルから設定を実施していきます。下記URLへのアクセスをお願いいたします。 事前に設定していただいたユーザ名/パスワード及び二段階認証にてログインお願いいたします。
https://portal-jp.ecl.ntt.com/glass/login?destination=%2Fglass%2Fhome&session-expired=1

* ログインが完了したら、上部の「サービス」→「Smart Data Platform」を選択します。  
<img width="80%" alt="スクリーンショット 2024-03-12 15 37 57" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/f58af888-540f-49b1-8e71-f14f0ff7aff6">

* 「ワークスペースを選択」をクリックして、ワークスペース名「Hands-on」を選択します。
<img width="50%" alt="スクリーンショット 2024-03-12 15 38 22" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/f2aa8e10-f173-4082-86c0-6b6e95343789">
<img width="50%" alt="スクリーンショット 2024-03-12 15 38 35" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/3f297e70-80de-487f-a1dd-02588416ba05">

* 現在選択中のワークスペースに「Hands-on」が表示されていれば選択完了です。
<img width="80%" alt="スクリーンショット 2024-03-12 15 38 52" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/30054b0e-c6a6-4375-9f1e-adbdbab6dad2">

* 続いて、上部の「メニュー」を選択して、上部の「IoT」を選択します。IoTサービス一覧に画面がスクロールされますので、そこで「IoT Connect Gateway」をクリックします。
<img width="50%" alt="スクリーンショット 2024-03-12 15 39 11" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/e5040d4c-f949-4344-ae61-4e34f7cfafe3">
<img width="50%" alt="スクリーンショット 2024-03-12 15 39 19" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/33ac494a-6bf4-4aef-b386-58f2e14c41c5">

* 各SIM情報が表示されていればここからICGWの設定が可能となります。  
* ICGWの設定に関しては、各自に配布されたHSNのSIMを設定する形になります。自分のHSNはSIMカードに記載されていますのでご確認お願いいたします。
<img width="50%" alt="スクリーンショット 2024-03-12 15 39 41" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/23af5425-77e4-4a93-8256-d90fa0fd875b">
<img width="50%" alt="IMG_1684" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/ffab2b88-d6d9-4748-902f-de3f4250cf5d">

* 以降のリモートアクセス設定に関しては、以下URLのマニュアルに従って実施していきます。
* マニュアルとの差分としては、今回は接続先デバイスポートに「22」を入力してください。
* アクセス利用例ではSSHのコマンドをコピーしますが、今回は席が隣もしくは近くにいる方のラズパイにssh確認を実施しますので、相手のSIM情報及びuser/passwordを確認してコピー及びsshログインをお願いします。
* sshコマンドを実施する際は、末尾に 「-l user」という形でuser指定をお願いします。
https://sdpf.ntt.com/services/docs/icgw/tutorials/rsts/remote/index.html#about-setting

* 問題なくログインできれば、以下のようなターミナル表示となります。これでICGWのリモートアクセス機能の確認は完了となります。
<img width="80%" alt="スクリーンショット 2024-03-15 21 19 47" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/0fa6e2ce-f347-4f74-b457-55cd4b5ba770">

### 2.2 クラウドサービス接続
* ICGWのクラウドサービス接続機能を確認していきます。端末からICGWのイベントエントリーポイントに対してデータをPOST送信するだけで、今回の場合はGoogle cloudeのpub/subに対してメッセージ送信してくれる機能となります。
<img width="50%" alt="スクリーンショット 2024-03-15 22 00 02" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/ac1ad448-d598-4bbc-8c70-37217367accc">  
<img width="50%" alt="スクリーンショット 2024-03-18 14 57 24" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/e45d61a0-0508-4376-b6c8-f14f4f0b5a9c">

#### 2.2.1 Pub/Sub設定
* まずはクラウドサービス接続するために必要なGoogle cloud Pub/Subの設定を行っていきます。
* google cloud　コンソールにログインします。（ID/PWは当日お伝えします。）
<img width="30%" alt="スクリーンショット 2024-03-16 0 22 32" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/f9229c30-029f-4923-9fee-bcb9d35e7a1d">
<img width="30%" alt="スクリーンショット 2024-03-16 0 23 26" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/caf91dc3-e4d8-43b0-8039-e0c4d419d85c">

* 以下のような画面が出ればログイン完了です。（表示される画面が異なる可能性がありますが、上部の「My First Project」等が表示されていればログイン完了となります。  
<img width="50%" alt="スクリーンショット 2024-03-16 0 25 48" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/cf0c2c55-c798-4e69-86fd-b34beb256059">

* Pub/Subの設定を行っていきます。Pub/Subについては下記URL等参照お願いします。  
https://laboratory.kiyono-co.jp/69/gcp/

* まずは、トピックの作成からになります。メニューから「Pub/Sub」を選択します。
<img width="50%" alt="スクリーンショット 2024-03-16 0 27 09" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/698f5fdb-00c2-40c4-9634-48bf4aff3e5f">

* 上部の「トピックを作成」をクリックします。
<img width="50%" alt="スクリーンショット 2024-03-16 0 27 32" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/446ab45c-43d6-4c97-b323-4cf066fe98cd">

* トピックIDに自分が作成したものと分かる形で入力し、その他は変更なしで「作成」をクリックします。
<img width="50%" alt="スクリーンショット 2024-03-16 0 28 06" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/960fb831-a85a-46ce-b9e8-4ac12e76b81a">

* トピックの一覧に先ほど作成したトピックが表示されていることを確認して、作成したトピックをクリックします。自動で生成されているサブスクリプションを確認します。
<img width="50%" alt="スクリーンショット 2024-03-16 0 28 50" src="https://github.com/gemunopedy/IoT_Hands-on/assets/1537206/c5db9086-f468-478e-b5a4-032a4fe2ea6f">

#### 2.2.2 IAM設定
