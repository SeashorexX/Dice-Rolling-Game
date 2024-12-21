import random

while True:
  choice = input("Roll the dice? (y/n): ").lower()

  if choice == "y":
      x = random.randint(1,6)
      y = random.randint(1,6)
      print(f"\n({x},{y})\n")
  elif choice == "n":
      print("\nThanks for Playing!\n")
      break
  else:
      print("\nInvalid choice!\n")
       