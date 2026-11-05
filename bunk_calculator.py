import math


class BunkCalculator:
    """Calculates attendance, bunks available, and classes needed to attend."""

    def __init__(self, attended: int, total: int, target: float = 75.0):
        self.attended = attended
        self.total = total
        self.target = target

    @classmethod
    def from_user_input(cls):
        """Class method to take input directly from the user and create an instance."""
        attended = int(input("Enter number of classes attended: "))
        total = int(input("Enter total classes conducted: "))
        target_str = input("Enter target percentage (press Enter for default 75%): ").strip()
        target = float(target_str) if target_str else 75.0
        return cls(attended, total, target)

    def change_percentage(self, new_target: float):
        """Method to change target percentage (e.g., 75, 80, etc.)."""
        self.target = new_target

    def get_current_percentage(self) -> float:
        """Method to calculate current attendance percentage."""
        if self.total == 0:
            return 0.0
        return (self.attended / self.total) * 100

    def calculate_bunks_allowed(self) -> int:
        """Method to calculate how many classes can be bunked."""
        current_pct = self.get_current_percentage()
        if current_pct < self.target:
            return 0
        bunks = math.floor((100 * self.attended - self.target * self.total) / self.target)
        return max(0, bunks)

    def calculate_classes_needed(self) -> int:
        """Method to calculate how many classes need to be attended."""
        current_pct = self.get_current_percentage()
        if current_pct >= self.target:
            return 0
        needed = math.ceil((self.target * self.total - 100 * self.attended) / (100 - self.target))
        return max(0, needed)

    def display_status(self):
        """Method to display the attendance result."""
        current_pct = self.get_current_percentage()
        print("\n--- Attendance Status ---")
        print(f"Current Attendance: {current_pct:.2f}% ({self.attended}/{self.total})")
        print(f"Target Percentage: {self.target}%")

        if current_pct >= self.target:
            print(f"Safe: You can miss {self.calculate_bunks_allowed()} class(es).")
        else:
            print(f"Shortage: You need to attend {self.calculate_classes_needed()} class(es) consecutively.")


def start_calculator():
    """Function to run the application."""
    # Create instance using the class method which gets user input
    calculator = BunkCalculator.from_user_input()
    calculator.display_status()

    # Allow changing the target percentage
    while True:
        choice = input("\nDo you want to change the target percentage? (y/n): ").strip().lower()
        if choice == "y":
            new_target = float(input("Enter new target percentage (e.g. 80, 85, 70): "))
            calculator.change_percentage(new_target)
            calculator.display_status()
        else:
            break


if __name__ == "__main__":
    start_calculator()