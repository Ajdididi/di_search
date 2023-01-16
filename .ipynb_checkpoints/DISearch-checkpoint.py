import sqlite3
db = sqlite3.connect('druginfo.db')
cur = db.cursor()
print('検索したい医薬品名を入力してください（商品名もしくは一般名）')
key = input()
kensaku = '%'+key+'%'
cur.execute("SELECT * FROM info WHERE drug like ? OR general LIKE ?", 
            [kensaku, kensaku]
           )
kekka = cur.fetchall()
cur.close()
db.close()
print('--------------------------------------------')
print(f'該当医薬品数：{len(kekka)}')
print('--------------------------------------------')
for i in range(0, len(kekka)):
    if kekka[i][1] == 1:
        saiyo = '採用あり'
    elif kekka[i][1] == 2:
        saiyo = '院内製剤'
    else:
        saiyo = '採用なし'
    
    if not kekka[i][11] is None:
        youji = '要時'
    else:
        youji = ''
    
    if not kekka[i][12] is None:
        if not kekka[i][13] is None:
            if not kekka[i][14] is None:
                limit = f'科限定：{kekka[i][12]}・{kekka[i][13]}・{kekka[i][14]}'
            else:
                limit = f'科限定：{kekka[i][12]}・{kekka[i][13]}'
        else:
            limit = f'科限定：{kekka[i][12]}'
    else:
        limit = ''
    
    if not kekka[i][9] is None:
        store = '冷'
    else:
        store = ''
    
    if not kekka[i][6] is None:
        class_ = kekka[i][6]
    else:
        class_ = ''

    print(f'{kekka[i][0]}  {store} {youji} {limit} {class_} {saiyo}' )
    print('【基本情報】')
    print(f'   一般名：{kekka[i][4]}  販売会社等：{kekka[i][5]}  薬効分類名：{kekka[i][8]}')
    print(f'   薬価：{kekka[i][7]} 円')
    print('【調剤設定】')
    if not kekka[i][42] is None:  #粉砕設定が空欄かどうかで分岐
        print(f'   一包化：{kekka[i][41]}  粉砕：{kekka[i][42]}  簡易懸濁：{kekka[i][43]}')
        print(f'   注意事項：{kekka[i][44]}')
    else:
        print('   該当しない')
    print('【最大量設定】')
    if not kekka[i][16] is None:
        print(f'   1日最大量：{kekka[i][16]} {kekka[i][15]}  1回最大量：{kekka[i][17]} {kekka[i][15]}')
        print(f'   1日小児量：{kekka[i][18]} {kekka[i][15]}  1回小児量：{kekka[i][19]} {kekka[i][15]}')
        print(f'   設定理由：{kekka[i][20]}')
        print(f'   備考：{kekka[i][21]}')
    else:
        print('   該当しない')
    print('【自動車運転等の注意喚起】')
    if not kekka[i][27] is None:
        print(f'   注意分類：{kekka[i][27]}   注意番号：{kekka[i][28]}')
        print(f'   電カルマスタ登録(1・3)：{kekka[i][29]}')
        print(f'   部門マスタ登録(1・2・3)：{kekka[i][30]}')
    else:
        print('   該当しない')    
    print('【投与日数制限】')
    if not kekka[i][31] is None:
        print(f'   電カル設定（日）：{kekka[i][31]}')
        print(f'   部門設定（日）：{kekka[i][32]}')
        print(f'   休薬チェック表：{kekka[i][33]}')
        print(f'   設定理由：{kekka[i][34]}')
    elif not kekka[i][35] is None:
        print(f'   電カル設定（日）：{kekka[i][35]}')
        print(f'   部門設定（日）：{kekka[i][36]}')
        print(f'   設定理由：{kekka[i][37]}')
    else:
        print('   該当しない')
    print('【冷所医薬品の室温での安定性】')
    if not kekka[i][47] is None:
        print(f'   曝光：{kekka[i][47]}')
        print(f'   遮光：{kekka[i][48]}')
    elif not kekka[i][49] is None:
        print(f'   曝光：{kekka[i][49]}')
        print(f'   遮光：{kekka[i][50]}')
    else:
        print('   該当しない')
    print('【薬情】')
    if not kekka[i][51] is None:
        print(f'   薬効：{kekka[i][51]}')
        print(f'   注意・副作用：{kekka[i][52]}')
        if not kekka[i][51] is None:
            print(f'   薬効（診療科限定）：{kekka[i][53]}')
    else:
        print('   設定なし')
    print('--------------------------------------------')