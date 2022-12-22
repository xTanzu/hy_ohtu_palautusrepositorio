from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli(tyyppi):
    if tyyppi == "kaksinpeli":
        return KPSPelaajaVsPelaaja()
    elif tyyppi == "yksinpeli_helppo":
        return KPSTekoaly()
    elif tyyppi == "yksinpeli_vaikea":
        return KPSParempiTekoaly(10)
    elif tyyppi == "yksinpeli_extravaikea":
        return KPSParempiTekoaly(100)
    else:
        raise ValueError("Tuntematon pelityyppi")
