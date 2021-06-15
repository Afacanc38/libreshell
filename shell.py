#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# libreshell, sürüm 0.1

# Copyright (C) 2021 Alperen İsa Nalbant

# Bu program özgür yazılımdır: Özgür Yazılım Vakfı tarafından yayımlanan 
# GNU Genel Kamu Lisansı’nın sürüm 3 ya da (isteğinize bağlı olarak) daha 
# sonraki sürümlerinin hükümleri altında yeniden dağıtabilir ve/veya 
# değiştirebilirsiniz.

# Bu program, yararlı olması umuduyla dağıtılmış olup, programın BİR 
# TEMİNATI YOKTUR; TİCARETİNİN YAPILABİLİRLİĞİNE VE ÖZEL BİR AMAÇ İÇİN 
# UYGUNLUĞUNA dair bir teminat da vermez. Ayrıntılar için GNU Genel 
# Kamu Lisansı’na göz atınız.

# Bu programla birlikte GNU Genel Kamu Lisansı’nın bir kopyasını elde 
# etmiş olmanız gerekir. Eğer elinize ulaşmadıysa <http://www.gnu.org/licenses/> 
# adresine bakınız.

try:
    import os, subprocess, time
    print("Libreshell, sürüm 0.1")
    print("\nCopyright (C) 2021 Alperen İsa Nalbant.")
    print("Bu programın KESİNLİKLE HİÇBİR TEMİNATI YOKTUR, ayrıntılar için \"license\" komutunu girin.")
    print("Bu bir özgür yazılımdır, ve bazı koşullar altında yeniden dağıtmakta serbestsiniz; ayrıntılar için \"free-sw\" yazın. ")
    print("\nYardım için \"help\" komutunu kullanın.")
    def main():
        while True:
            command = input("\033[1;34mlibreshell>\033[0m ")   
            if command == "exit":
                break
            elif command == "help":
                print("libreshell: Python ile yazılmış küçük bir komut satırı programı.")
                print("\nKullanım: <komut>")
                print("\nBasit komutlar:")
                print("     cd:             Çalıştığınız dizini değiştirir.")
                print("     ls/list/dir:    Bulunduğunuz dizinin içerisindeki dosya ve klasörleri listeler")
                print("     whoami:         Kullanıcı adınızı uçbirime yazdırır.")
                print("     pwd:            Bulunduğunuz dizinin konumunu yazdırır.")
                print("     clear/cls:      Uçbirim ekranını temizler.")
            elif command == "ls" or command == "dir" or command == "list":
                execute("ls --color=auto")
            elif command == "cls":
                execute("clear")
            elif "#" in command:
                pass
            elif "&&" in command or ";" in command:
                print("\033[1;31mhata:\033[0m Bu özellik libreshell tarafından desteklenmemektedir.")
            elif command == "license":
                print("Bu komutu çalıştırmak için kaynak kodun bulunduğu klasöre gitmeniz gerekir. Çıkmak için q tuşunu kullanabilirsiniz.")
                input("\nDevam etmek için ENTER tuşuna basın.")
                execute("cat lisans | less")
            elif command == "free-sw":
                try:
                    execute("firefox https://www.gnu.org/philosophy/free-sw.tr.html")
                except Exception:
                    try:
                        execute("chromium https://www.gnu.org/philosophy/free-sw.tr.html")
                    except Exception:
                        try:
                            execute("epiphany https://www.gnu.org/philosophy/free-sw.tr.html")
                        except Exception:
                            print("Özgür yazılım hakkında daha fazla bilgi edinin:\nhttps://www.gnu.org/philosophy/free-sw.tr.html")
                    
            elif command[:3] == "cd ":
                cd(command[3:])
            else:
                execute(command)

    def execute(command):
        try:
            if "|" in command:
                s_in, s_out = (0, 0)
                s_in = os.dup(0)
                s_out = os.dup(1)

                fdin = os.dup(s_in)

                for cmd in command.split("|"):
                    os.dup2(fdin, 0)
                    os.close(fdin)

                    if cmd == command.split("|")[-1]:
                        fdout = os.dup(s_out)
                    else:
                        fdin, fdout = os.pipe()

                    os.dup2(fdout, 1)
                    os.close(fdout)

                    try:
                        subprocess.run(cmd.strip().split())
                    except Exception:
                        print("\033[1;31mhata:\033[0m {}: Komut bulunamadı.".format(cmd.strip()))

                os.dup2(s_in, 0)
                os.dup2(s_out, 1)
                os.close(s_in)
                os.close(s_out)
            else:
                subprocess.run(command.split(" "))
        except Exception:
            print("\033[1;31mhata:\033[0m {}: Komut bulunamadı.".format(command))
        
    def cd(path):
        try:
            os.chdir(os.path.abspath(path))
        except Exception:
            print("\033[1mcd: \033[1;31mhata:\033[0m {}: Böyle bir dizin yok.".format(path))
    try: 
        main()
    except KeyboardInterrupt:
        exit()
    except Exception as hata:
        print("\033[1;31mKabuk ile ilgili ciddi bir hata oluştu. Lütfen https://github.com/Afacanc38/libreshell deposunda yeni sorun (issue) oluşturarak bu sorunu raporlayın.")
        print(f"\033[0;1mHata kodu: {hata}")
        exit()
except Exception as hata:
    print("\033[1;31mKabuk ile ilgili ciddi bir hata oluştu. Lütfen https://github.com/Afacanc38/libreshell deposunda yeni sorun (issue) oluşturarak bu sorunu raporlayın.")
    print(f"\033[0;1mHata kodu: {hata}")
    exit()