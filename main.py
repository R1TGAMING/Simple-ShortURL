
from pyshorteners import Shortener

s = Shortener()

print("SHORTENER LINK")
print("1. TinyURL\n2. Git IO (Only Git Link)\n3. Qps.Ru")
choiceLink = input("Choice link: ")

if choiceLink == "1" :
  try :
    link = s.tinyurl.short(input("Input link: "))
    print("Here is a link : " + link)
  except Exception as e :
    print(e)
    
elif choiceLink == "2" :
  try :
    link = s.gitio.short(input("Input link: "))
    print("Here is a link : " + link)
  except Exception as e :
    print(e)

elif choiceLink == "3" :
  try :
    link = s.qpsru.short(input("Input link: "))
    print("Here is a link : " + link)
  except Exception as e :
    print(e)

else :
  print("Invalid choice")