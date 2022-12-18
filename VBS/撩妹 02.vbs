Dim Msg1, Msg2, Msg3
Dim Response
Dim Msg()
redim Msg(4)

Msg(0) = "Can you be my girlfriend? (choose Y/N)"
Msg(1) = "You know I've had my head tilted up to the stars for as long as I can remember. You know what surprised me the most? It wasn't meeting them. It was meeting you. (choose Y/N)"
Msg(2) = "I foresee all sad but I am still willing to yearn. (choose Y/N)"
Msg(3) = "You will be the apple of my eye. (choose Y/N)"
Style = vbYesNo + vbInformation
Title = "Let's play a game, sweetheart."

for i = 0 to 3
    Response  = MsgBox(Msg(i),Style, Title)
    If Response = vbYes then
        MyString = "Yes"
        Response = MsgBox("You ARE my GF now, I am so happy! CALL ME ASAP. You already know my number.", vbOKOnly, Title)
        exit for
    Else
        MyString = "No"
        If i = 3 then
            i = -1
        End If
    End If 
	Next