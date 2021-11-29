class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        return luku in self.ljono

    def lisaa(self, luku):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        if not self.kuuluu(luku):
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

            return True

        return False

    def poista(self, luku):
        try:
            luvun_indeksi = self.ljono.index(luku)
        except ValueError:
            luvun_indeksi = None

        if luvun_indeksi is not None:
            self.ljono[luvun_indeksi] = 0
            for i in range(luvun_indeksi, self.alkioiden_lkm - 1):
                apu = self.ljono[i]
                self.ljono[i] = self.ljono[i + 1]
                self.ljono[i + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_taulukko(self, taulukosta, taulukkoon):
        for index, luku in enumerate(taulukosta):
            taulukkoon[index] = luku

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(int_joukko_a, int_joukko_b):
        int_joukko = IntJoukko()
        a_taulu = int_joukko_a.to_int_list()
        b_taulu = int_joukko_b.to_int_list()

        for luku in a_taulu:
            int_joukko.lisaa(luku)

        for luku in b_taulu:
            int_joukko.lisaa(luku)

        return int_joukko

    @staticmethod
    def leikkaus(int_joukko_a, int_joukko_b):
        int_joukko = IntJoukko()
        a_taulu = int_joukko_a.to_int_list()
        b_taulu = int_joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    int_joukko.lisaa(b_taulu[j])

        return int_joukko

    @staticmethod
    def erotus(int_joukko_a, int_joukko_b):
        int_joukko = IntJoukko()
        a_taulu = int_joukko_a.to_int_list()
        b_taulu = int_joukko_b.to_int_list()

        for luku in a_taulu:
            int_joukko.lisaa(luku)

        for luku in b_taulu:
            int_joukko.poista(luku)

        return int_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        tuotos = "{"
        for i in range(0, self.alkioiden_lkm - 1):
            tuotos += f"{self.ljono[i]}, "
        tuotos += f"{self.ljono[self.alkioiden_lkm - 1]}" + "}"
        return tuotos
