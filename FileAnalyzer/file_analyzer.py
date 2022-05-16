import os, fnmatch

class FileAnalyzer:
    def __init__(self, url):
        # URL
        self._url = url

        # Name project
        self._nameProject = os.path.basename(url).replace(".git","")

        # Data
        self._data = {}

        # Current Path 
        self._path = os.getcwd()

        # Object Properties
        self._properties = ["nameProject","authors","totalLines","totalClasses","controllers","services","microServicesSuggested"]

        # Default data
        self.setProperties()


    def setProperties(self):
        for property in self._properties:
            self._data[property] = ([] if property[-1].strip() == "s" and ("total" not in property) else 0 )

        self._data["nameProject"] = self._nameProject
        self._data["microServicesSuggested"] = []
    
    def findFile(self, name, path, bFolder):
        result = []
        for dirpath, dirname, filename in os.walk(path):
            if ( bFolder ):
                if name in dirpath:
                    return [os.path.join(dirpath, name), filename]
            else:
                
                for n in filename:
                    print(n, name,fnmatch.fnmatch(n, name))
                    print("")
                    if fnmatch.fnmatch(n, name):
                        result.append(n)
                        
        return result

    def getCommands(self):
        return ["git clone "+self._url]
    
    def startDownload(self):
        commands = self.getCommands()

        try:
            for command in commands:
                print("Executing command "+command,"\n")
                os.system(command)

            print("\n")
        except:
            print("The project already exits")

    def createInformation(self):
        self.startDownload()

        controllers = self.findFile("controller", self._path, True)[1]
        services = self.findFile("service", self._path, True)[1]
        totalClasses = self.findFile("*.java", self._path, False)

        self._data["controllers"] = controllers
        self._data["services"] = services
        self._data["totalClasses"] = len(totalClasses)

        return self._data
