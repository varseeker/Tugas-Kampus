namaKampus = 'UNIVERSITAS BSI'
lineDouble = '================================================================='
lineStraight = '-----------------------------------------------------------------'

apps = True
while apps:
    listMatkul = []
    listHM = []
    listAM = []
    listSKS = []
    listMutu = []

    namaMatkul = ''
    jmlSKSMatkul = 0
    nilaiAbsen = 0
    nilaiTugas = 0
    nilaiUts = 0
    nilaiUas = 0

    nilaiIPK = 0
    predikat = ''
    nilaiMutu = 0

    nim = input("Masukkan NIM : ")
    namaMhs = input("Masukkan Nama Mahasiswa/i : ")
    tmptLahir = input("Masukkan Tempat Lahir : ")
    programStudi = input("Masukkan Program Studi : ")

    while True:
        try:
            bnykMatkul = int(input("Banyak Mata Kuliah yang diambil : "))
        except:
            print("Tolong Masukan Input Angka!")
            continue
        if type(bnykMatkul) is int:
            if bnykMatkul < 0: 
                print('input tidak bisa lebih kecil dari 0.')
            else:
                break

    count = 0
    while count < bnykMatkul:
        print("Data Ke-", count+1)
        namaMatkul = input("Mata Kuliah : ")

        # Input Total SKS
        while True:
            try:
                jmlSKSMatkul = int(input("Jumlah SKS yang diambil : "))
            except:
                print("Tolong Masukan Input Angka!")
                continue
            if type(jmlSKSMatkul) is int:
                if jmlSKSMatkul < 0: 
                    print('input tidak bisa lebih kecil dari 0.')
                else:
                    break
        # Input Nilai Absen
        while True:
            try:
                nilaiAbsen = int(input("Nilai Absen : "))
            except:
                print("Tolong Masukan Input Angka!")
                continue
            if type(nilaiAbsen) is int:
                if nilaiAbsen < 0: 
                    print('input tidak bisa lebih kecil dari 0.')
                else:
                    break
        # Input Nilai Tugas 
        while True:
            try:
                nilaiTugas = int(input("Nilai Tugas : "))
            except:
                print("Tolong Masukan Input Angka!")
                continue
            if type(nilaiTugas) is int:
                if nilaiTugas < 0: 
                    print('input tidak bisa lebih kecil dari 0.')
                else:
                    break
        # Input Nilai UTS
        while True:
            try:
                nilaiUts = int(input("Nilai UTS : "))
            except:
                print("Tolong Masukan Input Angka!")
                continue
            if type(nilaiUts) is int:
                if nilaiUts < 0: 
                    print('input tidak bisa lebih kecil dari 0.')
                else:
                    break
        # Input Nilai UAS
        while True:
            try:
                nilaiUas = int(input("Nilai UAS : "))
            except:
                print("Tolong Masukan Input Angka!")
                continue
            if type(nilaiUas) is int:
                if nilaiUas < 0: 
                    print('input tidak bisa lebih kecil dari 0.')
                else:
                    break

        listMatkul.append(namaMatkul)
        listSKS.append(jmlSKSMatkul)
        totalNilai = round(((20/100)*nilaiAbsen) + ((20/100)*nilaiTugas) + ((30/100)*nilaiUts) + ((30/100)*nilaiUas))
        am = 0
        if totalNilai >= 80:
            listHM.append('A')
            listAM.append(4)
            am = 4
        elif totalNilai >= 75:
            listHM.append('B')
            listAM.append(3)
            am = 3
        elif totalNilai >= 60:
            listHM.append('C')
            listAM.append(2)
            am = 2
        elif totalNilai >= 48:
            listHM.append('D')
            listAM.append(1)
            am = 1
        else:
            listHM.append('E')
            listAM.append(0)
            am = 0
        mutu = jmlSKSMatkul * am
        listMutu.append(mutu)
        count += 1
    # FINAL OUTPUT
    print(namaKampus)
    print(lineDouble)
    print("NIM : ", str(nim))
    print("Nama Mahasiswa/i : ", str(namaMhs))
    print("Tempat Lahir : ", str(tmptLahir))
    print("Program Studi : ", str(programStudi))
    print(lineDouble)
    count = 1
    jmlMutu = 0
    jmlSks = 0
    print('NO   MATA KULIAH         HM          AM          SKS         Mutu')
    for index in range(len(listMatkul)):
        print(count,"   ",listMatkul[index],"           ",listHM[index],"          ",listAM[index],"          ",listSKS[index],"         ",listMutu[index])
        jmlMutu += listMutu[index]
        jmlSks += listSKS[index]
        count += 1

    print(lineDouble)
    print('Jumlah : ', jmlSks,'     ', jmlMutu)
    nilaiIPK = jmlMutu/jmlSks
    ipk = ''
    if nilaiIPK <= 4:
        ipk = 'Cumlaude'
    elif nilaiIPK <= 3:
        ipk = 'Memuaskan'
    elif nilaiIPK <= 2: 
        ipk = 'Cukup'
    else:
        ipk = 'Kurang'
    print('Indeks Prestasi : ', nilaiIPK)
    print('Predikat : ', ipk)

    serviceCmnd = input("Mau Isi lagi : ")
    if serviceCmnd == 't':
        apps = False
    else:
        continue
        



