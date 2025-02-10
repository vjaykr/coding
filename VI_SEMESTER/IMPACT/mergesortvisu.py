# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]
        
#         # Print splitting step
#         print(f"\nSplitting: {arr} → Left: {left}, Right: {right}")
        
#         # Recursively sort left and right
#         merge_sort(left)
#         merge_sort(right)
        
#         # Merge the sorted halves
#         print(f"\nMerging: Left {left} + Right {right} → Original array")
#         i = j = k = 0
        
#         # Compare elements and merge
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 print(f"  Placing left[{i}] ({left[i]}) → position {k}")
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 print(f"  Placing right[{j}] ({right[j]}) → position {k}")
#                 arr[k] = right[j]
#                 j += 1
#             k += 1
#         #its working
#         # Copy remaining elements from left
#         while i < len(left):
#             print(f"  Copying remaining left[{i}] ({left[i]}) → position {k}")
#             arr[k] = left[i]
#             i += 1
#             k += 1
        
#         # Copy remaining elements from right
#         while j < len(right):
#             print(f"  Copying remaining right[{j}] ({right[j]}) → position {k}")
#             arr[k] = right[j]
#             j += 1
#             k += 1
        
#         # Show array after merging
#         print(f"After merging: {arr}")
#     return arr

# # Test the implementation
# if __name__ == "__main__":
#     sample_array = [38, 27, 43, 3, 9, 82, 10]
#     print("Original array:", sample_array)
#     merge_sort(sample_array)
#     print("\nFully sorted array:", sample_array)




import tkinter as tk
from tkinter import messagebox
import time

class MergeSortVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Merge Sort Visualizer")
        self.root.geometry("800x600")

        # Input array
        self.input_label = tk.Label(root, text="Enter array (comma-separated):")
        self.input_label.pack(pady=10)
        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack(pady=10)

        # Start button
        self.start_button = tk.Button(root, text="Start Merge Sort", command=self.start_sorting)
        self.start_button.pack(pady=10)

        # Canvas for visualization
        self.canvas = tk.Canvas(root, width=750, height=400, bg="white")
        self.canvas.pack(pady=20)

        # Text box for logs
        self.log_text = tk.Text(root, height=10, width=80, state="disabled")
        self.log_text.pack(pady=10)

        # Array to sort
        self.array = []

    def log(self, message):
        """Add a message to the log text box."""
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.config(state="disabled")
        self.log_text.see(tk.END)  # Scroll to the end
        self.root.update()

    def draw_array(self, arr, highlight_indices=None, color="lightblue"):
        """Draw the array on the canvas."""
        self.canvas.delete("all")
        bar_width = 700 / len(arr)
        max_height = max(arr) if arr else 1
        for i, value in enumerate(arr):
            x0 = 25 + i * bar_width
            y0 = 380 - (value / max_height) * 350
            x1 = x0 + bar_width - 5
            y1 = 380
            color_fill = color if highlight_indices and i in highlight_indices else "lightblue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_fill)
            self.canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(value), font=("Arial", 10))
        self.root.update()

    def start_sorting(self):
        """Start the merge sort process."""
        try:
            self.array = list(map(int, self.input_entry.get().strip().split(",")))
            if not self.array:
                messagebox.showerror("Error", "Please enter a valid array.")
                return
            self.log_text.config(state="normal")
            self.log_text.delete(1.0, tk.END)
            self.log_text.config(state="disabled")
            self.draw_array(self.array)
            self.log("Starting Merge Sort...")
            self.merge_sort(self.array, 0, len(self.array) - 1)
            self.log("Merge Sort completed!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter comma-separated integers.")

    def merge_sort(self, arr, left, right):
        """Recursive merge sort function."""
        if left < right:
            mid = (left + right) // 2
            self.log(f"\nSplitting: {arr[left:right+1]} → Left: {arr[left:mid+1]}, Right: {arr[mid+1:right+1]}")
            self.draw_array(arr, range(left, right + 1), "lightgreen")
            time.sleep(1)

            # Recursively sort left and right halves
            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)

            # Merge the sorted halves
            self.log(f"\nMerging: Left {arr[left:mid+1]} + Right {arr[mid+1:right+1]} → Original array")
            self.merge(arr, left, mid, right)
            self.draw_array(arr, range(left, right + 1), "lightblue")
            time.sleep(1)

    def merge(self, arr, left, mid, right):
        """Merge two sorted subarrays."""
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                self.log(f"  Placing left[{i}] ({left_arr[i]}) → position {k}")
                i += 1
            else:
                arr[k] = right_arr[j]
                self.log(f"  Placing right[{j}] ({right_arr[j]}) → position {k}")
                j += 1
            self.draw_array(arr, [k], "yellow")
            time.sleep(0.5)
            k += 1

        # Copy remaining elements from left_arr
        while i < len(left_arr):
            arr[k] = left_arr[i]
            self.log(f"  Copying remaining left[{i}] ({left_arr[i]}) → position {k}")
            self.draw_array(arr, [k], "yellow")
            time.sleep(0.5)
            i += 1
            k += 1

        # Copy remaining elements from right_arr
        while j < len(right_arr):
            arr[k] = right_arr[j]
            self.log(f"  Copying remaining right[{j}] ({right_arr[j]}) → position {k}")
            self.draw_array(arr, [k], "yellow")
            time.sleep(0.5)
            j += 1
            k += 1

        self.log(f"After merging: {arr[left:right+1]}")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = MergeSortVisualizer(root)
    root.mainloop()