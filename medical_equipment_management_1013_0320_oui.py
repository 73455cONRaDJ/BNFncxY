# 代码生成时间: 2025-10-13 03:20:28
import numpy as np

"""
Medical Equipment Management System

This system manages medical equipment records using NumPy arrays for efficient data storage.
"""

# Define the Equipment class to manage medical equipment records
class Equipment:
    def __init__(self, name, category, serial_number, purchase_date, price):
        """
        Initializes an Equipment object with the given parameters.
        :param name: str - Name of the equipment
        :param category: str - Category of the equipment
        :param serial_number: str - Serial number of the equipment
        :param purchase_date: str - Purchase date of the equipment in 'YYYY-MM-DD' format
        :param price: float - Purchase price of the equipment
        """
        self.name = name
        self.category = category
        self.serial_number = serial_number
        self.purchase_date = purchase_date
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the equipment.
        """
        return f"{self.name} ({self.category}), Serial: {self.serial_number}, Purchased on: {self.purchase_date}, Price: ${self.price:.2f}"

# Define the MedicalEquipmentManager class to manage the equipment records
class MedicalEquipmentManager:
    def __init__(self):
        """
        Initializes the MedicalEquipmentManager with an empty list to store equipment records.
        """
        self.equipment_list = []

    def add_equipment(self, equipment):
        """
        Adds a new equipment record to the manager.
        :param equipment: Equipment - The equipment object to add
        """
        if not isinstance(equipment, Equipment):
            raise ValueError("Only Equipment objects can be added to the manager.")
        self.equipment_list.append(equipment)

    def remove_equipment(self, serial_number):
        """
        Removes an equipment record by its serial number.
        :param serial_number: str - The serial number of the equipment to remove
        """
        for equipment in self.equipment_list:
            if equipment.serial_number == serial_number:
                self.equipment_list.remove(equipment)
                return
        raise ValueError("Equipment with serial number not found.")

    def find_equipment(self, serial_number):
        """
        Finds an equipment record by its serial number.
        :param serial_number: str - The serial number of the equipment to find
        :return: Equipment - The equipment object if found, otherwise None
        """
        for equipment in self.equipment_list:
            if equipment.serial_number == serial_number:
                return equipment
        return None

    def list_equipment(self):
        """
        Returns a list of all equipment records.
        """
        return self.equipment_list

# Example usage
if __name__ == '__main__':
    manager = MedicalEquipmentManager()
    manager.add_equipment(Equipment('ECG Machine', 'Cardiology', 'SN123', '2023-01-01', 1500.00))
    manager.add_equipment(Equipment('Ultrasound', 'Imaging', 'SN456', '2023-02-01', 5000.00))

    try:
        print(manager.find_equipment('SN123'))
    except ValueError as e:
        print(e)

    try:
        manager.remove_equipment('SN789')
    except ValueError as e:
        print(e)

    for equipment in manager.list_equipment():
        print(equipment)