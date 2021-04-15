
from pymongo import MongoClient
client = MongoClient("mongodb+srv://username:password@mongocluster.yervs.mongodb.net/databasename?retryWrites=true&w=majority")
db = client.get_database('MongoDB')
records = db.MongoRecords

aa = records.count_documents({})

print(aa)


#---------------insert single record---------------------
# new_student = {
#         'Product_name': 'cell',
#         'product_id': 01,
# }
# records.insert_one(new_student)

#---------------insert multiple records---------------------
# new_record = [
#     {
#         'Product_name': 'cell',
#         'product_id': 01,
#  
#     },
#     {
#         'Product_name': 'cell phone',
#         'product_id': 02,
#     }
# ]
# records.insert_many(new_students)




#------------------Find all Records---------------------
# print(list(records.find()))




#-----------------find Specific record------------------------------
# print(records.find_one({'Reciept_id': '01'}))





#-----------------------Update Records-----------------
# record_updates = {
#     'Reciept_id': 001
# }
# records.update_one({'Reciept_id':01}, {'$set': record_updates})



#-----------------Delete Records-------------
# import time
# start_time = time.time()
# for i in range(101,103):
#     aa = records.delete_one({"Reciept_id":i})
#     print(aa)
# print("--- %s seconds ---" % (time.time() - start_time))





# # import pandas as pd
# df = pd.read_csv('/Users/mirza/Desktop/bot/data_grocessary/finaldataset.csv')
# for i in range(0,1000):
#     a=df['Products'][i]
#     b=df['Reciept_ID'][i]
#     c=df['Serial No.'][i]
#     d=df['Quantity'][i]
#     e=df['Sales Price'][i]
#     f=df['Unit Price'][i]
#     g=df['Cost_Price'][i]
#     h=df['Date and Time'][i]
#     new_student = {
#         'Product name': str(a),
#         'Reciept_id': int(b),
#         'Serial No': int(c),
#         'Sales Price':int(d),
#         'Unit Price':int(e),
#         'Cost_Price':int(f),
#         'Date and Time':int(g)
#         }
#     records.insert_one(new_student)





# print(a,b,c)

# new_student = {'Product name': a,'Reciept_ID': b,'Serial No.': c}
# records.insert_one(new_student)



# Index(['Unnamed: 0', 'Products', 'Reciept_ID', 'Serial No.', 'Quantity',
#     'Sales Price', 'Unit Price', 'Cost_Price', 'Date and Time'], dtype='object')

