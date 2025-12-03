"""
DAFTAR FUNGSI DARI KALKULATOR
"""
import math
PI = math.pi
UEREL = math.e
"""
operasi bilangan sederhana
"""
def tambah(*nomor:int,cara_penyelesaian:bool=False,tampilan_output:int=1):
    
    tampilan = ' + '.join(map(str,nomor))
    hasil_akhir = sum(nomor)
    
    if cara_penyelesaian == True and tampilan_output == 1:
       return f" cara penyelesaian dari {tampilan}\nhasil akhir : {hasil_akhir}"
   
    elif cara_penyelesaian == True and tampilan_output == 2:
        return f"hasil akhir dari {tampilan} adalah {hasil_akhir}"
    
    

def kurang(*nomor): return f'hasil: {nomor - nomor}'
def kali(*nomor): return f'hasil: {nomor * nomor}'
def bagi_desimal(*nomor): return f'hasil: {nomor / nomor}'
def bagi_bulat(*nomor): return f'hasil: {nomor // nomor}'

"""
operasi bilangan kompleks
"""
def faktorial(*angka):
    for i in angka:
        pass