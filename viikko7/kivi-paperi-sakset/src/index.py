from pelitehdas import luo_peli


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\n (d) Isommalla muistilla varustettua parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            luo_peli("kaksinpeli").pelaa()
        elif vastaus.endswith("b"):
            luo_peli("yksinpeli_helppo").pelaa()
        elif vastaus.endswith("c"):
            luo_peli("yksinpeli_vaikea").pelaa()
        elif vastaus.endswith("d"):
            luo_peli("yksinpeli_extravaikea").pelaa()
        else:
            break


if __name__ == "__main__":
    main()
