class FrequencyTracker:

    def __init__(self):
        self.frequency_dict = {}

    def add(self, number: int) -> None:
        self.frequency_dict[number] = self.frequency_dict.get(number, 0) + 1

    def deleteOne(self, number: int) -> None:
        self.frequency_dict[number] = self.frequency_dict.get(number, 0) - 1

    def hasFrequency(self, frequency: int) -> bool:
        for value in self.frequency_dict.values():
            if value == frequency:
                return True
        return False
