def morse_to_text(morse):
    code={' ':' ','a':'01','b':'1000','c':'1010','d':'100','e':'0','f':'0010',
      'g':'110','h':'0000','i':'00','j':'0111','k':'101','l':'0100','m':'11',
      'n':'10','o':'111','p':'0110','q':'1101','r':'010','s':'000','t':'1',
      'u':'001','v':'0001','w':'011','x':'1001','y':'1011','z':'1100'}
    blah=morse.split('/') 
    output=[]
    ans = ""
    for i in blah:
        output.append(i.split())
    for i in output:
        for j in i:
            for cde, value in code.items():
                if value == j:
                    ans = ans + cde 
    return ans