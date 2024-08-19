
from pyshorteners import Shortener

s = Shortener()

print("SHORTENER LINK")
print("1. TinyURL\n2. Git IO (Only Git Link)\n3. Qps.Ru\n4. OwLy\n5. OsDb\n6. NullPointer\n7. IsGd\n8. DaGd\n9. ClckRu\n10.ChilpIt")
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

elif choiceLink == "4" :
  try :
    link = s.owly.short(input("Input link: "))
    print("Here is a link : " + link)
  except Exception as e :
    print(e)

elif choiceLink == "5" :
  try :
    link = s.osdb.short(input("Input link: "))
    print("Here is a link : " + link)
  except Exception as e :
    print(e)

elif choiceLink == "6" :
  try :
    link = s.nullpointer.short(input("Input link: "))
    print("Here is a link : " + link)
  except Exception as e :
    print(e)

elif choiceLink == "7" :
  try :
    link = s.isgd.short(input("Input link: "))
    print("Here is a link : " + link)
  except Exception as e :
    print(e)

elif choiceLink == "8" :
  try :
    link = s.dagd.short(input("Input link: "))
    print("Here is a link : " + link)
  except Exception as e :
    print(e)

elif choiceLink == "9" :
  try :
    link = s.clckru.short(input("Input link: "))
    print("Here is a link : " + link)
  except Exception as e :
    print(e)
    
elif choiceLink == "10" :
  try :
    link = s.chillpit.short(input("Input link: "))
    print("Here is a link : " + link)
  except Exception as e :
    print(e)
    
else :
  print("Invalid choice")