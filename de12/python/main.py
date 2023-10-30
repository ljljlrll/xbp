for i in range(3):    
    #文字だから""をいれた
    print(i,"人目")
    name=input("名前をいれてください")
    waist=float(input("腹囲をいれてください"))
    age=int(input("年齢をいれてください"))　

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if age>=40 and waist>=85:
        print(name,"さん、内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")