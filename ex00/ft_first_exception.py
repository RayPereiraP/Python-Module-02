def check_temperature(tempe_str: str) -> int:
	print(f'testing temperature: {tempe_str}')
	try:
		temp = int(tempe_str)
	except ValueError as exc:
		raise ValueError(f'Error: '{tempe_str}''
		'is not a valide number\n') from exc
	if temp > 40:
		raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
	if temp < 0:
		raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
	print(f"Temperature {temp}°C is perfect for plants!\n")
	return temp

def test_temperature() -> None:
	tests = ['22', 'jsjkd', '120', '-34']
	try: 
		print('garden temperature checker\n')
		for t in tests:
			try:
				check_temperature(t)
			except ValueError as exc:
				print(exc)
	finally:
		print("\n all tests completed - program didn't crash!")

if __name__ == "__main__":
	test_temperature()