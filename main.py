data = []
know = ''
while True:
  userinput = input("Input: ")
  words = userinput.split()
  if "?" in words[-1]:
    question = True
  else:
    question = False
  if question == True:
    know = False
    for i in range(len(data)):
      if words[-1][0: -1] == data[i].split()[0]:
        know = True
        print(data[i])
        break
  else:
    print("Learning")
    data.append(userinput)
  words = []
  if know == False:
    print("I have not learn that yet") 