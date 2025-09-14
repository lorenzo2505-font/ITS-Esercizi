'''Dati due array ordinati nums1 e nums2 di dimensione rispettivamente m e n, restituire la mediana dei due array ordinati.

La complessità complessiva in fase di esecuzione dovrebbe essere O(log(m+n)).'''
import math

def median_arrays(nums1: list[int], nums2: list[int]) -> int | float:
    
    nums3: list[int] = sorted(nums1 + nums2)
    
    if len(nums3) % 2 != 0:
        mediana = (len(nums3) + 1) / 2

    else:
        mediana = (nums3[int((len(nums3) / 2) - 1)] + nums3[int(len(nums3) / 2)]) / 2
    
    return mediana




def main():

    print(median_arrays([1, 3], [2]))
    print(median_arrays([1, 2], [3, 4]))

main()
