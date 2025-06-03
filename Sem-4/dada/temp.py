import pywhatkit

with open("numbers.txt") as file:
    numbers = [line.strip() for line in file if line.strip()]
    
for number in numbers:
    try:
        pywhatkit.sendwhats_image(number,"image.jpg", tab_close=True,caption="")
        print(f"Sent to {number}")
    except Exception as e:
        print(f"Failed to send to {number}: {e}")