import collections
def findFraud(iplist):
  fraud_list = list()
  fraud_dict_names = {}
  fraud_dict = collections.defaultdict(list)
  for ii in iplist:
    temp = ii.split("|")
    if int(temp[1]) > 3000:
      if temp[0] not in fraud_dict_names:
        fraud_list.append([temp[0], 1])
        fraud_dict_names[temp[0]] = 1
        fraud_dict[temp[0]].append((temp[1:], len(fraud_list)-1))

    else:
      if temp[0] not in fraud_dict_names:
        try:
          #same location as previous location
          if fraud_dict[temp[0]][-1][0][1] == temp[2]:
            #add to dict and list
            #not a crime
            fraud_list.append([temp[0], 0])
            fraud_dict[temp[0]].append(temp[1:], len(fraud_list)-1)
          else:
            if int(temp[3]) - int(fraud_dict[temp[0]][-1][0][-1]) < 60:
              #Assign criminal status
              fraud_list[fraud_dict[temp[0]][-1][1]][1] = 1 
              fraud_dict_names[temp[0]] = 1
            else:
              fraud_list.append([temp[0], 0]) 
            #add to main list in any case
            fraud_dict[temp[0]].append((temp[1:], len(fraud_list)-1))
              
        except:
          fraud_list.append([temp[0], 0])
          fraud_dict[temp[0]].append((temp[1:], len(fraud_list)-1)) 
  return [ii[0] for ii in fraud_list if ii[1] == 1]    

iplist = ["Shilpa|500|California|63",
"Tom|25|New York|615",
"Krasi|9000|California|1230",
"Tom|25|New York|1235",
"Tom|25|New York|1238",
"Shilpa|50|Michigan|1300",
"Matt|90000|Georgia|1305",
"Jay|100000|Virginia|1310",
"Krasi|49|Florida|1320",
"Krasi|83|California|1325",
"Shilpa|50|California|1350"]
     
print findFraud(iplist)
