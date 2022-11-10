import random 
angkarandom = random.randint(0, 100)

print('=' * 45)
print('Silahkan tebak angka 0-100 yang telah kami sediakan!')
print('=' * 45)

for percobaan in range(10):
  jawaban = int(input(f'\nPercobaan ke {percobaan + 1} Masukkan angka: ')) 
  if jawaban == angkarandom :
    print(f'\nAngka anda benar setelah menebak {percobaan + 1} kali')
    break 
  elif jawaban  < angkarandom :
    print( 'Angka terlalu kecil')
  elif jawaban > angkarandom :
     print('Angka terlalu besar')

else:
    print('Anda kurang beruntung')