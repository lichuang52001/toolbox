Dim Msg1,Msg2,Msg3
Dim Response
Dim Msg()
redim Msg(9)
Msg(0) = "����Ů���Ѻ���?"
Msg(1) = "��ʳ������!"
Msg(2) = "����ȥ����ĵط�!"
Msg(3) = "����֤��д����!"
Msg(4) = "��������!"
Msg(5) = "������!"
Msg(6) = "���㻤��!!!"
Msg(7) = "����!"
Msg(8) = "�������Ӿ!"
Style = vbYesNo + vbInformation
Title = "С�����Ҫ����"
for i=0 to 8
    Response = MsgBox(Msg(i), Style,Title)
    If Response = vbYes Then    ' �û�ѡ��[��].
        MyString = "Yes"    ' Preform some action.
        Response = MsgBox("����,ôô��", vbOKOnly ,Title)
        exit for
    Else    ' �û�ѡ��[��],
        MyString = "No" ' Perfoem some action.
        If i = 8  Then  
            i=-1
        End If
    End If
Next