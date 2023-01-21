# heyreplit
artinya apa bang messi?


kamu adalah pencari OG paling hebat sedunia

# Disclaimer :
menggunakan script ini berarti setuju dg segala resiko yg di akibatkan
saya tidak bertanggung jawab apabila akun discordmu ke ban, harga btc turun , puan jadi presiden, dll. setelah menggunakan =script ini

script ini hasil edit dari beberapa sumber


# Fitur dan lain lain
1. multi account
2. multi channel
3. send messages yg sudah diatur sendiri di pesan.txt
   - minus : karna menggunakan random order kalo kata didalam pesan.txt sedikit maka bakalan banyak pengulangan 
   - solusi : perbanyak pembendaharaan kata di pesan.txt atau gunakan saja untuk channel khusus spam
4. copas messages atau repost messages yg sebelumnya sudah dikirim orang lain di channel tujuan
   - minus : kalau server sepi maka akan terjadi pengulangan karna pesan yg di copas max 70 pesan sebelumnya
             jadi kalau hanya ada 50 pesan di channel tsb maka script akan mengirim 20 pesan yg sama baru pesan ke 21 beda
   - solusi : gunakan pada channel yg rame 
5. delete message (otomatis menghapus pesan yg dikirim oleh script sebelumnya)
   - minus : rada aneh juga kalo level bnyak tp history chat ga ada

# How to install in replit
Buka 
```
https://replit.com/
```
create account lalu login
lalu klik create


![Screenshot 2023-01-21 201135](https://user-images.githubusercontent.com/87502414/213868637-bd359163-272e-46f8-a8b3-49912819d0f6.png)



pilih import from github



![Screenshot 2023-01-21 201157](https://user-images.githubusercontent.com/87502414/213868649-ce9b1bf7-5acd-44de-912c-add9f7b3c5e4.png)



masukkan url 
```
https://github.com/umyams/heyreplit
```
di kolom github url lalu klik import

proses import lumayan lama jadi ditunngu saja


![Screenshot 2023-01-21 201244](https://user-images.githubusercontent.com/87502414/213868657-b826ddf8-3bec-46ae-840b-4f910738e50e.png)



setelah selesai klik run dan tunggu replit mendownload packages yg dibutuhkan
lalu akan muncul keterangan error seperti ini



![Screenshot 2023-01-21 201602](https://user-images.githubusercontent.com/87502414/213868779-442b3c18-3052-4bc2-938b-82220b673de6.png)


dibagian tools pojok kiri bawah
pilih packages


![Screenshot 2023-01-21 201621](https://user-images.githubusercontent.com/87502414/213868851-46c9565e-86d1-40b5-9435-25ffaa3db428.png)


lalu di kolom seacrh ketik 
```
PyYAML
```

lalu klik tanda + atau install di PyYAML


![Screenshot 2023-01-21 201656](https://user-images.githubusercontent.com/87502414/213868889-81be1602-edb5-4dc4-a6d7-fa32d22cbfa5.png)



# Konfigurasi
setelah script terinstall lanjut untuk konfigurasi
pilih settings.yaml

![Screenshot 2023-01-21 202807](https://user-images.githubusercontent.com/87502414/213868963-9c60e6e1-b993-4891-ab54-b8043113aa4b.png)


```
TOKEN: 
  - ODAtsgu7c4hMxxxxxxxxxxxxxxxxxxxx   # Token akun discordmu, untuk multi akun bisa ditambahi sepuasnya
  - Mzuan73gdi3xxxxxxxxxxxxxxxxxxxxx   # tergantung spek vps mu, 
CHANNEL_ID: 
  - 12345xxxxxxxxxxxxxx                # channel ID server tujuan, untuk multi channel bisa ditambahi sepuasnya
  - 67890xxxxxxxxxxxxxx                # tergantung spek vps mu,
MODE:                                  # mode (teks,copas) untuk mode teks bisa dikosongi atau di tulis "teks"
                                       # untuk mode copas tinggal di isi "copas" 
                                       
DELAY: 10                              # delay dalam detik(second)

DELETE_MSG:                            # fitur untuk delete pesan (kosongi untuk menonaktifkan, isi dg "Y" untuk mengaktifkan)
```

* TOKEN :      isi token discord kamu, untuk multi akun tinggal ditambah kebawah 
* Channel id : isi dg channel id tujuan, untuk multi channel tinggal ditambah dibawahnya
* MODE :       kosong = mode default ambil pesan dari pesan.txt
               copas = mode repost atau copas akan merepost pesan yg dikirim oleh orang lain dari server tsb
               ketik 
               ```
               copas
               ``` 
               disamping MODE untuk mengaktifkan mode copas
               
 *
pesan.txt
tinggal diedit sesuka hati pisahkan tiap kata dg enter
