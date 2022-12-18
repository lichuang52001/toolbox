Dim Msg1,Msg2,Msg3
Dim Response
Dim Msg()
redim Msg(9)
Msg(0) = "做我女朋友好吗?"
Msg(1) = "零食都给你!"
Msg(2) = "带你去好玩的地方!"
Msg(3) = "房产证上写你名!"
Msg(4) = "我做家务!"
Msg(5) = "我做饭!"
Msg(6) = "宠你护你!!!"
Msg(7) = "保大!"
Msg(8) = "我妈会游泳!"
Style = vbYesNo + vbInformation
Title = "小姐姐我要撩你"
for i=0 to 8
    Response = MsgBox(Msg(i), Style,Title)
    If Response = vbYes Then    ' 用户选择[是].
        MyString = "Yes"    ' Preform some action.
        Response = MsgBox("爱你,么么哒", vbOKOnly ,Title)
        exit for
    Else    ' 用户选择[否],
        MyString = "No" ' Perfoem some action.
        If i = 8  Then  
            i=-1
        End If
    End If
Next