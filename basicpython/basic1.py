from basics import mani
print(mani("hello"))
# here we are only importing the defination but not all the file
import basics
print(basics.mani(5))
# here we are impoting whole file so we can acess this like this
# ! we can see that a new folder has been created by the name __pycache__