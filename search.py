import os

def getCurrentPathList(rootDir, keyword, dict={}):
    
    if rootDir not in dict:
        dict[rootDir] = 0

    if os.path.isfile(rootDir):
        return dict
    else:
        pathList = os.listdir(rootDir)
        for x in pathList:
            newPath = os.path.join(rootDir, x)

            if os.path.islink(newPath):
                print("Link: ", newPath)
            elif os.path.isdir(newPath):
                getCurrentPathList(newPath, keyword, dict)
            else:
                dict[rootDir] += 1
                
    print('Dict: ', dict)
    return dict
