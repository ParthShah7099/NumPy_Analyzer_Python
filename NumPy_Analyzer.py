import numpy as np

class DataAnalytics:
    def __init__(self):
        self.array = None

    def create_array(self):
        print("1. Create 1D Array")
        print("2. Create 2D Array")
        print("3. Create 3D Array")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                elements = input("Enter elements separated by space: ").split()
                self.array = np.array([int(i) for i in elements])
            elif choice == "2":
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))
                elements = input("Enter elements separated by space: ").split()
                if len(elements) != rows * cols:
                    print("Invalid number of elements.")
                    return
                self.array = np.array([int(i) for i in elements]).reshape(rows, cols)
            elif choice == "3":
                dim1 = int(input("Enter first dimension size: "))
                dim2 = int(input("Enter second dimension size: "))
                dim3 = int(input("Enter third dimension size: "))
                elements = input("Enter elements separated by space: ").split()
                if len(elements) != dim1 * dim2 * dim3:
                    print("Invalid number of elements.")
                    return
                self.array = np.array([int(i) for i in elements]).reshape(dim1, dim2, dim3)
            else:
                print("Invalid choice.")
                return
            print("Array created successfully:")
            print(self.array)
        except Exception as e:
            print("Error in creating array:", e)

    def math_operations(self):
        if self.array is None:
            print("No array found. Create array first.")
            return

        print("1. Add scalar")
        print("2. Subtract scalar")
        print("3. Multiply scalar")
        print("4. Divide scalar")
        print("5. Dot Product (for 2D)")
        print("6. Matrix Multiplication (for 2D)")
        choice = input("Choose an operation: ")

        try:
            if choice in ["1", "2", "3", "4"]:
                scalar = float(input("Enter scalar value: "))
                if choice == "1":
                    print("Result:", self.array + scalar)
                elif choice == "2":
                    print("Result:", self.array - scalar)
                elif choice == "3":
                    print("Result:", self.array * scalar)
                elif choice == "4":
                    print("Result:", self.array / scalar)
            elif choice in ["5", "6"]:
                if len(self.array.shape) != 2:
                    print("This operation requires a 2D array.")
                    return
                print("Enter another matrix for the operation:")
                rows = int(input("Rows: "))
                cols = int(input("Columns: "))
                values = input("Enter values separated by space: ").split()
                if len(values) != rows * cols:
                    print("Invalid number of values.")
                    return
                other = np.array([int(i) for i in values]).reshape(rows, cols)
                if choice == "5":
                    print("Dot Product:")
                    print(np.dot(self.array, other))
                else:
                    print("Matrix Multiplication:")
                    print(np.matmul(self.array, other))
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error performing operation:", e)

    def combine_split(self):
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                elements = input("Enter elements of 2nd array separated by space: ").split()
                other = np.array([int(i) for i in elements])
                combined = np.concatenate((self.array, other))
                print("Combined Array:")
                print(combined)
            except Exception as e:
                print("Error combining arrays:", e)
        elif choice == "2":
            try:
                sections = int(input("How many parts to split into? "))
                split_arrays = np.array_split(self.array, sections)
                for idx, arr in enumerate(split_arrays):
                    print(f"Part {idx+1}: {arr}")
            except Exception as e:
                print("Error splitting array:", e)
        else:
            print("Invalid choice.")

    def search_sort_filter(self):
        if self.array is None:
            print("No array found. Create array first.")
            return

        print("1. Search for a value")
        print("2. Sort array")
        print("3. Filter array (greater than a value)")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                val = int(input("Enter value to search: "))
                result = np.where(self.array == val)
                if result[0].size > 0:
                    print(f"Value found at index/indices: {result}")
                else:
                    print("Value not found.")
            elif choice == "2":
                print("Sorted Array:", np.sort(self.array, axis=None))
            elif choice == "3":
                val = int(input("Enter filter threshold: "))
                filtered = self.array[self.array > val]
                print("Filtered Array (greater than threshold):", filtered)
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error in Search/Sort/Filter:", e)

    def compute_statistics(self):
        if self.array is None:
            print("No array found. Create array first.")
            return

        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Min and Max")
        print("7. Percentile")
        print("8. Correlation Coefficient")
        choice = input("Choose an operation: ")

        try:
            if choice == "1":
                print("Sum:", np.sum(self.array))
            elif choice == "2":
                print("Mean:", np.mean(self.array))
            elif choice == "3":
                print("Median:", np.median(self.array))
            elif choice == "4":
                print("Standard Deviation:", np.std(self.array))
            elif choice == "5":
                print("Variance:", np.var(self.array))
            elif choice == "6":
                print("Min:", np.min(self.array), "Max:", np.max(self.array))
            elif choice == "7":
                p = float(input("Enter percentile (0-100): "))
                print(f"{p}th Percentile:", np.percentile(self.array, p))
            elif choice == "8":
                arr2 = input("Enter second array elements (same size) separated by space: ").split()
                arr2 = np.array([int(i) for i in arr2])
                if arr2.shape != self.array.shape:
                    print("Arrays must be of same shape for correlation.")
                    return
                print("Correlation Coefficient:", np.corrcoef(self.array.flatten(), arr2.flatten()))
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error computing statistics:", e)

    @classmethod
    def about(cls):
        print("This tool was created using class-based structure and NumPy.")
        print("Author: School Student")

    @staticmethod
    def help():
        print("Choose an option from the menu and follow instructions.")
        print("Use numbers for selecting options.")

def main():
    da = DataAnalytics()

    while True:
        print("\n===== NumPy Analyzer Menu =====")
        print("1. Create NumPy array")
        print("2. Perform mathematical operations")
        print("3. Combine or split array")
        print("4. Search, Sort or Filter Array")
        print("5. Compute Aggregation and Statics")
        print("6. Exit")

        try:
            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                da.create_array()
            elif choice == "2":
                da.math_operations()
            elif choice == "3":
                da.combine_split()
            elif choice == "4":
                da.search_sort_filter()
            elif choice == "5":
                da.compute_statistics()
            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter 1 to 6.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
