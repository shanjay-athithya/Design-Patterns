class execute_pgm:

    def __init__(self, filename = ""):
        self.g=get_memory()
        self.l=load_pgm(self.g,filename)
      #  invoke_parsing()
       # invoke_compilation()
 #       load_obj_file()
        r=run_pgm()

    def initiate_run(self):
        self.g.test_mry_alloc()
        self.l.test_load_pgm()
        
    

class get_memory():
    def __init__(self):
        print("requested os")
    def test_mry_alloc(self):
        print("tested")

class load_pgm():
    def __init__(self,file="", g= None):
        print("loaded")
    def test_load_pgm(self):
        print("tested")

class run_pgm():
    def __init__(self):
        print("run pgm")
e=execute_pgm("xyz.file")
e.initiate_run()


