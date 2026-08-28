class GardenError(Exception):
	pass


class PlantError(GardenError):
	pass


class WaterError(GardenError):
	pass


class GardenManager:
	def __init__(self) -> None:
		self.plants: list[str] = []

	def add_plant(self, plant_name: str) -> None:
		try:
			if not plant_name:
				raise PlantError("Plant name cannot be empty!")
			else:
				self.plants.append(plant_name)
				print(f"Added {plant_name} successfully")
		except PlantError as e:
			print(f"Error adding plant: {e}")

	def water_plant(self, water_level: int) -> None:
		print("Opening watering system")
		try:
			if (water_level < 1):
				raise WaterError(f"Water level {water_level} "
								 "is too low (min 1)")
			elif (water_level > 10):
				raise WaterError(f"Water level {water_level} "
								 "is too high (max 10)")
			else:
				for plant in self.plants:
					print(f"Watering {plant} - success")
		except WaterError as e:
			print(f"Error watering plants: {e}")
		finally:
			print("Closing watering system (cleanup)")

	def check_plant_health(self, plant_name: str, water_level: int,
						   sunlight_hours: int) -> None:
		try:
			if not plant_name:
				raise PlantError("Plant name cannot be empty!")
			elif (water_level < 1):
				raise WaterError(f"Water level {water_level} "
								 "is too low (min 1)")
			elif (water_level > 10):
				raise WaterError(f"Water level {water_level} "
								 "is too high (max 10)")
			elif (sunlight_hours < 2):
				raise PlantError(f"Sunlight hours {sunlight_hours} "
								 "is too low (min 2)")
			elif (sunlight_hours > 12):
				raise PlantError(f"Sunlight hours {sunlight_hours} "
								 "is too high (max 12)")
			else:
				print(f"{plant_name}: "
					  f"healthy (water: {water_level}, "
					  f"sun: {sunlight_hours})")
		except GardenError as e:
			print(f"Error checking {plant_name}: {e}")

	def error_recovery(self) -> None:
		print("\nTesting error recovery...")
		try:
			raise GardenError("Not enough water in tank")
		except GardenError as e:
			print(f"Caught GardenError: {e}")
		print("System recovered and continuing...")


def test_garden_management() -> None:
	print("Garden Management System")
	my_garden = GardenManager()
	print("\nAdding plants to garden...")
	my_garden.add_plant("tomato")
	my_garden.add_plant("lettuce")
	my_garden.add_plant("")
	print("\nWatering plants...")
	my_garden.water_plant(2)
	print("\nChecking plant health...")
	my_garden.check_plant_health("tomato", 5, 8)
	my_garden.check_plant_health("lettuce", 15, 5)
	my_garden.error_recovery()
	print("\nGarden management system test complete")

if __name__ == "__main__":
	test_garden_management()