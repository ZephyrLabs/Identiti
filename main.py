#!/usr/bin/env python3
# Python Password Manager project
# made by S.Sravan

"""

#########################################
#     ____    __           __  _ __  _  #
#    /  _/___/ /__  ____  / /_(_) /_(_) #
#    / // __  / _ \/ __ \/ __/ / __/ /  #
#  _/ // /_/ /  __/ / / / /_/ / /_/ /   #
# /___/\__,_/\___/_/ /_/\__/_/\__/_/    #
#########################################
Identiti is a password manager made with Python (Front-end) and MySQL (Back-end)

Checks:
#pending GPLv3 license
#pending Documentation

"""

# importing necessary modules:
import time
import os
import codecs

# DEFAULT PARAMETERS
ENABLE_DEFAULT_PARAMETERS = True
MASTER_AUTH_KEY = '123'

# if default parameters are enabled, set default params
if ENABLE_DEFAULT_PARAMETERS:
    host_param = 'localhost'
    user_param = 'root'
    passwd_param = 'root'
    database_param = 'db'

# creating a file handle for logging:
# noinspection PyBroadException
try:
    log = open('log.txt', 'a+')
except:
    print('unable to open logfile')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# miscellaneous functions #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


# creating timestamp function:
def timestamp():
    a = '['
    a += str(round(time.time(), 3))
    a += ']: '
    return a


# create logging function:
def verbose(output, visibility):
    if visibility:
        print(output)
    log.write(timestamp())
    log.write(output)
    log.write('\n')


# function for checking options
def option(valid):
    while True:
        a = input('>')
        if a not in valid:
            print('ERROR: invalid\n')
        else:
            return a


# function to clear the console,
# give bool::True if you need user consent
# give bool::False if you don't need user consent, clean console
def clear(check):
    if check:
        null_exit = input("\npress enter to continue...")
        print(null_exit)
        print("clean")
    # noinspection PyBroadException
    try:
        os.system('cls')  # on Windows System
    except:
        os.system('clear')  # on a Linux system


def about_psterm():
    print("               ______ ")
    print("    ____  ____/_  __/__  _________ ___ ")
    print("   / __ \/ ___// / / _ \/ ___/ __ `__ \ ")
    print("  / /_/ (__  )/ / /  __/ /  / / / / / / ")
    print(" / .___/____//_/  \___/_/  /_/ /_/ /_/ ")
    print("/_/ ")
    print("psTerm: 2020-21 Python-MySQL console Emulator, by ZephyrLabs")
    psterm_about_handle = open('psterm.md', '+r')
    psterm_about = psterm_about_handle.read()
    print(psterm_about)
    print("\n")
    psterm_about_handle.close()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# CRUD functions #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# function to fetch passphrase
def fetch(username, user_account):
    # noinspection PyBroadException
    try:
        # complete fetch task
        query = 'select user_pass from lut where username = %s and user_account = %s'
        params = (username, user_account)
        db_handle.execute(operation=query, params=params)
        result = db_handle.fetchone()

        # log the data fetch
        b = 'fetched data for user: '
        b += username
        verbose(b, True)

        # export fetched data
        print('\naccount:', user_account, '|', 'passphrase:', codecs.decode(result[0], 'rot_13'), '\n')

    except:
        # parse error as fatal
        print('fatal error occurred during that operation', '\n')

    finally:
        clear(True)


# function to fetch passphrase
def fetchall(username):
    # noinspection PyBroadException
    try:
        # complete fetch task
        query = 'select user_account, user_pass from lut where username = %s'
        params = (username,)
        db_handle.execute(operation=query, params=params)
        result = db_handle.fetchall()

        # log the data fetch
        b = 'fetched data for user: '
        b += username
        verbose(b, True)

        # export fetched data
        for i in result:
            print('\naccount:', i[0], '|', 'passphrase:', codecs.decode(i[1], 'rot_13'), '\n')

    except:
        # parse error as fatal
        print('fatal error occurred during that operation', '\n')

    finally:
        clear(True)


# function to record passphrases
def record(username, user_account, user_pass):
    # noinspection PyBroadException
    try:
        # complete write task
        query = 'insert into lut values(%s, %s, %s)'
        params = (username, user_account, codecs.encode(user_pass, 'rot_13'))
        db_handle.execute(operation=query, params=params)
        db.commit()

        # log the data written
        b = 'Data written for user: '
        b += username
        verbose(b, True)

        # export the written data
        print('\nData written:')
        print('account:', user_account, '|', 'passphrase:', user_pass, '\n')

    except:
        # parse error as fatal
        print('fatal error occurred during that operation', '\n')

    finally:
        clear(True)


# function to update passphrases
def update(username, user_account, user_pass):
    # noinspection PyBroadException
    try:
        # complete update task
        query = 'update lut set user_pass = %s where username = %s and user_account = %s'
        params = (codecs.encode(user_pass, 'rot_13'), username, user_account)
        db_handle.execute(operation=query, params=params)
        db.commit()

        # log the data written
        b = 'Data written for user: '
        b += username
        verbose(b, True)

        # export the written data
        print('\nData written:')
        print('account:', user_account, '|', 'passphrase:', user_pass, '\n')

    except:
        # parse error as fatal
        print('fatal error occurred during that operation', '\n')

    finally:
        clear(True)


# function to purge passphrases
def purge(username, user_account):
    # noinspection PyBroadException
    try:
        # complete purge task
        query = 'delete from lut where username = %s and user_account = %s'
        params = (username, user_account)
        db_handle.execute(operation=query, params=params)
        db.commit()

        # log the data purged
        b = 'Data purged for user: '
        b += username
        verbose(b, True)

        # export the purged data
        print('\nData purged:')
        print('account:', user_account, ' no longer exists', '\n')

    except:
        # parse error as fatal
        print('fatal error occurred during that operation', '\n')

    finally:
        clear(True)


# function to purge all passphrases
def purge_all(username):
    # noinspection PyBroadException
    try:
        # complete purge task
        query = 'delete from lut where username = %s'
        params = (username,)
        db_handle.execute(operation=query, params=params)
        db.commit()

        # log the data purged
        b = 'Data purged (all) for user: '
        b += username
        verbose(b, True)

        # export the purged data
        print('\nData purged:')
        print('user:', username, ' no longer exists', '\n')

    except:
        # parse error as fatal
        print('fatal error occurred during that operation', '\n')

    finally:
        clear(True)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Main program handle #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Initialising message
verbose('starting Identiti...', True)

# try connecting to the database, else parse as error and exit
# noinspection PyBroadException
try:
    import mysql.connector

    if ENABLE_DEFAULT_PARAMETERS == 1:
        # noinspection PyUnboundLocalVariable
        db = mysql.connector.connect(host=host_param, user=user_param, passwd=passwd_param)
    else:
        db = mysql.connector.connect(host='localhost', user='root', passwd='root')

    verbose('connected to the MySQL', True)

    # noinspection PyBroadException
    try:
        if ENABLE_DEFAULT_PARAMETERS == 1:
            # noinspection PyUnboundLocalVariable
            db = mysql.connector.connect(host=host_param, user=user_param, passwd=passwd_param, database=database_param)
        else:
            db = mysql.connector.connect(host='localhost', user='root', passwd='root', database='db')
        verbose('connected to the Database', True)

    except:
        verbose("couldn't connect to the database", True)
        if ENABLE_DEFAULT_PARAMETERS == 1:
            # noinspection PyUnboundLocalVariable
            db = mysql.connector.connect(host=host_param, user=user_param, passwd=passwd_param)
        else:
            db = mysql.connector.connect(host='localhost', user='root', passwd='root')

except:
    verbose('connection to MySQL failed', True)
    verbose('ending session, closing Identiti\n', True)
    clear(True)
    exit()
else:

    # noinspection PyBroadException
    try:
        db_handle = db.cursor(buffered=True)
        verbose('database handle initiated', True)

        # create the database if it doesn't exist
        db_handle.execute('create database if not exists db')
        print('create database: PASS')
        db_handle.execute('use db')
        print('use database: PASS')

        # auto setup of tables
        db_handle.execute('create table if not exists lut(username varchar(32) not null, user_account varchar(64) not '
                          'null, user_pass varchar(32) not null)')
        db_handle.execute('create table if not exists bst(username varchar(32) primary key, main_pass varchar(32) not '
                          'null)')

        # noinspection PyUnboundLocalVariable
        db.commit()

        verbose('auto setup complete', True)

    except Exception as e:
        verbose('auto setup failed', True)
        print(e)

    print('\n')
    clear(True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Main program..
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

print('Welcome.')

while True:
    print('1. Login\n'
          '2. about software\n'
          'exit\n')
    extern_option = option(('1', '2', 'exit', MASTER_AUTH_KEY))
    clear(False)

    if extern_option == 'exit':
        print('goodbye.')
        verbose("ending session, closing Identiti", True)
        clear(False)
        break

    elif extern_option == '2':
        # noinspection PyBroadException
        try:
            readme_handle = open('README.md', '+r')
            print('About the Software and the Creator:')
            readme = readme_handle.read()
            print(readme)
            print("\n")
            readme_handle.close()

        except:
            print('ERROR: something went wrong there :/\n')
        clear(True)

    elif extern_option == '1':
        while True:
            print('1. Login to existing account\n'
                  '2. Create new account\n'
                  'exit\n')
            account_option = option(('1', '2', 'exit'))
            clear(False)

            if account_option == 'exit':
                break

            if account_option == '1':
                while True:
                    # noinspection PyBroadException
                    try:
                        user_name = input('enter username:\n>')
                        main_pass = input('enter passphrase:\n>')
                        clear(False)
                        auth_query = 'select main_pass from bst where username = %s'
                        auth_param = (user_name,)
                        # noinspection PyUnboundLocalVariable
                        db_handle.execute(operation=auth_query, params=auth_param)
                        auth_token = db_handle.fetchone()

                        if codecs.encode(auth_token[0], 'rot_13') == main_pass:
                            notifier_1 = 'user: ' + user_name + ' has logged in'
                            verbose(notifier_1, True)
                        else:
                            print('given credentials are incorrect, please try again\n')
                            clear(True)
                            break

                    except:
                        print('\nERROR: something went wrong there :/\nplease try again...\n')
                        clear(True)
                        break

                    while True:
                        # noinspection PyBroadException
                        try:
                            # noinspection PyUnboundLocalVariable
                            db.commit()
                            verbose("Data synced", True)

                        except:
                            print('\nERROR: something went wrong there :/\nplease try again...\n')
                            clear(True)
                            break

                        print('1.get your passphrase\n'
                              '2.get all passphrases\n'
                              '3.add a passphrase\n'
                              '4.update a passphrase\n'
                              '5.remove a passphrase\n'
                              '6.delete this account\n'
                              'exit\n')
                        intern_option = option(('1', '2', '3', '4', '5', '6', 'exit'))
                        clear(False)

                        # executing the selected options
                        if intern_option == 'exit':
                            notifier_1 = 'user ' + user_name + ' has logged out'
                            verbose(notifier_1, True)
                            clear(True)
                            break

                        elif intern_option == '1':
                            # noinspection PyBroadException
                            try:
                                account_username = input('enter the username of the respective account:\n>')
                                fetch(username=user_name, user_account=account_username)

                            except:
                                print('\nERROR: something went wrong there :/\nplease try again...\n')
                                clear(True)

                        elif intern_option == '2':
                            # noinspection PyBroadException
                            try:
                                fetchall(username=user_name)

                            except:
                                print('\nERROR: something went wrong there :/\nplease try again...\n')
                                clear(True)

                        elif intern_option == '3':
                            # noinspection PyBroadException
                            try:
                                account_username = input('enter the username of the respective account:\n>')
                                account_password = input('enter the passphrase of the respective account:\n>')
                                account_password_reenter = input('enter the passphrase again\n>')
                                clear(False)
                                if account_password != account_password_reenter:
                                    print('something was wrong with the entries, please try again :/')
                                    clear(True)
                                else:
                                    record(username=user_name,
                                           user_account=account_username,
                                           user_pass=account_password)

                            except:
                                print('\nERROR: something went wrong there :/\nplease try again...\n')
                                clear(True)

                        elif intern_option == '4':
                            # noinspection PyBroadException
                            try:
                                account_username = input('enter username of the respective account:\n>')
                                account_password_old = input('enter the old passphrase of the respective account:\n>')
                                account_password = input('enter the new passphrase of the respective account:\n>')
                                account_password_reenter = input('enter the new passphrase again\n>')
                                clear(False)

                                # check if the old passphrase entered was correct
                                pass_query = 'select user_pass from lut where username = %s and user_account = %s'
                                pass_params = (user_name, account_username)
                                db_handle.execute(operation=pass_query, params=pass_params)
                                pass_check = db_handle.fetchone()

                                if account_password_old == codecs.decode(pass_check[0], 'rot_13'):
                                    if account_password != account_password_reenter:
                                        print('something was wrong with the entries, please try again :/')
                                        clear(True)
                                    else:
                                        update(username=user_name,
                                               user_account=account_username,
                                               user_pass=account_password)

                            except:
                                print('\nERROR: something went wrong there :/\nplease try again...\n')
                                clear(True)

                        elif intern_option == '5':
                            # noinspection PyBroadException
                            try:
                                account_username = input('enter username of the respective account:\n>')
                                account_password_old = input('enter the old passphrase of the respective account:\n>')
                                clear(False)

                                # check if the passphrase entered was correct
                                pass_query = 'select user_pass from lut where username = %s and user_account = %s'
                                pass_params = (user_name, account_username)
                                db_handle.execute(pass_query, pass_params)
                                pass_check = db_handle.fetchone()

                                if account_password_old != codecs.decode(pass_check[0], 'rot_13'):
                                    print('something was wrong with the entries, please try again :/')
                                    clear(True)
                                else:
                                    purge(username=user_name, user_account=account_username)

                            except:
                                print('\nERROR: something went wrong there :/\nplease try again...\n')
                                clear(True)

                        elif intern_option == '6':
                            # noinspection PyBroadException
                            try:
                                account_password = input('enter your Identiti passphrase:\n>')
                                account_password_reenter = input('enter the passphrase again\n>')
                                clear(False)

                                if account_password != account_password_reenter:
                                    print('something was wrong with the entries, please try again :/')
                                    clear(True)
                                else:

                                    # check if the old passphrase entered was correct
                                    pass_query = 'select main_pass from bst where username = %s'
                                    pass_params = (user_name,)
                                    db_handle.execute(operation=pass_query, params=pass_params)
                                    pass_check = db_handle.fetchone()

                                    if account_password != codecs.encode(pass_check[0], 'rot_13'):
                                        print('something was wrong with the entries, please try again :/')
                                        clear(True)
                                    else:
                                        ##
                                        # remove account from base table
                                        purge_query = 'delete from bst where username = %s'
                                        purge_param = (user_name,)
                                        # noinspection PyUnboundLocalVariable
                                        db_handle.execute(operation=purge_query, params=purge_param)
                                        db.commit()
                                        purge_all(username=user_name)
                                        break

                            except:
                                print('\nERROR: something went wrong there :/\nplease try again...\n')

                                clear(True)

                    break  # come out of the session loop

            if account_option == '2':
                while True:
                    # noinspection PyBroadException
                    try:
                        user_name = input('enter username:\n>')
                        main_pass = input('enter passphrase:\n>')
                        main_pass_reenter = input('enter the passphrase again:\n>')
                        if main_pass != main_pass_reenter:
                            print('something was wrong with the entries, please try again :/')
                            clear(True)
                            break

                        else:
                            # noinspection PyBroadException
                            try:
                                auth_query = 'select main_pass from bst where username = %s'
                                auth_param = (user_name,)
                                # noinspection PyUnboundLocalVariable
                                db_handle.execute(operation=auth_query, params=auth_param)
                                auth_token = db_handle.fetchone()
                                if not auth_token:
                                    auth_query = 'insert into bst values(%s, %s);'
                                    auth_param = (user_name, codecs.encode(main_pass, 'rot_13'))
                                    # noinspection PyUnboundLocalVariable
                                    db_handle.execute(operation=auth_query, params=auth_param)
                                    db.commit()
                                    print('Account registered successfully')
                                else:
                                    print("that account already exists")
                                    clear(True)
                                    break

                            except:
                                print('\nERROR: something went wrong there :/\nplease try again...\n')
                                clear(True)
                                break

                            clear(True)
                            break

                    except:
                        print('\nERROR: something went wrong there :/\nplease try again...\n')
                        clear(True)
                        break

    if extern_option == MASTER_AUTH_KEY:
        print("               ______ ")
        print("    ____  ____/_  __/__  _________ ___ ")
        print("   / __ \/ ___// / / _ \/ ___/ __ `__ \ ")
        print("  / /_/ (__  )/ / /  __/ /  / / / / / / ")
        print(" / .___/____//_/  \___/_/  /_/ /_/ /_/ ")
        print("/_/ ")
        print("psTerm: 2020-21 Python-MySQL console Emulator, by ZephyrLabs\n")
        while True:
            psterm_query = input('>')

            if psterm_query == 'exit':
                clear(False)
                break

            elif psterm_query == 'clear':
                clear(False)

            elif psterm_query == 'about':
                # noinspection PyBroadException
                try:
                    about_psterm()
                except:
                    print('\nERROR: something went wrong there :/\nplease try again...\n')
                clear(True)

            elif psterm_query == 'commit':
                db.commit()

            elif psterm_query == 'reset':

                # drop tables
                db_handle.execute('if exists drop table bst')
                db_handle.execute('if exists drop table lut')

                # auto setup of tables
                db_handle.execute(
                    'create table if not exists lut(username varchar(32) not null, user_account varchar(64) not '
                    'null, user_pass varchar(32) not null)')
                db_handle.execute(
                    'create table if not exists bst(username varchar(32) primary key, main_pass varchar(32) not '
                    'null)')

                print('database reset complete')

            else:
                # noinspection PyBroadException
                try:
                    db_handle.execute(psterm_query)
                    if psterm_query[0:6] == 'select' or psterm_query[0:4] == 'show' or psterm_query[0:8] == 'describe' or psterm_query[0:4] == 'desc':
                        psterm_result = db_handle.fetchall()
                        for row in psterm_result:
                            for entry in row:
                                print("|", end='')
                                print(entry, end='')
                            print("|")
                        print('') 

                except Exception as e:
                    print("ERROR: query error")
                    print(e)
