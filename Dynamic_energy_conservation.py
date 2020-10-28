
def main():

	class Sensor():
		"""Represent a sensor."""
		def __init__(self, name):
			"""Initialize sensor object."""
			self.name = name
		def pullingdata(self):
			"""Simulate pulling data."""
			print(self.name + "is pulling data.")
	my_Sensor = Sensor('Sensor1')

	print(my_Sensor.name + "has pulled data.")
	my_Sensor.pullingdata()
		
if __name__ == "__main__":
    main()