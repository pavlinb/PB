while True:
  try:
     pb_adr = int(input('Въведете PROFIBUS адрес: '))       
  except ValueError:
     print("Въведете цяло число.")
     continue
  else:
    break   


dip_sw = ['   ', ' 64', ' 32', ' 16', '  8', '  4', '  2', '  1']


def dip_sw_convert(num):
	binary_digits = list("{0:08b}".format(num))
	for i in range(7, -1, -1):
		if binary_digits[i] == '0':
			binary_digits[i] = '  OFF'
			print(dip_sw[i], binary_digits[i])
		else:
			binary_digits[i] = 'ON'
			print(dip_sw[i], '\033[32m' + binary_digits[i] + '\x1b[0m')
	return binary_digits

     
print('Настройки:\n')
dip_sw_convert(pb_adr)