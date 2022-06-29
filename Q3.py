def emailseparate(email):
    sep = email.split('@')
    username = sep[0]
    companyname = sep[1].split('.')[0]
    print('User Name: ', username)
    print('Company Name: ', companyname)

emailseparate('nurfaiqah@google.com')