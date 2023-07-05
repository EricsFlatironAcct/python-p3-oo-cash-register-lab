#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = []

  def add_item(self, title, price, quantity = 1):
    self.last_transaction = [title, price, quantity]
    self.total+=price*quantity
    for n in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if self.discount==0 or self.total ==0:
      print("There is no discount to apply.")
    else:
      self.total = self.total*(1-self.discount/100)
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total = self.total - (self.last_transaction[1] * self.last_transaction[2])
    self.items.pop()
    return None

# We're going to create an Object-Oriented Cash Register that can:

# Add items of varying quantities and prices
# Calculate discounts
# Keep track of what's been added to it
# Void the last transaction