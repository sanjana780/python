from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd

class PythonCafeTalk:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Cafe Talk")
        
        width, height = 1200, 600
        d = str(width) + "x" + str(height)
        self.root.geometry(d)
        self.root.configure(bg="#55a3a3")

        self.menu_frame = Frame(self.root, bg="#55a3a3")
        self.menu_frame.pack()

        Label(self.menu_frame, text="Restrau Cafe", font=("Montserrat", 24), bg="#55a3a3", fg="#2c3e50").pack()
        Label(self.menu_frame, text="Since-1997", font=("Montserrat", 18), bg="#55a3a3").pack()
        Label(self.menu_frame, text="www.fuddybuddy.com", font=("Montserrat", 14), bg="#55a3a3").pack()
        Label(self.menu_frame, text="\nMENU", font=("Montserrat", 20), bg="#55a3a3").pack()

        self.cuisines = ["Rajasthani", "Gujrati", "Punjabi", "South Indian"]
        
        for cuisine in self.cuisines:
            btn = Button(self.menu_frame, text=cuisine, font=("Montserrat", 16), command=lambda c=cuisine: self.show_menu(c))
            btn.pack(pady=5)

    def show_menu(self, cuisine):
        self.menu_frame.pack_forget()
        self.order_frame = Frame(self.root)
        self.order_frame.pack(fill="both", expand=True)

        self.food_types, self.prices = self.get_menu_data(cuisine)
        menu_data = {"Food": self.food_types, "Price": self.prices}
        df = pd.DataFrame(menu_data)
        text = f"\n{cuisine} Foods\n\n{df.to_string(index=False)}"

        Label(self.order_frame, text=text, font=("Montserrat", 14), justify="left").pack()
        Label(self.order_frame, text="Select Item Position and Quantity", font=("Montserrat", 12)).pack()

        self.position_var = StringVar()
        self.quantity_var = StringVar()
        
        Label(self.order_frame, text="Position:").pack()
        Entry(self.order_frame, textvariable=self.position_var).pack()
        
        Label(self.order_frame, text="Quantity:").pack()
        Entry(self.order_frame, textvariable=self.quantity_var).pack()

        Button(self.order_frame, text="Add to Order", command=self.add_to_order).pack(pady=10)
        Button(self.order_frame, text="Finish Order", command=self.finish_order).pack(pady=10)

        self.order_list = []

    def get_menu_data(self, cuisine):
        if cuisine == "Rajasthani":
            return (["Dal Baati Churma", "Gatte ki Sabzi", "Ker Sangri", "Pyaaz Kachori", "Bajre ki Roti"],
                    [150, 120, 180, 50, 30])
        elif cuisine == "Gujrati":
            return (["Dhokla", "Thepla", "Undhiyu", "Khandvi", "Handvo"],
                    [60, 40, 120, 50, 100])
        elif cuisine == "Punjabi":
            return (["Chole Bhature", "Sarson Da Saag", "Makki Di Roti", "Rajma Chawal", "Paneer Tikka"],
                    [80, 100, 40, 60, 120])
        elif cuisine == "South Indian":
            return (["Dosa", "Idli", "Vada", "Sambar", "Uttapam"],
                    [50, 30, 20, 40, 60])

    def add_to_order(self):
        try:
            position = int(self.position_var.get())-1
            quantity = int(self.quantity_var.get())
            price = self.prices[position]
            self.order_list.append(price * quantity)
            messagebox.showinfo("Item Added", f"Added {quantity} of {self.food_types[position]} to order.")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def finish_order(self):
        if not self.order_list:
            messagebox.showinfo("No Order", "No items ordered.")
            return

        total = sum(self.order_list)
        service_tax = total * 0.05
        total_with_tax = total + service_tax

        messagebox.showinfo("Total Amount", f"Total Amount: {total} Rupees\nService Tax: 5%\nTotal Amount Including Service Tax: {total_with_tax} Rupees")
        self.order_frame.pack_forget()
        self.__init__(self.root)


if __name__ == "__main__":
    root = Tk()
    app = PythonCafeTalk(root)
    root.bind('<Escape>', lambda e:root.quit())
    root.mainloop()
