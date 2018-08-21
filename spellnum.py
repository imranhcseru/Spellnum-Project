#name = "spellnum"
def basic_numbers(num):
	basic_numbers = {0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
	return basic_numbers[num]

def tenth_numbers(num):
	tenth_numbers = {2:'Twenty',3:'Thirty',4:'Fourty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}
	return tenth_numbers[num]

def large_numbers(num):	
	large_numbers = {100:'Hundread',1000:'Thousand',100000:'Lacs',1000000:'Million',1000000000:'Billion'}
	return large_numbers[num]
	
def get_number_length(num):
	str_num = str(num)
	num_length = len(str_num)
	return num_length

def get_divisor(num):
	divisor_unit = get_divisor_unit(num)
	divisor_num = {1:1,2:10,3:100,4:1000,6:100000,7:1000000,10:1000000000}
	return divisor_num[divisor_unit]

def get_divisor_unit(num):
	number_length = get_number_length(num)
	if number_length >= 10:
		divisor_unit = 10
	elif number_length >= 7:
		divisor_unit = 7
	elif number_length == 6:
		divisor_unit = 6
	elif number_length >= 4:
		divisor_unit = 4
	elif number_length == 3:
		divisor_unit = 3
	elif number_length == 2:
		divisor_unit = 2
	else:
		divisor_unit == 1
	return divisor_unit

def print_num(resultant,divisor):
	if resultant<=19:
		if resultant == 0:
			pass
		else:
			print(basic_numbers(resultant),end = ' ')
		print(large_numbers(divisor),end = ' ')


def below_hundread(decimal,basic):
	if decimal == None:
		pass
	else:
		print(tenth_numbers(decimal),end = ' ')
	if basic == 0:
		pass
	else:
		print(basic_numbers(basic),end = ' ')

def more_check(num):
	while True:
		if len(str(num))>2:
			divisor = get_divisor(num)
			resultant = int(num/divisor)
			print_num(resultant,divisor)
			num = num%divisor
		else:
			resultant = int(num/10)
			if resultant<2:
				tenth_numbers = None
				basic_numbers = num
			else:
				tenth_numbers = resultant
				basic_numbers = num%10
			below_hundread(tenth_numbers,basic_numbers)
			break;

def reminder_check(num,divisor):
	if num%divisor == 0:
		return True
	else:
		return False

def spellnum(num = 20):
	while True:
		if len(str(num))>2:
			divisor = get_divisor(num)
			resultant = int(num/divisor)
			if len(str(resultant))>1:
				more_check(resultant)
				print(large_numbers(divisor),end = ' ')
			else:
				print_num(resultant,divisor)
			num = num%divisor
		else:
			resultant = int(num/10)
			if resultant<2:
				tenth_numbers = None
				basic_numbers = num
			else:
				tenth_numbers = resultant
				basic_numbers = num%10
			below_hundread(tenth_numbers,basic_numbers)
			break;	
def main():
	num = int(input('Enter number : '))
	spellnum(num)

if __name__ == '__main__':
	main()
