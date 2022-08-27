import pandas as pd

class Space:
    def __init__(self, building_name, row):
        '''
        constructor
        '''
        self.building_name = building_name
        self.floor_num = ""
        self.row = row
        self.space_name = ""
        self.visitor_dist = pd.DataFrame()
        self.noise_dist = pd.DataFrame()
        self.open_hr = ""
        self.close_hr = ""
        self.has_comp = False
        self.has_charger = False
        
        self.setSpaceName()
        self.setVisitorsDist()
        self.setNoiseDist()
        self.setOpenHr()
        self.setCloseHr()
        self.setHasCharger()
        self.setHasComp()
        

    def setVisitorsDist(self):
        '''
        set a pd data frame with headers ["time", "visitors"]
        '''
        # Extracting visitors
        string = self.row["visitors"]
        visitors = string.split("|")
        self.visitor_dist["visitors"] = visitors
        # Extracting time
        string = self.row["time"]
        time = string.split("|")
        self.visitor_dist["time"] = time
        
    
    def setNoiseDist(self):
        '''
        set a pd data frame with headers ["time", "noise_level"]
        '''
        # Extracting noise_level
        string = self.row["noise_level"]
        noise = string.split("|")
        self.noise_dist["noise_level"] = noise
        # Extracting time
        string = self.row["time"]
        time = string.split("|")
        self.noise_dist["time"] = time

    def setSpaceName(self):
        '''
        set the name of the space
        '''
        self.space_name = self.row["space_name"]
    
    def setCloseHr(self):
        '''
        set the name of the closing hour as a string 
        '''
        self.close_hr = self.row["closing_hour"]
    
    
    def setOpenHr(self):
        '''
        set the name of the opening hour as a string 
        '''
        self.open_hr = self.row["opening_hour"]
    
    def setHasCharger(self):
        '''
        set hasCharger --> boolean
        '''
        if self.row["hasCharger"] == "yes":
            self.has_charger = True
        else:
            self.has_charger = False
    
    def setHasComp(self):
        '''
        set hasComp --> boolean
        '''
        if self.row["hasComp"] == "yes":
            self.has_comp = True
        else:
            self.has_comp = False
    
    def setSpaceName(self):
        '''
        set space name
        '''
        self.space_name = self.row["space_name"]
        
    def setFloor(self):
        '''
        set floor number
        '''
        self.floor_num = self.row["floor"]