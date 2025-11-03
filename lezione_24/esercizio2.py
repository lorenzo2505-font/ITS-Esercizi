def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    newdict: dict[str, float] = {}

    for key, value in prodotti.items():

        if value > 20:
            newdict[key] = value - (value * 10 / 100)
    
    return newdict