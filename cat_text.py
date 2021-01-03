import glob
import os

file_integrate = 15

def NER(file_integrate):
    f1 = glob.glob("../../../ENER/Event/ENEs/Competition/*.NE")
    f2 = glob.glob("../../../ENER/Event/ENEs/Election/*.NE")
    f3 = glob.glob("../../../ENER/Event/ENEs/Flood_Damage/*.NE")
    f4 = glob.glob("../../../ENER/Event/ENEs/Religious_Festival/*.NE")
    f5 = glob.glob("../../../ENER/Event/ENEs/Conference/*.NE")
    f6 = glob.glob("../../../ENER/Event/ENEs/Event_Other/*.NE")
    f7 = glob.glob("../../../ENER/Event/ENEs/Incident_Other/*.NE")
    f8 = glob.glob("../../../ENER/Event/ENEs/Traffic_Accident/*.NE")
    f9 = glob.glob("../../../ENER/Event/ENEs/Earthquake/*.NE")
    f10 = glob.glob("../../../ENER/Event/ENEs/Exhibition/*.NE")
    f11 = glob.glob("../../../ENER/Event/ENEs/Occasion_Other/*.NE")
    f12 = glob.glob("../../../ENER/Event/ENEs/War/*.NE")

    all = []
    for i in range(file_integrate):
        all.append(f1[i])
        all.append(f2[i])
        all.append(f3[i])
        all.append(f4[i])
        all.append(f5[i])
        all.append(f6[i])
        all.append(f7[i])
        all.append(f8[i])
        all.append(f9[i])
        all.append(f10[i])
        all.append(f11[i])
        all.append(f12[i])
    all_str = ' '.join(all)
    cmd = f"cat {all_str} > ./NER/all{file_integrate}.NE"
    os.system(cmd)

def ENER(file_integrate):
    f1 = glob.glob("../../../ENER/Event/plain/Competition/*.ENE")
    f2 = glob.glob("../../../ENER/Event/plain/Election/*.ENE")
    f3 = glob.glob("../../../ENER/Event/plain/Flood_Damage/*.ENE")
    f4 = glob.glob("../../../ENER/Event/plain/Religious_Festival/*.ENE")
    f5 = glob.glob("../../../ENER/Event/plain/Conference/*.ENE")
    f6 = glob.glob("../../../ENER/Event/plain/Event_Other/*.ENE")
    f7 = glob.glob("../../../ENER/Event/plain/Incident_Other/*.ENE")
    f8 = glob.glob("../../../ENER/Event/plain/Traffic_Accident/*.ENE")
    f9 = glob.glob("../../../ENER/Event/plain/Earthquake/*.ENE")
    f10 = glob.glob("../../../ENER/Event/plain/Exhibition/*.ENE")
    f11 = glob.glob("../../../ENER/Event/plain/Occasion_Other/*.ENE")
    f12 = glob.glob("../../../ENER/Event/plain/War/*.ENE")

    all = []
    for i in range(file_integrate):
        all.append(f1[i])
        all.append(f2[i])
        all.append(f3[i])
        all.append(f4[i])
        all.append(f5[i])
        all.append(f6[i])
        all.append(f7[i])
        all.append(f8[i])
        all.append(f9[i])
        all.append(f10[i])
        all.append(f11[i])
        all.append(f12[i])
    all_str = ' '.join(all)
    cmd = f"cat {all_str} > ./ENER/all{file_integrate}.ENE"
    os.system(cmd)

NER(file_integrate)
# ENER(file_integrate)