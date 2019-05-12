# This is where the user object will go

class User():
	def __init__(self, username, email, notificationTime, zipCode, preference):
		self.username = username
		self.email = email
		self.notificationTime = notificationTime
		self.zipCode = zipCode
		self.preference = preference
		
	def writeUser(self):
                f = open("userList.txt", "a+")
                f.write("Username: " + self.username)
                f.write("\nEmail: " + self.email)
                f.write("\nNotification Time: " + self.notificationTime)
                f.write("\nZipcode: " + self.zipCode)
                f.write("\nPreferences: " + self.preference + "\n\n")
                f.close()
