import Classes, API

#Personal data here, no need to worry about anything down there (unless you do want to tweak stuff)
#Check Variables.py as well for the remaining input variables. 
#Variables.py inputs are usually once-in-a-blue-moon fill.
#Main file (MetadataManager.py) input fills are updated on pretty much every new export operation, I mean why
#export new stuff without new subscribers or content?

#Patreons
example_patreons = [Classes.User('1', 'User1'), Classes.User('2', 'User2')];

#Comics
example_path = r"C:\Users\JohnnyBlaze\Desktop"
example_comic_1 = Classes.Content(example_path+r"\My Comic\Chapter 1\Title 1 (Artist Name)", "Title 1 (Artist Name)", "Passw0rd")
example_comic_2 = Classes.Content(example_path+r"\My Comic\Chapter 2\Title 2 (Artist Name)", "Title 2 (Artist Name)", "Passw0rd")

#Month's Rewards
example_reward = [example_comic_1, example_comic_2]

#Copies set of images A for each of your subscribers into new sets X1, X2, X..., injecting user-specific metadata into each image.
#Were any of your subscribers to leak this injected content, you could possibly identify them by reading the image's metadata. 
#Deepweb FBI honeypots are rumored to use stuff like this, no idea how it stands in court but it's indeed a 100% guarantee 
#to the source of the image and a helpful tracer.
#API.export_monthly_rewards(example_patreons, example_reward)

#Does the same as the previous method, but doesn't dig into sub-directories & adds a watermark to each image.
#API.export_free_comic(example_reward)