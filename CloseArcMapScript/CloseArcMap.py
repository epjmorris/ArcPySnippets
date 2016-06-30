mxdName = "Editing.mxd"

import psutil
pidList = psutil.pids()

for pidID in pidList:
    process = psutil.Process(pidID)
    pidName = process.name()
    if (pidName == "ArcMap.exe"):       #Process only the ArcMap.exe processes
        #print("\n\n" + str(process.pid))

        #Get the process memory map
        tMemMaps = process.memory_maps() # returns a list of tuples
        for eachMemMap in tMemMaps:
            #print(eachMemMap)
            mxdPresent = eachMemMap[0].find(mxdName)
            if mxdPresent > -1:
                #print eachMemMap[0]
                process.kill()      # Close the desired ArcMap process
                break
print(mxdName + " has been closed down")
