# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:39:13 2020

@author: Hp
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


# Importing the dataset
dataset = pd.read_csv('ThesisPred.csv')

b=dataset.shape
print(b[0])
columnNumber=b[0]

####################
#### VenueIndexing #####
"""=IF(S2="M Chinnaswamy Stadium",1,IF(S2="MA Chidambaram Stadium",2,
IF(S2="Punjab Cricket Association IS Bindra Stadium",3,IF(S2="Sawai Mansingh Stadium",4,IF(S2="Eden Gardens",5,
IF(S2="Wankhede Stadium",6,IF(S2="Maharashtra Cricket Association Stadium",7,
IF(S2="Arun Jaitley Stadium",8,IF(S2="Rajiv Gandhi International Stadium",9,
IF(S2="JSCA International Stadium Complex",10,IF(S2="Sharjah Cricket Stadium",11,
IF(S2="Dubai International Cricket Stadium",12,IF(S2="Sheikh Zayed Stadium",13,
IF(S2="Sardar Patel Stadium",14,IF(S2="Shaheed Veer Narayan Sing International Stadium",15,
IF(S2="Saurashtra Cricket Association Stadium",16,IF(S2="Holkar Cricket Stadium",17,0)))))))))))))))))"""
#####################


for i in range(0,columnNumber):
    y=dataset.at[i,'Venue']
    if(y=="M Chinnaswamy Stadium"):
        
        dataset.at[i,'VenueIndex']=1
    elif(y=="MA Chidambaram Stadium"):
     
        dataset.at[i,'VenueIndex']=2
    elif(y=="Punjab Cricket Association IS Bindra Stadium"):
     
        dataset.at[i,'VenueIndex']=3
    elif(y=="Sawai Mansingh Stadium"):
      
        dataset.at[i,'VenueIndex']=4
    elif(y=="Eden Gardens"):
       
        dataset.at[i,'VenueIndex']=5
    elif(y=="Wankhede Stadium"):
     
        dataset.at[i,'VenueIndex']=6
    elif(y=="Maharashtra Cricket Association Stadium"):
  
        dataset.at[i,'VenueIndex']=7
    elif(y=="Arun Jaitley Stadium"):
     
        dataset.at[i,'VenueIndex']=8
    elif(y=="Rajiv Gandhi International Stadium"):
  
        dataset.at[i,'VenueIndex']=9
    elif(y=="JSCA International Stadium Complex"):
   
        dataset.at[i,'VenueIndex']=10
    elif(y=="Sharjah Cricket Stadium"):
    
        dataset.at[i,'VenueIndex']=11
    elif(y=="Dubai International Cricket Stadium"):
      
        dataset.at[i,'VenueIndex']=12
    elif(y=="Sheikh Zayed Stadium"):
      
        dataset.at[i,'VenueIndex']=13
    elif(y=="Sardar Patel Stadium"):
      
        dataset.at[i,'VenueIndex']=14
    elif(y=="Shaheed Veer Narayan Sing International Stadium"):
    
        dataset.at[i,'VenueIndex']=15
    elif(y=="Saurashtra Cricket Association Stadium"):
      
        dataset.at[i,'VenueIndex']=16
    elif(y=="Holkar Cricket Stadium"):
      
        dataset.at[i,'VenueIndex']=17
    elif(y=="ACA-VDCA"):
      
        dataset.at[i,'VenueIndex']=18
    elif(y=="Barabati Stadium"):
      
        dataset.at[i,'VenueIndex']=19
    elif(y=="Brabourne Stadium"):
      
        dataset.at[i,'VenueIndex']=20
    elif(y=="DY Patil Stadium"):
      
        dataset.at[i,'VenueIndex']=21
    elif(y=="Feroz Shah Kotla Ground"):
      
        dataset.at[i,'VenueIndex']=22
    elif(y=="Green Park Stadium"):
      
        dataset.at[i,'VenueIndex']=23
    elif(y=="HPCA Stadium"):
      
        dataset.at[i,'VenueIndex']=24
    elif(y=="Jawaharlal Nehru Stadium"):
      
        dataset.at[i,'VenueIndex']=25
    elif(y=="Holkar Cricket Stadium"):
      
        dataset.at[i,'VCA Stadium']=26 
        
    else:
        dataset.at[i,'VenueIndex']=27



################################
################################

#Calculation of VenueExp
cnt1=0
cnt2=0
cnt3=0
cnt4=0
cnt5=0
cnt6=0
cnt7=0
cnt8=0
cnt9=0
cnt10=0
cnt11=0
cnt12=0
cnt13=0
cnt14=0
cnt15=0
cnt16=0
cnt17=0


for i in range(0,columnNumber):
    x=dataset.at[i,'VenueIndex']
    if(x==1):
        cnt1=cnt1+1
        dataset.at[i,'VenueExp']=cnt1
    elif(x==2):
        cnt2=cnt2+1
        dataset.at[i,'VenueExp']=cnt2
    elif(x==3):
        cnt3=cnt3+1
        dataset.at[i,'VenueExp']=cnt3
    elif(x==4):
        cnt4=cnt4+1
        dataset.at[i,'VenueExp']=cnt4
    elif(x==5):
        cnt5=cnt5+1
        dataset.at[i,'VenueExp']=cnt5
    elif(x==6):
        cnt6=cnt6+1
        dataset.at[i,'VenueExp']=cnt6
    elif(x==7):
        cnt7=cnt7+1
        dataset.at[i,'VenueExp']=cnt7
    elif(x==8):
        cnt8=cnt8+1
        dataset.at[i,'VenueExp']=cnt8
    elif(x==9):
        cnt9=cnt9+1
        dataset.at[i,'VenueExp']=cnt9
    elif(x==10):
        cnt10=cnt10+1
        dataset.at[i,'VenueExp']=cnt10
    elif(x==11):
        cnt11=cnt11+1
        dataset.at[i,'VenueExp']=cnt11
    elif(x==12):
        cnt12=cnt12+1
        dataset.at[i,'VenueExp']=cnt12
    elif(x==13):
        cnt13=cnt13+1
        dataset.at[i,'VenueExp']=cnt13
    elif(x==14):
        cnt14=cnt14+1
        dataset.at[i,'VenueExp']=cnt14
    elif(x==15):
        cnt15=cnt15+1
        dataset.at[i,'VenueExp']=cnt15
    elif(x==16):
        cnt16=cnt16+1
        dataset.at[i,'VenueExp']=cnt16
    elif(x==17):
        cnt17=cnt17+1
        dataset.at[i,'VenueExp']=cnt17
    else:
        dataset.at[i,'VenueExp']=1
    

################################
        """Opposition Indexing"""
################################
for i in range(0,columnNumber):
    y=dataset.at[i,'Vs']
    if(y=="Delhi Capitals"):
        
        dataset.at[i,'OppositionIndex']=1
    elif(y=="Kolkata Knight Riders"):
     
        dataset.at[i,'OppositionIndex']=2
    elif(y=="Chennai Super Kings"):
     
        dataset.at[i,'OppositionIndex']=3
    elif(y=="Rajasthan Royals"):
      
        dataset.at[i,'OppositionIndex']=4
    elif(y=="Pune Warriors"):
       
        dataset.at[i,'OppositionIndex']=5
    elif(y=="Kings XI Punjab"):
     
        dataset.at[i,'OppositionIndex']=6
    elif(y=="Deccan Chargers"):
  
        dataset.at[i,'OppositionIndex']=7
    elif(y=="Mumbai Indians"):
     
        dataset.at[i,'OppositionIndex']=8
    elif(y=="Sunrisers Hyderabad"):
  
        dataset.at[i,'OppositionIndex']=9
    elif(y=="Rising Pune Supergiant"):
   
        dataset.at[i,'OppositionIndex']=10
    elif(y=="Gujarat Lions"):
    
        dataset.at[i,'OppositionIndex']=11
    else:
        dataset.at[i,'VenueIndex']=0

#create new dataframe using the values of csv file
#df = pd.DataFrame(dataset, columns = ['Venue', 'VenueExp'])


#df = pd.DataFrame(initial_data, columns = ['First_name', 'Last_name', 'Marks'])   
# Generate result using pandas 
#result = [] 
#for value in df["Marks"]: 
#    if value >= 33: 
#        result.append("Pass") 
#    elif value < 0 and value > 100: 
#        result.append("Invalid") 
#    else: 
#        result.append("Fail") 
#df["Result"] = result    
#print(df) 


################################
################################


#New Table
df=pd.DataFrame(dataset,columns=['Match','TotalRuns','Runs','Balls','Out','TotalOut',
                                 'Average','Sr','Fifty','TotalFifty',
                                 'Hundred','TotalHundred','Dot','VenueIndex'
                                 ,'VenueExp','OppositionIndex'])





################################
################################

#Number of Rows
a=df.shape
print(a[0])
columnNum=a[0]



########Opposition Experience

ex1=0
ex2=0
ex3=0
ex4=0
ex5=0
ex6=0
ex7=0
ex8=0
ex9=0
ex10=0
ex11=0
OppositionExp=[]   
for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if(val==1):
            ex1=ex1+1
            OppositionExp.append(ex1)
    elif(val==2):
            ex2=ex2+1
            OppositionExp.append(ex2)
    elif(val==3):
            ex3=ex3+1
            OppositionExp.append(ex3)
    elif(val==4):
            ex4=ex4+1
            OppositionExp.append(ex4)
    elif(val==5):
            ex5=ex5+1
            OppositionExp.append(ex5)
    elif(val==6):
            ex6=ex6+1
            OppositionExp.append(ex6)
    elif(val==7):
            ex7=ex7+1
            OppositionExp.append(ex7)
    elif(val==8):
            ex8=ex8+1
            OppositionExp.append(ex8)
    elif(val==9):
            ex9=ex9+1
            OppositionExp.append(ex9)
    elif(val==10):
            ex10=ex10+1
            OppositionExp.append(ex10)
    elif(val==11):
            ex11=ex11+1
            OppositionExp.append(ex11)
    else:
            OppositionExp.append(0)
df["OppositionExp"] = OppositionExp   

################################
################################



#For NoOfInningsConsistency
MatchCon=[]
for value in df["Match"]:
    if value>=0 and value<=48:
        MatchCon.append(1)
    elif value>=49 and value<=98:
        MatchCon.append(2)
    elif value>=99 and value<=123:
        MatchCon.append(3)
    elif value>=124 and value<=148:
        MatchCon.append(4)
    elif value>=149 :
        MatchCon.append(5)
df["MatchCon"] = MatchCon   




################################
################################




#For NoOfInningsForm
MatchForm=[]
for value in df["Match"]:
    if value>=0 and value<=3:
        MatchForm.append(1)
    elif value>=4 and value<=8:
        MatchForm.append(2)
    elif value>=9 and value<=10:
        MatchForm.append(3)
    elif value>=11 and value<=13:
        MatchForm.append(4)
    elif value>=14 :
        MatchForm.append(5)
df["MatchForm"] = MatchForm   





################################
################################



#For NoOfInningsVenue
MatchVen=[]
for value in df["VenueExp"]:
    if value==1:
        MatchVen.append(1)
    elif value==2:
        MatchVen.append(2)
    elif value==3:
        MatchVen.append(3)
    elif value==4:
        MatchVen.append(4)
    elif value>=5 :
        MatchVen.append(5)
df["MatchVen"] = MatchVen 


################################
################################



#For NoOfInningsOpposition
MatchOpp=[]
for value in df["OppositionExp"]:
    if value>=0 and value<=2:
        MatchOpp.append(1)
    elif value>=3 and value<=4:
        MatchOpp.append(2)
    elif value>=5 and value<=6:
        MatchOpp.append(3)
    elif value>=7 and value<=9:
        MatchOpp.append(4)
    elif value>=10 :
        MatchOpp.append(5)
df["MatchOpp"] = MatchOpp 


################################
################################



#Calculation of Average
CalAvg=[]
for i in range(0,columnNum):
    #CalAvg.append(math.floor((df.at[i,'TotalRuns']/df.at[i,'TotalOut'])))
    CalAvg.append(df.at[i,'TotalRuns']/df.at[i,'TotalOut'])
df["CalAvg"]=CalAvg




################################
################################


#Calculation of SR
CalSR=[]
for i in range(0,columnNum):
    #CalAvg.append(math.floor((df.at[i,'TotalRuns']/df.at[i,'TotalOut'])))
    CalSR.append((df.at[i,'Runs']/df.at[i,'Balls'])*100)
df["CalSR"]=CalSR



################################
################################




#Calculation of Fifty
CalFifty=[]
for i in range(0,columnNum):
    if ((df.at[i,'Runs']>=50) and (df.at[i,'Runs']<100)):
        CalFifty.append(1)
    else:
        CalFifty.append(0) 
df["CalFifty"]=CalFifty


#Number of Fifties
fiftycount=0
NumFifty=[]
for i in range(0,columnNum):
    if (df.at[i,'CalFifty']==1):
        fiftycount=fiftycount+1
        NumFifty.append(fiftycount)
    else:
        NumFifty.append(fiftycount)
df["NumFifty"]=NumFifty
#Rating For Fifty for Consistency
FiftyCon=[]
for value in df["NumFifty"]: 
     if value==0:
        FiftyCon.append(0)
     if value>=1 and value<=9:
        FiftyCon.append(1)
     elif value>=10 and value<=19:
        FiftyCon.append(2)
     elif value>=20 and value<=29:
        FiftyCon.append(3)
     elif value>=30 and value<=39:
        FiftyCon.append(4)
     elif value>=40 :
        FiftyCon.append(5)
df["FiftyCon"] = FiftyCon    

#Rating For Fifty for Form
FiftyForm=[]
for value in df["NumFifty"]: 
     if value==0:
        FiftyForm.append(0)
     if value>=1 and value<=2:
        FiftyForm.append(1)
     elif value>=3 and value<=4:
        FiftyForm.append(2)
     elif value>=5 and value<=6:
        FiftyForm.append(3)
     elif value>=7 and value<=9:
        FiftyForm.append(4)
     elif value>=10 :
        FiftyForm.append(5)
df["FiftyForm"] = FiftyForm  



#Fifties In Particular Venue
fven1=0
fven2=0
fven3=0
fven4=0
fven5=0
fven6=0
fven7=0
fven8=0
fven9=0
fven10=0
fven11=0
fven12=0
fven13=0
fven14=0
fven15=0
fven16=0
fven17=0
VenueFifty=[]   
for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if (df.at[i,'CalFifty']==1):
        if(val==1):
            fven1=fven1+1
            VenueFifty.append(fven1)
        elif(val==2):
            fven2=fven2+1
            VenueFifty.append(fven2)
        elif(val==3):
            fven3=fven3+1
            VenueFifty.append(fven3)
        elif(val==4):
            fven4=fven4+1
            VenueFifty.append(fven4)
        elif(val==5):
            fven5=fven5+1
            VenueFifty.append(fven5)
        elif(val==6):
            fven6=fven6+1
            VenueFifty.append(fven6)
        elif(val==7):
            fven7=fven7+1
            VenueFifty.append(fven7)
        elif(val==8):
            fven8=fven8+1
            VenueFifty.append(fven8)
        elif(val==9):
            fven9=fven9+1
            VenueFifty.append(fven9)
        elif(val==10):
            fven10=fven10+1
            VenueFifty.append(fven10)
        elif(val==11):
            fven11=fven11+1
            VenueFifty.append(fven11)
        elif(val==12):
            fven12=fven12+1
            VenueFifty.append(fven12)
        elif(val==13):
            fven13=fven13+1
            VenueFifty.append(fven13)
        elif(val==14):
            fven14=fven14+1
            VenueFifty.append(fven14)
        elif(val==15):
            fven15=fven15+1
            VenueFifty.append(fven15)
        elif(val==16):
            fven16=fven16+1
            VenueFifty.append(fven16)
        elif(val==17):
            fven17=fven17+1
            VenueFifty.append(fven17)
    elif(df.at[i,'CalFifty']==0):
        if(val==1):
            VenueFifty.append(fven1)
        elif(val==2):          
            VenueFifty.append(fven2)
        elif(val==3):         
            VenueFifty.append(fven3)
        elif(val==4):            
            VenueFifty.append(fven4)
        elif(val==5):           
            VenueFifty.append(fven5)
        elif(val==6):           
            VenueFifty.append(fven6)
        elif(val==7):         
            VenueFifty.append(fven7)
        elif(val==8):       
            VenueFifty.append(fven8)
        elif(val==9):           
            VenueFifty.append(fven9)
        elif(val==10):           
            VenueFifty.append(fven10)
        elif(val==11):           
            VenueFifty.append(fven11)
        elif(val==12):        
            VenueFifty.append(fven12)
        elif(val==13):         
            VenueFifty.append(fven13)
        elif(val==14):            
            VenueFifty.append(fven14)
        elif(val==15):         
            VenueFifty.append(fven15)
        elif(val==16):           
            VenueFifty.append(fven16)
        elif(val==17):         
            VenueFifty.append(fven17)
        else:
            VenueFifty.append(0)
   
df["VenueFifty"]=VenueFifty

#Rating For Fifty for Venue
FiftyVenue=[]
for value in df["VenueFifty"]: 
     if value==0:
        FiftyVenue.append(0)
     if value==1 :
        FiftyVenue.append(3)
     elif value==2:
        FiftyVenue.append(4)
     elif value>=3:
        FiftyVenue.append(5)
df["FiftyVenue"] = FiftyVenue  


##Fifties against a particular opposition
fopp1=0
fopp2=0
fopp3=0
fopp4=0
fopp5=0
fopp6=0
fopp7=0
fopp8=0
fopp9=0
fopp10=0
fopp11=0

OppFifty=[]   
for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if (df.at[i,'CalFifty']==1):
        if(val==1):
            fopp1=fopp1+1
            OppFifty.append(fopp1)
        elif(val==2):
            fopp2=fopp2+1
            OppFifty.append(fopp2)
        elif(val==3):
            fopp3=fopp3+1
            OppFifty.append(fopp3)
        elif(val==4):
            fopp4=fopp4+1
            OppFifty.append(fopp4)
        elif(val==5):
            fopp5=fopp5+1
            OppFifty.append(fopp5)
        elif(val==6):
            fopp6=fopp6+1
            OppFifty.append(fopp6)
        elif(val==7):
            fopp7=fopp7+1
            OppFifty.append(fopp7)
        elif(val==8):
            fopp8=fopp8+1
            OppFifty.append(fopp8)
        elif(val==9):
            fopp9=fopp9+1
            OppFifty.append(fopp9)
        elif(val==10):
            fopp10=fopp10+1
            OppFifty.append(fopp10)
        elif(val==11):
            fopp11=fopp11+1
            OppFifty.append(fopp11)
       
    elif(df.at[i,'CalFifty']==0):
        if(val==1):
            OppFifty.append(fopp1)
        elif(val==2):          
            OppFifty.append(fopp2)
        elif(val==3):         
            OppFifty.append(fopp3)
        elif(val==4):            
            OppFifty.append(fopp4)
        elif(val==5):           
            OppFifty.append(fopp5)
        elif(val==6):           
            OppFifty.append(fopp6)
        elif(val==7):         
            OppFifty.append(fopp7)
        elif(val==8):       
            OppFifty.append(fopp8)
        elif(val==9):           
            OppFifty.append(fopp9)
        elif(val==10):           
            OppFifty.append(fopp10)
        elif(val==11):           
            OppFifty.append(fopp11)
       
        else:
            OppFifty.append(0)
   
    
df["OppFifty"]=OppFifty


    
#Rating For Fifty for Opposition
FiftyOppRating=[]
for value in df["OppFifty"]: 
     if value==0:
        FiftyOppRating.append(0)
     if value==1 :
        FiftyOppRating.append(3)
     elif value==2:
        FiftyOppRating.append(4)
     elif value>=3:
        FiftyOppRating.append(5)
df["FiftyOppRating"] = FiftyOppRating      
    
    
    
    
    
    


################################
################################



#Calculation of Hundred
CalHundred=[]
for i in range(0,columnNum):
    if ((df.at[i,'Runs']>=100) and (df.at[i,'Runs']<200)):
        CalHundred.append(1)
    else:
        CalHundred.append(0) 
df["CalHundred"]=CalHundred

#Number of Hundred
Hundredcount=0
NumHundred=[]
for i in range(0,columnNum):
    if (df.at[i,'CalHundred']==1):
        Hundredcount=Hundredcount+1
        NumHundred.append(Hundredcount)
    else:
        NumHundred.append(Hundredcount)
df["NumHundred"]=NumHundred


#Rating For Hundred for Consistency
HundredCon=[]
for value in df["NumHundred"]: 
     if value==0:
        HundredCon.append(0)
     if value>=1 and value<=3:
        HundredCon.append(1)
     elif value>=4 and value<=6:
        HundredCon.append(2)
     elif value>=7 and value<=9:
        HundredCon.append(3)
     elif value>=10 and value<=12:
        HundredCon.append(4)
     elif value>=13 :
        HundredCon.append(5)
df["HundredCon"] = HundredCon    

#Rating For Century for Form
CenturyForm=[]
for value in df["NumHundred"]: 
     if value==0:
       CenturyForm.append(0)
     if value==1:
        CenturyForm.append(1)
     elif value==2:
        CenturyForm.append(2)
     elif value==3:
        CenturyForm.append(3)
     elif value==4:
        CenturyForm.append(4)
     elif value>=5 :
        CenturyForm.append(5)
df["CenturyForm"] = CenturyForm  

#Hundreds In Particular Venue
hven1=0
hven2=0
hven3=0
hven4=0
hven5=0
hven6=0
hven7=0
hven8=0
hven9=0
hven10=0
hven11=0
hven12=0
hven13=0
hven14=0
hven15=0
hven16=0
hven17=0
VenueHundred=[]   
for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if (df.at[i,'CalHundred']==1):
        if(val==1):
            hven1=hven1+1
            VenueHundred.append(hven1)
        elif(val==2):
            hven2=hven2+1
            VenueHundred.append(hven2)
        elif(val==3):
            hven3=hven3+1
            VenueHundred.append(hven3)
        elif(val==4):
            hven4=hven4+1
            VenueHundred.append(hven4)
        elif(val==5):
            hven5=hven5+1
            VenueHundred.append(hven5)
        elif(val==6):
            hven6=hven6+1
            VenueHundred.append(hven6)
        elif(val==7):
            hven7=hven7+1
            VenueHundred.append(hven7)
        elif(val==8):
            hven8=hven8+1
            VenueHundred.append(hven8)
        elif(val==9):
            hven9=hven9+1
            VenueHundred.append(hven9)
        elif(val==10):
            hven10=hven10+1
            VenueHundred.append(hven10)
        elif(val==11):
            hven11=hven11+1
            VenueHundred.append(hven11)
        elif(val==12):
            hven12=hven12+1
            VenueHundred.append(hven12)
        elif(val==13):
            hven13=hven13+1
            VenueHundred.append(hven13)
        elif(val==14):
            hven14=hven14+1
            VenueHundred.append(hven14)
        elif(val==15):
            hven15=hven15+1
            VenueHundred.append(hven15)
        elif(val==16):
            hven16=hven16+1
            VenueHundred.append(hven16)
        elif(val==17):
            hven17=hven17+1
            VenueHundred.append(hven17)
    elif(df.at[i,'CalHundred']==0):
        if(val==1):
            VenueHundred.append(hven1)
        elif(val==2):          
            VenueHundred.append(hven2)
        elif(val==3):         
            VenueHundred.append(hven3)
        elif(val==4):            
            VenueHundred.append(hven4)
        elif(val==5):           
            VenueHundred.append(hven5)
        elif(val==6):           
            VenueHundred.append(hven6)
        elif(val==7):         
            VenueHundred.append(hven7)
        elif(val==8):       
            VenueHundred.append(hven8)
        elif(val==9):           
            VenueHundred.append(hven9)
        elif(val==10):           
            VenueHundred.append(hven10)
        elif(val==11):           
            VenueHundred.append(hven11)
        elif(val==12):        
            VenueHundred.append(hven12)
        elif(val==13):         
            VenueHundred.append(hven13)
        elif(val==14):            
            VenueHundred.append(hven14)
        elif(val==15):         
            VenueHundred.append(hven15)
        elif(val==16):           
            VenueHundred.append(hven16)
        elif(val==17):         
            VenueHundred.append(hven17)
        else:
            VenueHundred.append(0)
   
df["VenueHundred"]=VenueHundred

#Rating For Hundred for Venue
HundredVenueRating=[]
for value in df["VenueHundred"]: 
     if value==0:
      HundredVenueRating.append(0)
     if value==1 :
        HundredVenueRating.append(4)
     elif value>=2:
        HundredVenueRating.append(5)
df["HundredVenueRating"] = HundredVenueRating 


##Hundreds against a particular opposition
hopp1=0
hopp2=0
hopp3=0
hopp4=0
hopp5=0
hopp6=0
hopp7=0
hopp8=0
hopp9=0
hopp10=0
hopp11=0

OppHundred=[]   
for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if (df.at[i,'CalHundred']==1):
        if(val==1):
            hopp1=hopp1+1
            OppHundred.append(hopp1)
        elif(val==2):
            hopp2=hopp2+1
            OppHundred.append(hopp2)
        elif(val==3):
            hopp3=hopp3+1
            OppHundred.append(hopp3)
        elif(val==4):
            hopp4=hopp4+1
            OppHundred.append(hopp4)
        elif(val==5):
            hopp5=hopp5+1
            OppHundred.append(hopp5)
        elif(val==6):
            hopp6=hopp6+1
            OppHundred.append(hopp6)
        elif(val==7):
            hopp7=hopp7+1
            OppHundred.append(hopp7)
        elif(val==8):
            hopp8=hopp8+1
            OppHundred.append(hopp8)
        elif(val==9):
            hopp9=hopp9+1
            OppHundred.append(hopp9)
        elif(val==10):
            hopp10=hopp10+1
            OppHundred.append(hopp10)
        elif(val==11):
            hopp11=hopp11+1
            OppHundred.append(hopp11)
       
    elif(df.at[i,'CalHundred']==0):
        if(val==1):
            OppHundred.append(hopp1)
        elif(val==2):          
            OppHundred.append(hopp2)
        elif(val==3):         
            OppHundred.append(hopp3)
        elif(val==4):            
            OppHundred.append(hopp4)
        elif(val==5):           
            OppHundred.append(hopp5)
        elif(val==6):           
            OppHundred.append(hopp6)
        elif(val==7):         
            OppHundred.append(hopp7)
        elif(val==8):       
            OppHundred.append(hopp8)
        elif(val==9):           
            OppHundred.append(hopp9)
        elif(val==10):           
            OppHundred.append(hopp10)
        elif(val==11):           
            OppHundred.append(hopp11)
       
        else:
            OppHundred.append(0)
   
df["OppHundred"]=OppHundred


#Rating For Hundred for Opposition
HundredOppRating=[]
for value in df["OppHundred"]: 
     if value==0:
      HundredOppRating.append(0)
     if value==1 :
        HundredOppRating.append(3)
     elif value==2 :
        HundredOppRating.append(4)
     elif value>=3:
        HundredOppRating.append(5)
df["HundredOppRating"] = HundredOppRating 

################################
################################





#Calculation of Zero
CalZero=[]
for i in range(0,columnNum):
    if (df.at[i,'Runs']==0):
        CalZero.append(1)
    else:
        CalZero.append(0) 
df["CalZero"]=CalZero

#Number of Hundred
Zerocount=0
NumZero=[]
for i in range(0,columnNum):
    if (df.at[i,'CalZero']==1):
        Zerocount=Zerocount+1
        NumZero.append(Zerocount)
    else:
        NumZero.append(Zerocount)
df["NumZero"]=NumZero


#Rating For Zero for Consistency
ZeroCon=[]
for value in df["NumZero"]: 
     if value==0:
        ZeroCon.append(0)
     if value>=1 and value<=4:
        ZeroCon.append(1)
     elif value>=5 and value<=9:
        ZeroCon.append(2)
     elif value>=10 and value<=14:
        ZeroCon.append(3)
     elif value>=15 and value<=19:
        ZeroCon.append(4)
     elif value>=20 :
        ZeroCon.append(5)
df["ZeroCon"] = ZeroCon    

#Rating For Zero for Form
ZeroForm=[]
for value in df["NumZero"]: 
     if value==0:
        ZeroForm.append(0)
     if value==1:
        ZeroForm.append(1)
     elif value==2:
       ZeroForm.append(2)
     elif value==3:
        ZeroForm.append(3)
     elif value==4:
        ZeroForm.append(4)
     elif value>=5 :
        ZeroForm.append(5)
df["ZeroForm"] =ZeroForm


##Zero against a particular opposition
zopp1=0
zopp2=0
zopp3=0
zopp4=0
zopp5=0
zopp6=0
zopp7=0
zopp8=0
zopp9=0
zopp10=0
zopp11=0

OppZero=[]   
for i in range(0,columnNum):
    val=df.at[i,'OppositionIndex']
    if (df.at[i,'CalZero']==1):
        if(val==1):
            zopp1=zopp1+1
            OppZero.append(zopp1)
        elif(val==2):
            zopp2=zopp2+1
            OppZero.append(zopp2)
        elif(val==3):
            zopp3=zopp3+1
            OppZero.append(zopp3)
        elif(val==4):
            zopp4=zopp4+1
            OppZero.append(zopp4)
        elif(val==5):
            zopp5=zopp5+1
            OppZero.append(zopp5)
        elif(val==6):
            zopp6=zopp6+1
            OppZero.append(zopp6)
        elif(val==7):
            zopp7=zopp7+1
            OppZero.append(zopp7)
        elif(val==8):
            zopp8=zopp8+1
            OppZero.append(zopp8)
        elif(val==9):
            zopp9=zopp9+1
            OppZero.append(zopp9)
        elif(val==10):
            zopp10=zopp10+1
            OppZero.append(zopp10)
        elif(val==11):
            zopp11=zopp11+1
            OppZero.append(zopp11)
       
    elif(df.at[i,'CalZero']==0):
        if(val==1):
            OppZero.append(zopp1)
        elif(val==2):          
            OppZero.append(zopp2)
        elif(val==3):         
            OppZero.append(zopp3)
        elif(val==4):            
            OppZero.append(zopp4)
        elif(val==5):           
            OppZero.append(zopp5)
        elif(val==6):           
            OppZero.append(zopp6)
        elif(val==7):         
            OppZero.append(zopp7)
        elif(val==8):       
            OppZero.append(zopp8)
        elif(val==9):           
            OppZero.append(zopp9)
        elif(val==10):           
            OppZero.append(zopp10)
        elif(val==11):           
            OppZero.append(zopp11)
       
        else:
            OppZero.append(0)
   
df["OppZero"]=OppZero


#Rating For Hundred for Opposition
ZeroOppRating=[]
for value in df["OppZero"]: 
     if value==0:
      ZeroOppRating.append(0)
     if value==1 :
        ZeroOppRating.append(1)
     elif value==2 :
        ZeroOppRating.append(2)
     elif value==3 :
        ZeroOppRating.append(3)
     elif value==4 :
        ZeroOppRating.append(4)
     elif value>=5:
        ZeroOppRating.append(5)
df["ZeroOppRating"] = ZeroOppRating 

################################
################################



#BattingAverage rating For Consistency,form, opposition and venue
AvgRating=[]
for value in df["CalAvg"]:
    if value>=0.0 and value<=5.99:
        AvgRating.append(1/2.8)
    elif value>=6.00 and value<=9.99:
       AvgRating.append(2/2.8)
    elif value>=10.00 and value<=15.99:
        AvgRating.append(3/2.8)
    elif value>=16.00 and value<=19.99:
        AvgRating.append(4/2.8)
    elif value>=20.00 and value<=25.99:
        AvgRating.append(5/2.8)
    elif value>=26.00 and value<=29.99:
        AvgRating.append(6/2.8)
    elif value>=30.00 and value<=35.99:
        AvgRating.append(7/2.8)
    elif value>=36.00 and value<=39.99:
        AvgRating.append(8/2.8)
    elif value>=40.00 and value<=41.99:
        AvgRating.append(9/2.8)
    elif value>=42.00 and value<=43.99:
        AvgRating.append(10/2.8)
    elif value>=44.00 and value<=45.99:
        AvgRating.append(11/2.8)
    elif value>=46.00 and value<=47.99:
        AvgRating.append(12/2.8)
    elif value>=48.00 and value<=49.99:
        AvgRating.append(13/2.8)
    elif value>=50.00 :
        AvgRating.append(14/2.8)
df["AvgRating"] = AvgRating  


################################
################################





#BattingForm rating For Consistency,form, opposition and venue
SrRating=[]
for value in df["CalSR"]:
    if value>=0.0 and value<=49.99:
        SrRating.append(1/2.8)
    elif value>=50.00 and value<=59.99:
       SrRating.append(2/2.8)
    elif value>=60.00 and value<=79.99:
        SrRating.append(3/2.8)
    elif value>=80.00 and value<=99.99:
        SrRating.append(4/2.8)
    elif value>=100.00 and value<=124.99:
        SrRating.append(5/2.8)
    elif value>=125.00 and value<=149.99:
        SrRating.append(6/2.8)
    elif value>=150.00 and value<=174.99:
        SrRating.append(7/2.8)
    elif value>=175.00 and value<=199.99:
        SrRating.append(8/2.8)
    elif value>=200.00 and value<=224.99:
        SrRating.append(9/2.8)
    elif value>=225.00 and value<=249.99:
        SrRating.append(10/2.8)
    elif value>=250.00 and value<=274.99:
        SrRating.append(11/2.8)
    elif value>=275.00 and value<=299.99:
        SrRating.append(12/2.8)
    elif value>=300.00 and value<=324.99:
        SrRating.append(13/2.8)
    elif value>=325.00 :
        SrRating.append(14/2.8)
df["SrRating"] = SrRating  




################################
################################



#########################################################################
############# Highest Score in a Particular Venue Till Match Day#######
############################################################################

hsven1=[]
hsven2=[]
hsven3=[]
hsven4=[]
hsven5=[]
hsven6=[]
hsven7=[]
hsven8=[]
hsven9=[]
hsven10=[]
hsven11=[]
hsven12=[]
hsven13=[]
hsven14=[]
hsven15=[]
hsven16=[]
hsven17=[]



HighestScoreVenue=[]   
for i in range(0,columnNum):
    val=df.at[i,'VenueIndex']
    if(val==1):
        hsven1.append(df.at[i,'Runs'])
        hsven1.sort(reverse=True)
        HighestScoreVenue.append(hsven1[0])
    elif(val==2):
        hsven2.append(df.at[i,'Runs'])
        hsven2.sort(reverse=True)
        HighestScoreVenue.append(hsven2[0])
    elif(val==3):
        hsven3.append(df.at[i,'Runs'])
        hsven3.sort(reverse=True)
        HighestScoreVenue.append(hsven3[0])
    elif(val==4):
        hsven4.append(df.at[i,'Runs'])
        hsven4.sort(reverse=True)
        HighestScoreVenue.append(hsven4[0])
    elif(val==5):
        hsven5.append(df.at[i,'Runs'])
        hsven5.sort(reverse=True)
        HighestScoreVenue.append(hsven5[0])
    elif(val==6):
        hsven6.append(df.at[i,'Runs'])
        hsven6.sort(reverse=True)
        HighestScoreVenue.append(hsven6[0])
    elif(val==7):
        hsven7.append(df.at[i,'Runs'])
        hsven7.sort(reverse=True)
        HighestScoreVenue.append(hsven7[0])
    elif(val==8):
        hsven8.append(df.at[i,'Runs'])
        hsven8.sort(reverse=True)
        HighestScoreVenue.append(hsven8[0])
    elif(val==9):
        hsven9.append(df.at[i,'Runs'])
        hsven9.sort(reverse=True)
        HighestScoreVenue.append(hsven9[0])
    elif(val==10):
        hsven10.append(df.at[i,'Runs'])
        hsven10.sort(reverse=True)
        HighestScoreVenue.append(hsven10[0])
    elif(val==11):
        hsven11.append(df.at[i,'Runs'])
        hsven11.sort(reverse=True)
        HighestScoreVenue.append(hsven11[0])
    elif(val==12):
        hsven12.append(df.at[i,'Runs'])
        hsven12.sort(reverse=True)
        HighestScoreVenue.append(hsven12[0])
    elif(val==13):
        hsven13.append(df.at[i,'Runs'])
        hsven13.sort(reverse=True)
        HighestScoreVenue.append(hsven13[0])
    elif(val==14):
        hsven14.append(df.at[i,'Runs'])
        hsven14.sort(reverse=True)
        HighestScoreVenue.append(hsven14[0])
    elif(val==15):
        hsven15.append(df.at[i,'Runs'])
        hsven15.sort(reverse=True)
        HighestScoreVenue.append(hsven15[0])
    elif(val==16):
        hsven16.append(df.at[i,'Runs'])
        hsven16.sort(reverse=True)
        HighestScoreVenue.append(hsven16[0])
    elif(val==17):
        hsven17.append(df.at[i,'Runs'])
        hsven17.sort(reverse=True)
        HighestScoreVenue.append(hsven17[0])
    
    else:
        HighestScoreVenue.append(0)
   
df["HighestScoreVenue"]=HighestScoreVenue  

############# Rating Of Highest Scores ##############
################################################

HighestScoreRating=[]
for value in df["HighestScoreVenue"]:
    if value==0:
        HighestScoreRating.append(0)
    if value>=1.0 and value<=19.99:
        HighestScoreRating.append(1/1.2)
    elif value>=20.00 and value<=39.99:
        HighestScoreRating.append(2/1.2)
    elif value>=40.00 and value<=59.99:
        HighestScoreRating.append(3/1.2)
    elif value>=60.00 and value<=99.99:
        HighestScoreRating.append(4/1.2)
    elif value>=100.00 and value<=149.99:
        HighestScoreRating.append(5/1.2)
    elif value>=150.00 :
        HighestScoreRating.append(6/1.2)
df["HighestScoreRating"] = HighestScoreRating










#######################################
####              Calculation of Consistency      ############
####################################

ConValue=[]
ConValue.append(0)
df.at[0,'Consistency']=0

for i in range(1,columnNum):
      ConValue.append(0.4262*(df.at[i-1,'AvgRating'])+0.2566*(df.at[i-1,'MatchCon'])+0.1510*(df.at[i-1,'SrRating'])+0.0787*(df.at[i-1,'HundredCon'])+0.0556*(df.at[i-1,'FiftyCon'])-0.0328*(df.at[i-1,'ZeroCon']))  

df["Consistency"] = ConValue  





#######################################
####              Calculation of Form      ############
####################################

FormValue=[]
FormValue.append(0)
df.at[0,'Form']=0

for i in range(1,columnNum):
      FormValue.append(0.4262*(df.at[i-1,'AvgRating'])+0.2566*(df.at[i-1,'MatchForm'])+0.1510*(df.at[i-1,'SrRating'])+0.0787*(df.at[i-1,'CenturyForm'])+0.0556*(df.at[i-1,'FiftyForm'])-0.0328*(df.at[i-1,'ZeroForm']))  

df["Form"] = FormValue  





#######################################
####              Calculation of Opposition      ############
####################################

OppValue=[]
OppValue.append(0)
df.at[0,'OppositionValue']=0

for i in range(1,columnNum):
      OppValue.append(0.4262*(df.at[i-1,'AvgRating'])+0.2566*(df.at[i-1,'MatchOpp'])+0.1510*(df.at[i-1,'SrRating'])+0.0787*(df.at[i-1,'HundredOppRating'])+0.0556*(df.at[i-1,'FiftyOppRating'])-0.0328*(df.at[i-1,'ZeroOppRating']))  

df["OppositionValue"] = OppValue  


#######################################
####              Calculation of VenueValue      ############
####################################

VenueValue=[]
VenueValue.append(0)
df.at[0,'VenueValue']=0

for i in range(1,columnNum):
      VenueValue.append(0.4262*(df.at[i-1,'AvgRating'])+0.2566*(df.at[i-1,'MatchVen'])+0.1510*(df.at[i-1,'SrRating'])+0.0787*(df.at[i-1,'HundredVenueRating'])+0.0556*(df.at[i-1,'FiftyVenue'])+0.0328*(df.at[i-1,'HighestScoreRating']))  

df["VenueValue"] = VenueValue  




################
#################
#####################
#########################
###########################
























































































    

        
