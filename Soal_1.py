def waktu(time):
    import math
    if 0 <= time <= 359999:
        jam = math.floor(time / 3600)
        sisa_time = time % 3600
        
        menit = math.floor(sisa_time / 60)
        sisa_time1 = sisa_time % 60
        
        detik = sisa_time1

        if 0 <= jam <= 9:
            jam_final = '0' + str(jam)
        else:
            jam_final = jam
            
        if menit < 10:
            menit_final = '0' + str(menit)
        else:
            menit_final = menit

        if detik < 10:
            detik_final = '0' + str(detik)
        else:
            detik_final = detik
            
        hasil = str(jam_final) + ':' + str(menit_final) + ':' + str(detik_final)
        return hasil
    
    else:
        print('Tidak menerima angka negatif maupun angka di luar batas.')

try:
    dtk = int(float((input('Masukan detik: '))))
    print(waktu(dtk))
except:
    print('Hanya menerima Integer.')