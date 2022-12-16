from pelitapa import Pelitapa

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a") or vastaus.endswith("b") or vastaus.endswith("c"):
            Pelitapa.pelitapa(vastaus)
        else:
            break


if __name__ == "__main__":
    main()
