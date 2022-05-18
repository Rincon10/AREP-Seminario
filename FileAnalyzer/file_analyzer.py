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

        # Titles
        self._titles = ["Nombre del proyecto","Autores","Total de líneas de codigo","Total de clases","Total de controladores", "Total de servicios","Número de los microservicios sugeridos"]


        # Default data
        self.setProperties()


    def setProperties(self):
        i = 0
        for property in self._properties:
            obj = { "title": self._titles[i], "value": "" }
            self._data[property] = obj
            i+=1

        self._data["nameProject"]["value"] = self._nameProject

    def findFile(self, name, path, bFolder):
        totalLines, result = 0, []
        for dirpath, dirname, filename in os.walk(path):
            if ( bFolder ):
                print(self._nameProject, dirpath,self._nameProject in dirpath)
                if  (name in dirpath):
                    return filename
            elif (self._nameProject in dirpath):
                for n in filename:
                    if fnmatch.fnmatch(n, name):
                        print(dirpath,n, name,fnmatch.fnmatch(n, name))
                        print("")

                        d = dirpath.replace("\\","/")+"/"+n
                        """ print(d)
                        print("") """
                        with open(d) as fp:
                            lines = len(fp.readlines())
                            """ print(lines, totalLines) """
                            totalLines+=lines
                        result.append(n)
        
        return [totalLines,result]

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
    
    def removeProject(self):
        command = "rm -r "+self._nameProject
        os.system(command)

    def getMicroservicesName(self):
        
        c = self._data["controllers"]["value"].lower()
        c = c.replace(".java", "")
        c = c.replace("controller","")
        c = c.replace("api","")

        return c
            
    def createInformation(self):
        self.startDownload()
        self.setProperties()

        controllers = self.findFile("controller", self._path, True)
        services = self.findFile("service", self._path, True)
        totalLines, totalClasses = self.findFile("*.java", self._path, False)

        self._data["controllers"]["value"] = ", ".join(controllers)
        self._data["services"]["value"] = ", ".join(services)
        self._data["totalClasses"]["value"] = len(totalClasses)
        self._data["totalLines"]["value"] = totalLines
        self._data["microServicesSuggested"]["value"] = self.getMicroservicesName()

        """ self.removeProject() """
        return self._data
