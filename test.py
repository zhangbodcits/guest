# # # # This sample code uses the Appium python client
# # # # pip install Appium-Python-Client
# # # # Then you can paste this into a file and simply run with Python
# # #
# # # from appium import webdriver
# # #
# # # caps = {}
# # # caps["platformName"] = "Android"
# # # caps["deviceName"] = "seveniruby"
# # # caps["appPackage"] = "com.xueqiu.android"
# # # caps["appActivity"] = ".view.WelcomeActivityAlias"
# # # caps["autoGrantPermissions"] = "true"
# # #
# # # driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# # # driver.implicitly_wait(5)
# # # el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
# # # el1.click()
# # # el2 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
# # # el2.click()
# # # el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
# # # el3.send_keys("alibaba")
# # # el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
# # # el4.click()
# # #
# # # driver.quit()
# # # a = 100
# # # i = 0
# # # for g in range(a):
# # # #     print("******" * 100, end="")
# # # names = ['zz', 'cc', 'dd', 'ss']
# # # for name in names:
# # #     print(name.title() + ',that is a great trick!')
# # #     # print('我期待你的下一次表演，' + name.title() + '。\n')
# # # a = list(range(1, 5, 2))
# # # print(a)
# # # # for i in a:
# # # #     print(i)
# # ss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# # # for a in range(1, 11):
# # #     # s = a**2
# # #     ss.append(a ** 2)
# # # print(ss)
# # print(sum(ss))
# #
# # aa = [value ** 2 for value in range(1, 11)]
# # print(aa)
# #
# # numbers = range(3, 31, 3)
# # # print(sum(numbers))
# # for number in numbers:
# #     print(number)
# # number = [number for number in range(3, 31, 3)]
# names = ['zz', 'cc', 'dd', 'ss']
# # print(names[0:2])
# # names_too = names[:]
# # print(names_too)
# # names_too.append('ww')
# # names.append('11')
# # print(names)
# # print(names_too)
#
# # names = (200, 50)
# # for name in names:
# #     print(name)
# # for name in names:
# #     if name == 'zz':
# #         print(name.upper())
# #     else:
# #         print(name.title())
# # age = 12
# # if age < 4:
# #     print('免费')
# # elif age < 18:
# #     print('5元')
# # else:
# #     print('10yuan')
# alien0 = {'color': 'green', 'points': 5}
# alien1 = {'color': 'yellow', 'points': 10}
# alien2 = {'color': 'red', 'points': 15}
# # print(alien['color'])
# # print(alien['points'])
# # aliens = [alien0, alien1, alien2]
# # for alien in aliens:
# #     print(alien)
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# print(aliens)
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = '10'
#         alien['speed'] = 'medium'
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['points'] = '20'
#         alien['speed'] = 'fast'
# for alien in aliens[0:10]:
#     print(alien)
# alien_number = len(aliens)
# print(alien_number)
# favorite_languages = {
#     'zhang': ['python', 'c'],
#     'li': ['python'],
#     'wang': ['ruby', 'go'],
#     'cui': ['php']
# }
# # print(favorite_languages.items())
# for name, languages in favorite_languages.items():
#     print('\n' + name.title() + "'s favorite languages are:")
#     for language in languages:
#         print('\t' + language.title())
# users = {
#     'renxiaolei': {
#         'first': 'yuncheng',
#         'last': 'ruicheng',
#         'location': 'taiyuan',
#     },
#     'zhangbo': {
#         'first': 'yuncheng',
#         'last': 'ruicheng',
#         'location': 'taiyuan',
#     }
# }
# for user_name, user_info in users.items():
#     print('\nUsername:' + user_name)
#     full_name = user_info['first'] + '\t' + user_info['last']
#     location = user_info['location']
#     print('\tFull name: ' + full_name.title())
#     print('\tlocation: ' + location.title())

# message = input('请输入你的名字：')
# # print('您好：' + message + '!')
# a = 1
# while a <= 5:
#     print(a)
#     a += 1
# a = '\nTell me something, and I will repeat it back to you:'
# a += "\nEnter 'quit' to end the program."
# message = ''
# while message != 'quit':
#     message = input(a)
#     print(message)
def a(bname, btype='dog'):
    print('I have a ' + btype + '.')
    print('My ' + btype + "'s name is " + bname.title() + '.')


a(bname='憨批', btype='cat')


def get_name(firstname, lastname):
    full_name = firstname + ' ' + lastname
    return full_name


name = get_name('zhang', 'bo')
print(name)
