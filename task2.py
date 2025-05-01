"""Build a simple bill calculator for a grocery store: Ask for item prices and quantities, apply 18% GST, and show the total bill."""
total_price = float(input("Enter total price of items: "))
gst = total_price * 0.18
final_amount = total_price + gst

print(f"total bill: {final_amount} (including GST: {gst})")
