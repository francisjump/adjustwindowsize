import win32gui
import win32con
import pygetwindow as gw
import os
import time

time.sleep(5)
all_list = gw.getAllTitles()
# print(all_list)
system_application_list = ['Settings','Windows Input Experience','PDSTYLEAGENT','Program Manager','Realtek Audio Console','ZPToolBarParentWnd']

while('' in all_list):
    all_list.remove('')

user_application_list = [x for x in all_list if (x not in system_application_list)]
# print(user_application_list)

count = 1

while (count == 1):
    answer = int(input("Use default setting? (1: Yes ; 2: No): "))
    if answer == 1:
        count = 0
        with open(r"D://adjustwindowsize/adjustwindowsize_info.txt", "r",encoding='utf-8') as f:
            contents = f.readlines()
        f.close()
        new_contents = [x[:-1] for x in contents]
        print(new_contents)

        for i in range(0,len(new_contents)):
            if (i%5 == 0):
                print(new_contents[i])
                for j in range(0,len(user_application_list)):
                    if new_contents[i].lower() in user_application_list[j].lower():
                        target = gw.getWindowsWithTitle(user_application_list[j])[0]
                        target.restore()
                        target.resizeTo(int(new_contents[i+1]), int(new_contents[i+2]))
                        target.moveTo(int(new_contents[i+3]), int(new_contents[i+4]))
        print("All windows have been successfully adjusted!")
    elif answer == 2:
        count = 0
        with open("D://adjustwindowsize/adjustwindowsize_info.txt",'r+') as f:
            f.truncate(0)
        f.close()
        window_num = input("Please type the number of windows (positive integer): ")
        while ((window_num.isnumeric() == False) or (int(window_num) < 0)):
            window_num = input("Your input is not a positive integer! Please retype the number of windows: ")
        window_num = int(window_num)
        title_list = []
        for i in range(0, window_num):
            print("Please enter the name of window " + str(i+1) +".")
            window_name = input("Name: " )
            title_list.append(window_name.lower())
        print("You have entered " + str(window_num) + " windows, the window names are shown below: ")
        print(title_list)
        for i in range(0,len(title_list)):
            for j in range(0, len(user_application_list)):
                if title_list[i] in user_application_list[j].lower():
                    target = gw.getWindowsWithTitle(user_application_list[j])[0]
                    with open(r"D://adjustwindowsize/adjustwindowsize_info.txt", "a",encoding='utf-8') as f:
                        f.write(title_list[i])
                        f.write("\n")
                        f.write(str(target.width))
                        f.write("\n")
                        f.write(str(target.height))
                        f.write("\n")
                        f.write(str(target.left))
                        f.write("\n")
                        f.write(str(target.top))
                        f.write("\n")
                        print(target.size)
                        # print(target.width,target.height)
                        print(target.topleft)
                        # print(target.left,target.top)
                    f.close()
        print("Your default setting has been successfully updated!")
    else:
        print("You type wrongly. Please try again.")







    

# all_list = gw.getAllTitles()
# # print(all_list)
# system_application_list = ['安裝程式','Windows 輸入體驗','PDSTYLEAGENT','Program Manager','Realtek Audio Console','ZPToolBarParentWnd']

# while('' in all_list):
#     all_list.remove('')

# user_application_list = [x for x in all_list if (x not in system_application_list)]
# print(user_application_list)

# if (os.stat("info.txt").st_size) == 0:
#     for i in range(1,len(user_application_list)):
#         target = gw.getWindowsWithTitle(user_application_list[i])[0]
#         with open("info.txt", "a") as f:
#             f.write(user_application_list[i])
#             f.write("\n")
#             f.write(str(target.width))
#             f.write("\n")
#             f.write(str(target.height))
#             f.write("\n")
#             f.write(str(target.left))
#             f.write("\n")
#             f.write(str(target.top))
#             f.write("\n")
#             print(target.size)
#             print(target.width,target.height)
#             print(target.topleft)
#             print(target.left,target.top)
#     f.close()

# all_list = gw.getAllTitles()
# # print(all_list)
# system_application_list = ['安裝程式','Windows 輸入體驗','PDSTYLEAGENT','Program Manager','Realtek Audio Console','ZPToolBarParentWnd','Francis是豬 | Francis is a PIG!!! - Discord']

# while('' in all_list):
#     all_list.remove('')

# user_application_list = [x for x in all_list if (x not in system_application_list)]
# print(user_application_list)

# for i in range(1,len(user_application_list)):
#     target = gw.getWindowsWithTitle(user_application_list[i])[0]
#     with open("info.txt", "a") as f:
#         f.write(user_application_list[i])
#         f.write("\n")
#         f.write(str(target.width) + ',' + str(target.height) + ',' + str(target.left) + ',' + str(target.top))
#         f.write("\n")
#     print(target.size)
#     print(target.width,target.height)
#     print(target.topleft)
#     print(target.left,target.top)



# target = gw.getWindowsWithTitle(user_application_list[1])[0]
# print(target.topleft)
# print(target.size)
# target.resizeTo(600, 860)
# hwnd = win32gui.FindWindow(None, user_application_list[2])
# win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600,300,600,600, win32con.SWP_SHOWWINDOW)




# hwnd = win32gui.FindWindow(None, user_application_list[3])
# title = win32gui.GetWindowText(hwnd)
# left, top, right, bottom = win32gui.GetWindowRect(hwnd)
# print(left, top, right, bottom)
# win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600,300,600,600, win32con.SWP_SHOWWINDOW)


# target = gw.getWindowsWithTitle(user_application_list[1])[0]
# print(target.size)
# target.moveTo(500, 1000)
# for i in range(len(user_application_list)):
#     target = gw.getWindowsWithTitle(user_application_list[i])[0]
#     print(target.size)
    # if len(user_application_list) == 1:
    #     target.maximize()
    # if len(user_application_list) == 2:
    #     if i == 0:

# # Initializing the wmi constructor
# f = wmi.WMI()
  
# flag = 0
  
# # Iterating through all the running processes
# for process in f.Win32_Process():
#     print (process.Name)
#     if "microsoft" == process.Name:    
#         print("Application is Running")
#         flag = 1
#         target = gw.getWindowsWithTitle('Google')[0]
#         target.maximize()
#         print(target.isMaximized)
#         target.restore()
#         print(target.size)
#         target.resizeTo(600, 860)
#         print(target.size)
#         break
  
# if flag == 0:
#  print("Application is not Running")

# # import pygetwindow
# # win = pygetwindow.getWindowsWithTitle('Notepad')[0]
# # win.size = (640, 400)