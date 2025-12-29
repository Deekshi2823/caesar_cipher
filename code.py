alphabets=list("abcdefghijklmnopqrstuvwxyz")
def cipher(message,shift):
  new_letter=""
  for i in message:
    if i not in alphabets:
      new_letter+=i
    else:
      position=alphabets.index(i)
      new_position=(position+shift)%26
      new_letter+=alphabets[new_position]
  print(new_letter)
want_to_end=False
while not want_to_end:
  choice=input("Enter 'encrypt' for encryption and 'decrypt' for decryption:").lower()
  message=input("Enter your message:").lower()
  shift=int(input("Enter the shift value:"))
  if choice =='encrypt':
    cipher(message,shift)
  elif choice =='decrypt':
    cipher(message,-shift)
  else:
    print("Invalid Input")
  play_again=input("Type 'yes' if you want to play again Otherwise type 'no'.")
  if play_again=='no':
    want_to_end=True
    print("Goodbye")