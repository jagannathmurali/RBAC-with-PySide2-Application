import argparse
import time
import csv
import random


class RBACClass(object):
    """docstring for RBAC."""
    permission_dict = {'Administrator': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                       'Cash Counter': [0, 1, 4, 5, 12, 13, 14], 'Insurance': [0, 1, 3, 12, 13, 14],
                       'Reception': [0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]}

    def __init__(self):
        # self.LOG_DATA_PATH = 'D:\\SASTRA\\Code\\Dean Mam Project\\assignment\\log\\'
        self.USER_DATA_PATH = 'D:\\SASTRA\\Code\\Dean Mam Project\\assignment\\Data\\user-database.csv'

    # def __writeCSV(self, data):
    #     LOG_FILE_PATH = self.LOG_DATA_PATH + 'log_temp_' + time_string + '.csv'
    #     with open(LOG_FILE_PATH, mode='a') as log_file:
    #         log_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #         log_writer.writerow([data])

    def logon(self, UserName, Password):
        getRole = self.__checkPass(UserName, Password)
        if getRole != None:
            permission = RBACClass.permission_dict[getRole]
            return permission
        return getRole

    def __checkPass(self, UserName, Password):
        with open(self.USER_DATA_PATH, 'r') as csvfile:
            readCSV = csv.reader(csvfile)
            for row in readCSV:
                if row[0] == UserName and row[2] == Password:
                    return row[1]

# read log delete_log
# permission_dict = {'admin':'1 1 1','user':'1 0 0', 'debugger':'1 1 0'}
# global temp, time_string, start
# start = False
# temp = 40.0
# # parsing arguments
# parser = argparse.ArgumentParser()
# parser.add_argument('--data_path', default='D:\\SASTRA\\Code\\Dean Mam Project\\assignment\\Data\\user-database.csv', help="Enter path where data is stored excluding filename")
# parser.add_argument('--user_name', required=True, help="Enter UserName")
# parser.add_argument('--password', required=True, help="Enter Password")
# parser.add_argument('--log_data', default=False)
#
# args = parser.parse_args()


# UserName = args.user_name
# Password = args.password
# logData = args.log_data

# while(1):
#     f = open('helloworld.html','w')
#     tempValue = tempData()
#     permission = logon(UserName, Password)
#     if logData == True & permission[1] == 1:
#         if start == False:
#             named_tuple = time.localtime() # get struct_time
#             time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
#             start = True
#         __writeCSV(tempValue)
#
#     message = """<html>
#     <head>
#         <script>
#             setInterval(function(){
#                 window.open('helloworld.html', "_self")
#             }, 2000);
#         </script>
#     </head>
#     <body>
#         <p>Temperature:- {value}</p>
#
#     </body>
#     </html>""".format(value=tempValue)
#
#     f.write(message)
#
#     f.close()
