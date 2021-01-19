import glob
import os

def NER(start,end,sw):
    f1 = glob.glob("../../../ENER/Event/ENE_lim20/Competition/*.NE")
    f2 = glob.glob("../../../ENER/Event/ENE_lim20/Election/*.NE")
    f3 = glob.glob("../../../ENER/Event/ENE_lim20/Flood_Damage/*.NE")
    f4 = glob.glob("../../../ENER/Event/ENE_lim20/Religious_Festival/*.NE")
    f5 = glob.glob("../../../ENER/Event/ENE_lim20/Conference/*.NE")
    f6 = glob.glob("../../../ENER/Event/ENE_lim20/Event_Other/*.NE")
    f7 = glob.glob("../../../ENER/Event/ENE_lim20/Incident_Other/*.NE")
    f8 = glob.glob("../../../ENER/Event/ENE_lim20/Traffic_Accident/*.NE")
    f9 = glob.glob("../../../ENER/Event/ENE_lim20/Earthquake/*.NE")
    f10 = glob.glob("../../../ENER/Event/ENE_lim20/Exhibition/*.NE")
    f11 = glob.glob("../../../ENER/Event/ENE_lim20/Occasion_Other/*.NE")
    f12 = glob.glob("../../../ENER/Event/ENE_lim20/War/*.NE")

    all = []
    for i in range(start,end):
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
    prt = f"{end-start}_{sw}"
    cmd = f"cat {all_str} > ./NER/all{prt}_NE.conll"
    os.system(cmd)

def ENER(start,end,sw):
#    ENER/Event/ENE_lim20/ENEtext_list/1.9.0
    f1 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.0/*.ENE")
    f2 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.1.0/*.ENE")
    f3 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.1.1/*.ENE")
    f4 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.1.2/*.ENE")
    f5 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.1.3/*.ENE")
    f6 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.1.4/*.ENE")
    f7 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.1.5/*.ENE")
    f8 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.2.0/*.ENE")
    f9 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.2.1/*.ENE")
    f10 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.2.2/*.ENE")
    f11 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.4.1/*.ENE")
    f12 = glob.glob("../../../ENER/Event/ENE_lim20/ENEtext_list/1.9.4.2/*.ENE")

    all = []
    for i in range(start,end):
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
    prt = f"{end-start}_{sw}"
    cmd = f"cat {all_str} > ./ENER/all{prt}_ENE.conll"
    os.system(cmd)

# NER(file_integrate)
# ENER(file_integrate)
def main():
    flag = 1
    if flag == 0:
        NER(0,10,"A")
        NER(10,20,"B")
    else:
        ENER(0,1,"TEST")
#        ENER(10,20,"B")
main()
