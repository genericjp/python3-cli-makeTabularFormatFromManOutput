"# python3-cli-makeTabularFormatFromManOutput" 
"# python3-cli-makeTabularFormatFromManOutput" 

# -*- coding:utf-8 -*-
# python makeTabularFormatFromManOutput.py

   　1. motivation
        I want to record the set value in the man output, and record Japanese as a memo.
        When converting to a table in the past, there was a problem with table and editor use.
        
        For example,
        1) English output by man, additional Japanese sentences will not be ordinary html.
        2) In the case of code, it can not be handled with the <pre> tag equivalent function.
        3) I can not easily check the history of updating.
        4) I suffer from differences in codes due to each Os-dependent i/o.
        5) I would like to use any OS-independent wrappers
    [
　　　　１．　動機
　　　　　　　manで出力したものに設定値を記録し、メモとして日本語を記録したい。
　　　　　　　以前に表に変換した時、表やエディタ使用での問題があった。

　　　　　　　例えば、
　　　　　　　１）　manの出力する英語、追加の日本語の文は、通常のhtmlにならない。
　　　　　　　２）　コードの場合は、<pre>タグ相当機能で扱えない。
　　　　　　　３）　更新の経緯を簡易にチェック出来ない。
　　　　　　　４）　osに依存するi/oによるコード上の相違点に悩される。
　　　　　　　５）　OSに依存しないラッパーがあれば使用したい。
    ]

    2. makeTabularFormatFromManOutput.py
       [man出力から表形式フォーマットを作成 py]

    3. Prerequisites for using
       [使う上での前提条件]

      1) python 3 If possible install v 3 6 or later
         However, considering when python 2 is already installed
        [
        python3 出来れば　v3 6以降をインストール。
        但し、python2がインストール済みの場合の考慮すること
        ]

          https://www python org/downloads/release/python-366/ is no problem

      2) Since clipboard operation is used, after installing python 3,
         execute the following command to acquire external library
        [
        クリップボード操作を使うのでpython3インストール後、
        外部ライブラリ取得のため、下記コマンドを行う
        ]

          >pip install pyperclip

      3) Conditions on Linux (here, Fedora fc 29) side.
        (1) Confirm that the GNOME Desktop is installed. If not, do the following operation.
            ① Install the GNOME Desktop.
                # dnf - y group install "Fedora Workstation"

            ② Register and start gnome-session.
                # cd ~
                # echo "exec / usr / bin / gnome-session" >> ~ /. Xinitrc
                # startx

            ③ After rebooting and root logon, start gnome - session.
                # startx

        (2) Open Terminal and confirm that Encodhing is default Unicode-UTF-8.
            ① Activities → Terminal
            ② Edit → Preferences screen
            ③ Select Compatibility-> Encoding: Unicode-UTF-8.
        [
        ３）　Linux（ここではVirtualBox上のFedora fc29とする）側での条件。
　　　　　　　（１）　GNOMEデスクトップがインストールされていることを確認。そうでなければ下記操作を行う。
　　　　　　　　　　　①　GNOMEデスクトップをインストールする。
　　　　　　　　　　　　　　# dnf -y group install "Fedora Workstation"

　　　　　　　　　　　②　gnome-session を登録・開始する。
　　　　　　　　　　　　　　#cd ~
　　　　　　　　　　　　　　#echo "exec /usr/bin/gnome-session" >> ~/.xinitrc
　　　　　　　　　　　　　　#startx

　　　　　　　　　　　③　再起動してrootログオン後は、　gnome-session を開始する。
　　　　　　　　　　　　　　#startx
　　　　　　　
　　　　　　　（２）　Terminalを開きEncodhingがdefaultのUnicode-UTF-8であることを確認する。
　　　　　　　　　　　①　Activities→Terminal
　　　　　　　　　　　②　Terminal→Edit→Preferences画面を開く
　　　　　　　　　　　③　Compatibility->Encoding: Unicode-UTF-8を選択するようにする。
        ]

      4) How to use,
        (1) Perform operations on Linux (here, Fedora fc 29 on VirtualBox) side.
            ① Activities → Terminal
            ② Insert the following command. (following example, httpd is the target)
                #man - no - hyphenation httpd | col - bfx
            ③ Open the Edit tab.
            ④ Edit → Select All (output screen is selected)
            ⑤ Edit → Copy as HTML (output screen is pasted on clipboard)
        
        (2) Execute the following on the Window side. 
            ① makeTabularFormatFromManOutput.py
            ② Use HTML because it is pasted on the clipboard.
        [
　　　　　　　使用方法は、
　　　　　　　　　　　　　　
　　　　　　　（１）　Linux（ここではVirtualBox上のFedora fc29とする）側での操作を行う。。
　　　　　　　　　　　①　Activities→Terminal
　　　　　　　　　　　②　以下のコマンドを入れる。（以下の例ではhttpdが対象である）
　　　　　　　　　　　　　　#man --no-hyphenation httpd | col -bfx
　　　　　　　　　　　③　Editタブを開く。
　　　　　　　　　　　④　Edit→Select All    (出力画面が選択される)
　　　　　　　　　　　⑤　Edit→Copy as HTML  （出力画面がクリップボードに貼り付けられる）
　　　　　　　
　　　　　　　（２）　Window上で下記を実行する。　　　　　　　　　　　
　　　　　　　　　　　①　makeTabularFormatFromManOutput.py
　　　　　　　　　　　②　HTMLファイルがクリップボード上に貼り付けられているので使用する。
        ]
    
 History
     2018/10/22 22:00 (JST,UTC+9h)  v1.0.0 by ShozoNamikawa
    
