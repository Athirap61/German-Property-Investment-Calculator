import math
from lst2024 import Lohnsteuer2024
from lst2025 import Lohnsteuer2025


def print_lst(lst: Lohnsteuer2024):
        steuer = math.floor(float(lst.getLstlzz()) + float(lst.getStv()) + float(lst.getSts())) / 100.0
        soli = math.floor(float(lst.getSolzlzz()) + float(lst.getSolzs()) + float(lst.getSolzv())) / 100
        stges = steuer + soli
        print(f"LSTLZZ: {float(lst.getLstlzz())/100}\nVFRB: {float(lst.getVfrb())/100}\nWVFRB: {float(lst.getWvfrb())/100/12}")

brutto = 6400 * 12 *100 # Brutto in ¢ent


# Set the parameters using constructor arguments

l = Lohnsteuer2024()
l.setRe4(brutto) # Cent
l.setStkl(3) # Tax class
l.setLzz(1) # Wage payment period, 2 = month
l.setZkf(0) # Kinder
l.setPkv(0) # GKV (default)
l.setKvz(1.5) # Health insurance contribution (1.50%)
l.setKrv(0) # RV-WEST (default)
l.setAlter1(0) # set 1 if the 64th year of life was completed at the beginning of the calendar year
l.setAf(0) # # 1 if the application of the factor procedure has been selected (only in tax class IV)
l.setF(1) # Factor
l.setPvs(0) # Only if in Saxony
l.setR(0) # Religion yes/no
l.setLzzhinzu(0) # Additional amount on the income tax card
l.setPvz(0) # 1, if surcharge for social long -term care insurance

l.MAIN()
print_lst(l)