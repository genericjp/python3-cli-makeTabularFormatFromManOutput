# -*- coding:utf-8 -*-
# python makeTabularFormatFromManOutput.py

"""
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


    Problem 1:
    
    1) There is a problem with libreoffice.
        (1) libreoffice deletes border = "1" and the table line disappears.
            → It is necessary to add it before displaying the web.
                <Table ... style = "page-break-before: always" border = "1">
                
        (2) If libreoffice contains Japanese, 
            it becomes a paragraph line by line, 
            and it becomes constitution with blank line.
                → Configure the cell as one paragraph.
                
    2) Perform the following procedure.
        (1) Create man HTML.
                MakeTabularFormatFromManOutput.py
                
        (2) Addition of Japanese.
            ① Construct lines by sentence and do google translation.
            ② Since alphanumeric character strings may become illegal, 
              resume to en base.
            
            ③ Convert statement tone.
                PoliteWordToAssertiveOne.py
                
            ④ Review tone and so on to be a reasonable translation.
            ⑤ Insert Japanese as empty cell in libreoffice as MS P Mincho.
            Ⅰ The original English letter continues Liberation Serf.
            
        (3) Fix man HTML with notepad ++ as follows.
            ① Add border = "1".
            ② → unix Make line breaks.
            ③ Replace with re base.
                I Configure the cell as one paragraph.
                Ⅱ Replace line end with HTML line break.
                    </ P> \ n \ s + <p [^>] +> → </ br>
            ④ → windows resume to line feed.
[
　　問題点１：

　　１）　libreofficeに問題がある。
　　　　（１）　libreofficeがborder="1" を削除して、　表罫線が消えてしまう。
　　　　　　　　　→　web表示前に追加が必要。
　　　　　　　<table ...　style="page-break-before: always" border="1">

　　　　（２）　libreofficeが日本語を含むと行ごとに段落としてしまい、空行付の構成となる。
　　　　　　　　　→　セルを一段落で構成する。

　　２）　次の手順を行う。
　　　　（１） man HTML を作成。
　　　　　　　　　makeTabularFormatFromManOutput.py

　　　　（２）　日本語の追記。
　　　　　　①　文単位に行を構成し、google翻訳を行う。
　　　　　　②　英数字文字列は不正になることがあるので、enベースに戻す。
　　　　　　③　語調の変換を行う。
　　　　　　　　　politeWordToAssertiveOne.py
　
　　　　　　④　妥当な翻訳になるように語調も含めレビューする。
　　　　　　⑤　libreofficeで表の空セルにMS　P明朝として日本語を挿入する。
　　　　　　　　ⅰ　元の英文はLiberation Serfを継続させる。

　　　　（３）　notepad++でman HTMLを下記手順で修正する。
　　　　　　①　border="1"　を追加する。
　　　　　　②　→ unix 改行とする。
　　　　　　③　正規表現ベースで置換する。
　　　　　　　　　ⅰ　セルを一段落で構成する。
　　　　　　　　　ⅱ　行末はHTML改行に置き換える。
　　　　　　　　　　　</p>\n\s+<p[^>]+> → </br>

　　　　　　④　→　windows　改行に戻す。
]

 History
    2018/10/24 2:25 (JST,UTC+9h)  v1.0.1 add Problem 1 procedure: by ShozoNamikawa
    2018/10/22 22:00 (JST,UTC+9h)  v1.0.0 by ShozoNamikawa
    
"""

import os
import re

import pyperclip


class ClipBoard():
    """
        read the text content of the current clipboard,
        or paste the new text contents and update the contents
        [現在のクリップボードのテキスト内容を読む、ないし新たなテキスト内容を貼り付け内容を更新する]
    """
    
    def get(self):
        """
            Contents of current clipboard\
            [現在クリップボードの内容]
        """
        return (str(pyperclip.paste()))
    
    def set(self, past_text):
        """
            Rewrite the clipboard to this content
            [この内容に、クリップボードを書き換える]
        """
        pyperclip.copy(past_text)
        return (past_text)


class MakeHtml:
    '''
        Convert to HTML format.
        [HTMLを作成する]
    '''
    
    def __init__(self):
        pass
    
    def docHead(self):
        '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title></title>
    <meta name="generator" content="LibreOffice 5.3.2.2 (Windows)"/>
    <meta name="author" content=""/>
    <meta name="created" content="00:00:00"/>
</head>
<body lang="ja-JP" dir="ltr">
<table width="1500" cellpadding="4" cellspacing="0" style="page-break-before: always" border="1">
    <col width="7%">
    <col width="9%">
    <col width="2%">
    <col width="2%">
    <col width="77%">
    <tr>
        <td width="7%" style="background: transparent" style="border-top: 1px solid #808080; border-bottom: 1px solid #808080; border-left: 1px solid #808080; border-right: 1px solid #808080; padding: 0.11cm"><p align="center">
            <font face="Liberation Sans, sans-serif"><font size="3" style="font-size: 11pt"><span lang="en-US"><b>section</b></span></font></font></p>
        </td>
        <td width="9%" style="background: transparent" style="border-top: 1px solid #808080; border-bottom: 1px solid #808080; border-left: 1px solid #808080; border-right: 1px solid #808080; padding: 0.11cm"><p align="center">
            <font face="Liberation Sans, sans-serif"><font size="3" style="font-size: 11pt"><span lang="en-US"><b>descriptor</b></span></font></font></p>
        </td>
        <td width="2%" style="background: transparent" style="border-top: 1px solid #808080; border-bottom: 1px solid #808080; border-left: 1px solid #808080; border-right: 1px solid #808080; padding: 0.11cm"><p align="center">
            <font face="Liberation Sans, sans-serif"><font size="3" style="font-size: 11pt"><span lang="en-US"><b>setting</b></span></font></font></p>
        </td>
        <td width="2%" style="background: transparent" style="border-top: 1px solid #808080; border-bottom: 1px solid #808080; border-left: 1px solid #808080; border-right: 1px solid #808080; padding: 0.11cm"><p align="center">
            <font face="Liberation Sans, sans-serif"><font size="3" style="font-size: 11pt"><span lang="en-US"><b>value</b></span></font></font></p>
        </td>
        <td width="77%" style="background: transparent" style="border-top: 1px solid #808080; border-bottom: 1px solid #808080; border-left: 1px solid #808080; border-right: 1px solid #808080; padding: 0.11cm"><p align="center">
            <font face="Liberation Sans, sans-serif"><font size="3" style="font-size: 11pt"><span lang="en-US"><b>description</b></span></font></font></p>
        </td>
    </tr>
        '''
        pass
    
    def getHead(self):
        return(self.docHead.__doc__)
    
    def docRow(self):
        '''
    <tr valign="top">
        <td width="7%" style="background: transparent" style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.11cm; padding-bottom: 0.11cm; padding-left: 0.11cm; padding-right: 0cm"><p align="left">
            <font face="Liberation Sans, sans-serif"><font size="3" style="font-size: 11pt"><span lang="en-US">td_0</span></font></font></p>
        </td>
        <td width="9%" style="background: transparent" style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.11cm; padding-bottom: 0.11cm; padding-left: 0.11cm; padding-right: 0cm"><p align="left">
            <font face="Liberation Sans, sans-serif"><font size="3" style="font-size: 11pt"><span lang="en-US">td_1</span></font></font></p>
        </td>
        <td width="2%" style="background: transparent" style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.11cm; padding-bottom: 0.11cm; padding-left: 0.11cm; padding-right: 0cm"><p align="left">
            <font face="Liberation Sans, sans-serif"><font size="3" style="font-size: 11pt"><span lang="en-US">td_2</span></font></font></p>
        </td>
        <td width="2%" style="background: transparent" style="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: none; padding-top: 0.11cm; padding-bottom: 0.11cm; padding-left: 0.11cm; padding-right: 0cm"><p align="left">
            <font face="Liberation Sans, sans-serif"><font size="3" style="font-size: 11pt"><span lang="en-US">td_3</span></font></font></p>
        </td>
        <td width="77%" style="background: transparent" style="border: 1px solid #000000; padding: 0.11cm"><p align="left">
            <font face="Liberation Sans, sans-serif"><font size="3" style="font-size: 11pt"><span lang="en-US">td_4</span></font></font></p>
        </td>
    </tr>
        '''
        pass
    
    def getRow(self):
        return(self.docRow.__doc__)
    
    def docTail(self):
        '''
</table>
<p><br/>
<br/>

</p>
</body>
</html>
        '''
        pass
    
    def getTail(self):
        return(self.docTail.__doc__)
    
class HoldRow():
    """
        hold row in table.
        [行出力管理を行う。]
    """
    
    def __init__(self, ):
        """
            Initialize line output contorol
            [行出力管理の初期化行う]
        """
        
        # debug option
        self.debug = False

        # used variable
        self.stack = ''             # hold stack
        
        # used class
        self.make_html = MakeHtml()
        
        # take head
        self.stack = self.make_html.getHead()
                
        # list column definition
        self.c_sec = 0              # section
        self.c_tor = 1              # descriptor
        self.c_set = 2              # setting
        self.c_val = 3              # value
        self.c_ion = 4              # description

        # fixd list style
        self.td_c = ['', '', '', '', '']# define clear data
        
        # hold list
        self.h_row = []             # hold row
        self.h_ion = []             # hold diescription
        self.h_stack = []           # hold stack
    
    def putRow(self, row):
        """
            do line output.
            [行出力を行う。]
        """
        
        if self.debug:
            print(row)
        
        # embed column values
        tr = self.make_html.getRow()
        tr= tr.replace('td_0', row[0])
        tr= tr.replace('td_1', row[1])
        tr= tr.replace('td_2', row[2])
        tr= tr.replace('td_3', row[3])
        tr= tr.replace('td_4', row[4])
        self.stack += tr

    
    def holdSection(self, section):
        """
            init row and set section
            [行管理を初期化しsectionを設定]
        """
        
        self.h_row = self.td_c
        self.h_row[self.c_sec] = section
        self.h_row[self.c_tor] = ''
        self.h_row[self.c_ion] = ''
    
    def holdDescriptor(self, descriptor):
        """
            set descriptor and init diescription
            [descriptorを設定しdiescriptionを初期化する]
        """
        
        self.h_row[self.c_tor] = descriptor
        self.h_ion = []
    
    def holdDescription(self, description):
        """
            Set description as appendding
            [descriptionを追加して設定]
        """
        
        self.h_ion.append(description + " ")
    
    def putDescription(self):
        """
            ｌine output with description
            [descriptionを1のrowとして行出力する]
        """
        
        self.h_row[self.c_ion] = ''
        for description in self.h_ion:
            self.h_row[self.c_ion] += description + '' + "<br/>"
        self.putRow(self.h_row)
        self.h_ion = []
        self.h_row[self.c_ion] = ''

        # empty line
        self.h_row[self.c_ion] = '' + "<br/>"
        self.putRow(self.h_row)
    
    def putCategoryRaw(self, category):
        """
            ｌine output with specified contents
            [指定された内容で行出力する]
        """
        
        h_row = self.h_row
        h_row[self.c_tor] = category
        h_row[self.c_ion] = '' + "<br/>"
        self.putRow(h_row)
        self.h_row[self.c_tor] = ''
        self.h_row[self.c_ion] = ''

    
    def putWithoutHoldRaw(self, h_row):
        """
            ｌine output with specified contents
            [指定された内容で行出力する]
        """
        
        h_row[self.c_ion] += '' + "<br/>"
        self.putRow(h_row)
        h_row[self.c_ion] = ''

    def getStack(self):
        """
            get the stack
            [スタックを求める]
        """
        
        # take tail
        self.stack += self.make_html.getTail()
        
        return(self.stack)


class ParseManOut():
    """
        parse man output copyHTML.
        [copyHTMLしたman出力を解釈する。]
    """
    
    def __init__(self):
        """
            define of parse.
            [解析の定義。]
        """
        
        # debug option
        self.debug = False
        
        # define table
        self.th_l = [                   # define table head
                "section",
                "descriptor",
                "setting",
                "value",
                "description"
                ]
        
        # used variable
        self.row = ''                   #
        self.paste = ''                 #
        
        # used dict
        self.dict_s = {}                # section description start column
        self.dict_h = {}                # leading space length hierarchy
        self.dict_l = {}                # line_no:leading space length
        self.dict_p = {}                # paragraph
        
        # used hold section name
        self.sect_c = ''                # current section
        self.sect_n = ''                # next section
        
        # used class
        self.clip_board = ClipBoard()
        self.hold_row = HoldRow()
        
        # read clipping content of man output copyHTML at startup.
        self.clip_str = self.clip_board.get()
        
        # split clipbord content of man output copyHTML to each line.
        self.man_list = self.clip_str.splitlines()      #  lines
        self.man_l = len(self.man_list)                 #  lines length
        
        # positioning
        self.head_p = 1                 # header position
        self.ss_b_p = 3                 # begin sections position
        self.ss_e_p = self.man_l - 4    # end sections position
        self.tail_p = self.man_l - 3    # tailer position
        
        # used section position
        self.se_b_p = self.ss_b_p       # begin each section position
        self.se_e_p = 0                 # end each section position
        
        # used id constant
        # which section description start column to apply?
        self.d_column = 0               # description start column
        
        # specific section processing
        self.d_sect = 'NAME'            # section as the basis of the column
        self.s_opt = 'OPTIONS'          # section OPTIONS
        self.s_env = 'ENVIRONMENT'      # section ENVIRONMENT
        self.s_fil = 'FILES'            # section FILES
        
        # category ID of header and tail?
        self.head_pse = "HEAD"          # header pseudo section
        self.tail_pse = "TAIL"          # tail pseudo section
        
    def putWarning(self,args):
        """
            Warning guidance
            [警告ガイダンス]
        """
        
        print(args)
        
    def putDebug(self,args):
        """
            Debug guidance
            [デバッグガイダンス]
        """
        
        if self.debug:
            print(args)
    
    def isPattern(self, pattern, line_str):
        """
            pattern match
            must be (...)
            [()を指定したパターンマッチ]
        """
        
        m = re.search(pattern, line_str)
        if (m):
            t = m.groups(0)
            t_str = str(t[0])
            # t_str = t_str.strip()
            return(t_str)
        else:
            return (False)
    
    def isOption(self, line_str):
        """
            recognition of option description
            [オプション記述の認識]
        """
        
        # descriptions continue in options?
        top_p1 = line_str[0:self.d_column + 1]
        opt = self.isPattern('^(-.+)\s+[A-Z]$', top_p1)
        if opt:
            return(opt)
        
        # include () and descriptions continue in options?
        opt = self.isPattern('^(-.+)\s+\(', line_str)
        if opt:
            return(opt)
        else:
            # option only
            return(line_str)
    
    def headAndTail(self, pse, line_str):
        """
            process header and tail lines.
            [ヘッダーとテール行の処理を行う。]
        """
        
        t_0 = self.isPattern('^(\S+|\S+\s\S+|\S+\s\S+\s\S+)\s\s\s', line_str)
        if not t_0:
            return (False)
        
        t_1 = self.isPattern('\s\s\s(\S.*)\s\s\s', line_str)
        if not t_1:
            return (False)
        
        t_4 = self.isPattern('\s\s\s(\S*)$', line_str)
        if not t_4:
            return (False)
        
        self.hold_row.putWithoutHoldRaw([t_0, t_1, '', '', t_4,])
        if pse == self.head_pse:
            self.hold_row.putWithoutHoldRaw([t_0, '', '', '', '',])
        return(True)
    
    def sectionEach(self, section):
        """
            each section process.
            [各section処理]
        """
        
        #self.debug:
        self.putDebug(self.dict_s)
        self.putDebug(self.dict_h)
        self.putDebug(self.dict_l)
        
        # which section description start column to apply?
        self.d_column = int(self.dict_s[self.d_sect])
        self.dict_p = {}
        
        for line_item in enumerate(self.man_list):
            line_no = line_item[0]
            line_str = line_item[1]
            
            # exclude previous sections
            if line_no < self.se_b_p :
                continue
            
            if line_no > self.se_e_p:
                return(True)
            
            # section
            if line_no == self.se_b_p :
                self.hold_row.holdSection(section)
                continue
            
            # retrieve the contents of the current line except end line
            line_str = line_str.strip()
            sp_lead = int(self.dict_l[str(line_no)])
            
            # enpty line
            if sp_lead == 0:
                self.hold_row.putDescription()
                self.dict_p = {}
                continue
            
            # category?
            elif sp_lead < self.d_column:
                self.hold_row.putCategoryRaw(line_str)
                continue
            
            # is it the same column as the starting column?
            # standard description column
            if sp_lead == self.d_column:
                # is it an option script?
                if section == self.s_opt:   # OPTIONS
                    # start with '-'?
                    opt = self.isPattern('^(-)', line_str)
                    if opt:
                        opt = self.isOption(line_str)

                        self.dict_p["yes"] = line_str
                        # line_str = str(line_str)
                        self.hold_row.holdDescriptor(opt)

                        # is description continued?
                        line_len = len(line_str)
                        opt_len = len(opt)
                        if line_len == opt_len:
                            continue
                        ion_str = line_str[opt_len : line_len - 1]
                        ion_str = ion_str.strip()
                        self.hold_row.holdDescription(ion_str)
                        continue
                
                # environment variable format?
                if section == self.s_env:  # ENVIRONMENT
                    opt = self.isPattern('^([A-Z][A-Z_]*[A-Z][, ]*[A-Z][A-Z_]*[A-Z]).*$', line_str)
                    if opt:
                        self.hold_row.holdDescriptor(opt)
                        
                        # is description continued?
                        line_len = len(line_str)
                        opt_len = len(opt)
                        if line_len == opt_len:
                            continue
                        ion_str = line_str[opt_len : line_len - 1]
                        ion_str = ion_str.strip()
                        self.hold_row.holdDescription(ion_str)
                        continue
            
            if "yes" in self.dict_p:
                self.hold_row.holdDescription(line_str)
                continue
            
            # as include 3 consecutive blanks, replace space with & nbsp ;
            d = self.isPattern('(\s{3})', line_str)
            if (d):
                line_str = line_str.replace(' ', '&nbsp;')
            
            # padding leading space
            if sp_lead == self.d_column + 4 or sp_lead > self.d_column * 2:
                line_str = '&nbsp;' * (sp_lead - self.d_column) + line_str
            if sp_lead == self.d_column * 2 and section == self.s_fil:
                line_str = '&nbsp;' * (sp_lead - self.d_column) + line_str
            self.hold_row.holdDescription(line_str)
        return(True)
    
    def sections(self):
        """
            section process.(1st pass)
            [section処理(1st pass)]
        """
        
        # section name
        line_no = self.se_b_p
        self.sect_c = self.man_list[line_no].strip()
        
        for line_item in enumerate(self.man_list):
            line_no = line_item[0]
            line_str = line_item[1]
            
            # skip sections and previous lines
            if line_no <= self.se_b_p:
                continue
            
            # retrieve the contents of the current line except end line
            line_str = line_str.rstrip()
            
            # enpty line?
            if line_str == '':
                self.dict_l[str(line_no)] = "0"
                self.se_e_p = line_no
                continue
            
            # without section?
            l = self.isPattern('^(\s+)\S.*$', line_str)
            if (l):
                # leading space length
                l = len(l)
                
                # section start leading space length
                if not self.sect_c in self.dict_s:
                    self.dict_s[self.sect_c] = str(l)
                
                # each line leading space length
                self.dict_l[str(line_no)] = str(l)
                
                # leading space length hierarchy process.
                if not str(l) in self.dict_h:
                    self.dict_h[str(l)] = "1"
                self.se_e_p = line_no
                continue
                
            else:
                # detect last section end
                if line_no > self.ss_e_p:
                    # each section process
                    if not self.sectionEach(self.sect_c):
                        return(False)
                    else:
                        return(True)
                # detect next section
                t = self.isPattern('^(\S+\s*\S*)$', line_str)
                if (t):
                    self.sect_n = t
                    # each section process
                    if not self.sectionEach(self.sect_c):
                        return(False)
                    # initiate next section
                    self.se_b_p = line_no
                    self.sect_c = self.sect_n
                    self.dict_h = {}                # leading space length hierarchy
                    self.dict_l = {}                # leading space length dict
                    continue
                else:
                    self.putWarning('not specifid line:{}'.format(line_str))
                    continue
                    
            return(True)
        
        # 
        self.hold_row.getStackList()
        
        return(True)
    
    def parseManOut(self):
        """
            parse 'man output'
            [copyHTMLしたman出力を解釈]
        """
        
        # 'man output' is Copy_as_HTML format?
        
        # check limit length
        if self.man_l < 9:
            self.putWarning('not specifid length of clipboard:{}'.format(str(self.man_l)))
            return(False)
        
        # must be. ex. <pre>[root@localhost ~]# man --no-hyphenation man | col -bfx
        if not re.match('^<pre>', self.man_list[0]):
            self.putWarning('not specifid <pre>[...:{}'.format(self.man_list[0]))
            return (False)
        
        # must be. ex. [root@localhost ~]#
        if not re.match(r'^\[', self.man_list[self.man_l - 2]):
            self.putWarning('not specifid [...:{}'.format(self.man_list[self.man_l - 2]))
            return (False)
        
        # must be. ex. </pre>
        if not re.match(r'</pre>', self.man_list[self.man_l - 1]):
            self.putWarning('not specifid </pre>:{}'.format(self.man_list[self.man_l - 1]))
            return (False)
        
        # process header line.
        if not self.headAndTail(self.head_pse, self.man_list[self.head_p]):
            self.putWarning('not specifid header:{}'.format(self.man_list[self.head_p]))
            return(False)
        
        # section process
        if not self.sections():
            return(False)
        
        # process tail lines.
        if not self.headAndTail(self.tail_pse, self.man_list[self.tail_p]):
            self.putWarning('not specifid tail:{}'.format(self.man_list[self.tail_p]))
            return (False)
        
        # past HTML to clip board
        self.clip_board.set(self.hold_row.getStack())
        
        return(True)


if __name__ == '__main__':
    
    # parse man output
    parse_man = ParseManOut()
    if parse_man.parseManOut():
        exit(0)
    else:
        exit(1)


