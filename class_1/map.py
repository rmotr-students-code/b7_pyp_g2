my_list = ['tom', 'mary', 'ken', 'kenneth']

lenght_of_names = map(lambda n: len(n), my_list)
names_longer_than_4_chars = filter(lambda n: len(n) >= 4, my_list)

print(map(lambda n: len(n), filter(lambda n: len(n) >= 3, my_list)))

print([len(name) for name in my_list if len(name) >= 4])

"""

users = [User(1), User(2), User(3)...]

def analyze_if_user_is_a_robot(user):
    True | False

users_analyzed = [analyze_if_user_is_a_robot(u) for u in users]

[True, False, False, True]

robot_users = filter(lambda u: u is True, users_analyzed)
"""