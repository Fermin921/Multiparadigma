# Modulos
import csv
import random

def split(inputFile,outPutName,lines):
    with open(inputFile,'r,') as file: #Ejecuta salida y entrada
        header = file.readline().strip() #Quita los espacios strip
        outputFile = None
        lineCount = 0
        for line in file :
            if lineCount % lines == 0:
                if outputFile is not None:
                    outputFile.close()
                outputFile = open(f"{outPutName}_{lineCount//lines}.csv",'w')
                outputFile.write(header + '\n')
            outputFile.write(line)
            lineCount+=1
        if outputFile is not None:
            outputFile.close()

if __name__ == "__main__":
    pass