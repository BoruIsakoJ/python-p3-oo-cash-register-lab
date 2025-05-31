#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items=None, last_transaction_amount=0):
    self.discount = discount
    self.total = total
    self.items = items if items is not None else []
    self.last_transaction_amount = last_transaction_amount

    
  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.last_transaction_amount = price * quantity
    for _ in range(quantity):
      self.items.append(title)  
      
  def apply_discount(self):
    if self.discount > 0:
      self.total -= (self.discount/100 *self.total)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
    self.total -= self.last_transaction_amount
    self.last_transaction_amount = 0