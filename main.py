data = []
know = ''
while True:
  userinput = input("Input: ")
  words = userinput.split()
  if question := "?" in words[-1]:
    know = False
    for datum in data:
      if words[-1][:-1] == datum.split()[0]:
        know = True
        print(datum)
        break
  else:
    print("Learning")
    data.append(userinput)
  words = []
  if know == False:
    print("I have not learn that yet") 