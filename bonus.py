from abc import ABC, abstractmethod
# SRP is fulfilled as all of the functionalities are separated into distinct classes
# OCP is fulfilled by allowing new activities to be added simply without breaking any existing code
# LSP is fulfilled by each subclass doing the same roles as the superclass
# ISP is fulfilled as datastorage is set up for future different storage possibilities, plus display is separated
# DIP is fulfilled as ActivityMonitor has DataStorage and Display put in the constructor so there is loose coupling
# this program works by initializing a UserRecord() storage, a Display() and creating an activitymonitoring object of the ActivityMonitor() class.
# ActivityMonitor() will ask you for inputs and then you can use the method viewRecords() to access the user's records. Display notifies whenever a new record is created.
class User:
    def __init__(self, username):
        self.username = username
        self.record = []
    def viewRecords(self):
        i = 1
        for record in self.record:
            print(f"Record {i}: ")
            record.printDetails()
            i = i + 1

class ActivityObserver(ABC):
    def _init__(self):
        pass

    @abstractmethod
    def notify(self, activity):
        pass

class Display(ActivityObserver):
    def __init__(self):
        pass

    def notify(self, activity):
        print(f"New record of type {activity.activity_type} succesfully recorded.")

class Activity(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def getActivityType(self):
        pass
    @abstractmethod
    def getDistanceTraveled(self):
        pass
    @abstractmethod
    def getCaloriesBurned(self):
        pass
    @abstractmethod
    def getTime(self):
        pass
    @abstractmethod
    def getHeartRate(self):
        pass
    @abstractmethod
    def printDetails(self):
        pass

# make dataStorage an ABC for future prep of multiple ways to store data, since this simply uses a record inside User class
class DataStorage(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def storeData(self, user: User, activity: Activity):
        pass
    @abstractmethod
    def deleteData(self, user: User, activity: Activity):
        pass
    
class UserRecord(DataStorage):
    def __init__(self):
        pass

    def storeData(self, user: User, activity: Activity):
        user.record.append(activity)

    def deleteData(self, user: User, activity: Activity):
        user.record.remove(activity)

# dependencies in constructor
class ActivityMonitor:
    def __init__(self, data_storage: UserRecord, display: Display):
        self.data_storage = data_storage
        self.display = display
    # collectData() allows for new activity types to be simply added by adding a new elif
    def collectData(self, user: User):
        activity_type = input("Which activity type do you want to track? We can currently track: Swimming, Running: ")
        distance_traveled = input("How far did you travel: ")
        calories_burned = input("How many calories did you burn: ")
        time = input("How long did you exercise: ")
        heart_rate = input("What was your average heart rate: ")
        yesOrNo = input("Do you want to store this Data? Please answer YES OR NO ")
        yesOrNo = yesOrNo.lower()
        activity_type = activity_type.lower()
        if (yesOrNo == "yes"):
            if activity_type == "swimming":
                newRecord = Swimming(distance_traveled, calories_burned, time, heart_rate)
                self.data_storage.storeData(user, newRecord)
                self.display.notify(newRecord)
            elif activity_type == "running":
                newRecord = Running(distance_traveled, calories_burned, time, heart_rate)
                self.data_storage.storeData(user, newRecord)
                self.display.notify(newRecord)                
        else:
            print("Data recording cancelled.")
            exit()


class Swimming(Activity):
    def __init__(self, distance_traveled, calories_burned, time, heart_rate):
        self.activity_type = "Swimming"
        self.distance_traveled = distance_traveled
        self.calories_burned = calories_burned
        self.time = time
        self.heart_rate = heart_rate

    def getActivityType(self):
        return self.activity_type
    def getDistanceTraveled(self):
        return self.distance_traveled
    def getCaloriesBurned(self):
        return self.calories_burned
    def getTime(self):
        return self.time
    def getHeartRate(self):
        return self.heart_rate
    def printDetails(self):
        print(f"Activity type: {self.activity_type}\n Distance Traveled: {self.distance_traveled}\n Calories Burned: {self.calories_burned}\n Time: {self.time}\n Average BPM: {self.heart_rate}\n")

class Running(Activity):
    def __init__(self, distance_traveled, calories_burned, time, heart_rate):
        self.activity_type = "Running"
        self.distance_traveled = distance_traveled
        self.calories_burned = calories_burned
        self.time = time
        self.heart_rate = heart_rate

    def getActivityType(self):
        return self.activity_type
    def getDistanceTraveled(self):
        return self.distance_traveled
    def getCaloriesBurned(self):
        return self.calories_burned
    def getTime(self):
        return self.time
    def getHeartRate(self):
        return self.heart_rate
    def printDetails(self):
        print(f"Activity type: {self.activity_type}\n Distance Traveled: {self.distance_traveled}\n Calories Burned: {self.calories_burned}\n Time: {self.time}\n Average BPM: {self.heart_rate}\n")
    
def main():
    newUser = User("khaz")
    newStorage = UserRecord()
    newDisplay = Display()
    ActivityMonitorer = ActivityMonitor(newStorage, newDisplay)
    ActivityMonitorer.collectData(newUser)
    ActivityMonitorer.collectData(newUser)
    newUser.viewRecords()


if __name__ == "__main__":
    main()