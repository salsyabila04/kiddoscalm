print("\tSelamat Datang di Kuisioner Indikator Tantrum\t")

nama = input("Nama\t: ")
pilihan = input("Selamat Datang Ibu "+nama+", Apakah ibu ingin melakukan skrining indikator tantrum? (y/n)")

while pilihan == "y":
    print("1. Apakah anak ibu menangis dengan berteriak atau menjerit dengan intensitas menangis 5 menit dalam sehari?")
    print("2. Apakah anak ibu menangis dengan menghentakkan kaki dengan intensitas menangis 5 menit dalam sehari?")
    print("3. Apakah anak ibu menangis dengan menjatuhkan diri ke lantai dengan intensitas menangis 5 menit dalam sehari?")
    print("4. apakah anak ibu menangis dengan menggapai lengan tangan atau lengan kaki dengan intensitas menangis 5 menit dalam sehari?")
    print("5. Apakah anak ibu menangis dengan mendorong badan orang tua dengan intensitas menangis 5 menit dalam sehari?")
    print("6. Apakah anak ibu menangis dengan menarik badan orang tua dengan intensitas menangis 5 menit dalam sehari?")
    diagnosa1 = input("Jawaban (y/n): ")

    if diagnosa1 == "y":
        print("1. Apakah anak ibu menangis dengan berteriak atau menjerit terjadi < 5x dalam seminggu?")
        print("2. Apakah anak ibu menangis dengan menghentakkan kaki terjadi < 5x dalam seminggu?")
        print("3. Apakah anak ibu menangis dengan menjatuhkan diri ke lantai terjadi < 5x dalam seminggu?")
        print("4. Apakah anak ibu menangis dengan menggapai lengan tangan atau kaki terjadi < 5x dalam seminggu?")
        print("5. Apakah anak ibu menangis dengan mendorong badan orang tua terjadi < 5x dalam seminggu?")
        print("6. Apakah anak ibu menangis dengan menarik badan orang tua terjadi < 5x dalam seminggu?")
        diagnosa2 = input("Jawaban (y/n): ")

        if diagnosa2 == "y":
            print("Hi, Ibu "+nama+". Hasil skrining awal anak ibu mengalami tantrum dengan kategori rendah, silahkan mengunjungi fitur rekomendasi untuk edukasi penanganan.")
            
        elif diagnosa2 == "n":
                print("\nApakah anak anak mengalami perilaku seperti berikut? :\n")
                print("1. Apakah anak ibu menangis dengan melukai diri sendiri atau orang lain dengan intensitas menangis > 15 menit dalam sehari?")
                print("2. Apakah anak ibu menangis dengan melempar barang dengan intensitas menangis > 15 menit dalam sehari?")
                print("3. Apakah anak ibu menangis dengan mengumpat atau berkata kasar dengan intensitas menangis > 15 menit dalam sehari?")
                print("4. Apakah anak ibu menangis dengan tatapan marah dengan intensitas menangis > 15 menit dalam sehari?")
                print("5. Apakah anak ibu menangis dengan melukai diri sendiri atau orang lain terjadi > 5x dalam seminggu?")
                print("6. Apakah anak ibu menangis dengan melempar barang terjadi > 5x dalam seminggu?")
                print("7. Apakah anak ibu menangis dengan mengumpat atau berkata kasar terjadi > 5x dalam seminggu?")
                print("8. Apakah anak ibu menangis dengan tatapan marah terjadi > 5x dalam seminggu?")
                diagnosa3 = input("Jawaban (y/n): ")

                if diagnosa3 == "y":
                    print("Hi, Ibu "+nama+". Hasil skrining awal anak ibu mengalami tantrum dengan kategori tinggi, silahkan mengunjungi fitur rekomendasi untuk edukasi penanganan, dan konsultasikan ke psikolog terdekat")
                elif diagnosa3 == "n":
                    print("Hi, Ibu "+nama+". Anak anda dalam masa pertumbuhan yang baik")     
                else:
                    print("Hi, Ibu "+nama+". Anak anda dalam masa pertumbuhan yang baik")
        elif diagnosa1 == "n":
            print("Hi, Ibu "+nama+". Anak anda dalam masa pertumbuhan yang baik")
        else:
            print("Hi, Ibu "+nama+". Terima kasih sudah mengunjungi mengujungi sistem kami.")

