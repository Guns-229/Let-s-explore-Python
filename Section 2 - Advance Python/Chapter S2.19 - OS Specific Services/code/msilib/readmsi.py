import msilib

path = "files/MountPointGenerator.msi" #I cannot share msi
dbobject = msilib.OpenDatabase(path, msilib.MSIDBOPEN_READONLY)
view = dbobject.OpenView("SELECT FileName FROM File")
rec = view.MSIViewExecute(None)
print(rec)
r = v.Fetch() 

