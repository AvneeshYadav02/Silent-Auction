# Auction Program

This is a Python program that simulates an **auction bidding system**. Users can place their bids, and the program determines the highest bidder.

---

## Features

- Uses a **dictionary** to store bidders' names and their respective bids.
- Allows multiple bidders to participate.
- Determines the **highest bidder** and declares the winner.

---

## How It Works

1. **Display Logo**  
   The program imports a logo from the `art` module and displays it when the program starts.

2. **Add Bids**  
   Users are prompted to enter their name and bid amount.

3. **Check for More Bidders**  
   Users are asked whether there are more bidders:
   - Type `1` to add more bidders.
   - Type `2` to finish and calculate the winner.

4. **Determine the Winner**  
   The program uses a dictionary to track bids and determines the highest bidder by comparing values.

5. **Announce the Winner**  
   The name of the highest bidder is displayed.

---

## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/auction-program.git
   ```
2. Ensure you have Python installed (version 3.6 or above).
3. Install the `art` package:
   ```bash
   pip install art
   ```
4. Run the program:
   ```bash
   python auction.py
   ```

---

## Sample Output

```
Welcome to the Auction!
What's Your name:
John
How much do you want to bid:
$300
Are there anymore bidders?(Type '1' for yes and '2' for no):
1
...

************************************THE WINNER IS John!!************************************
```
