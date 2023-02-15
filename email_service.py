import smtplib
import poplib

# create an SMTP object
s = smtplib.SMTP('smtp.example.com')

# login to the server (if required)
s.login('username', 'password')

# compose the message
message = "Hello, this is an email message."

# send the message
s.sendmail('sender@example.com', 'receiver@example.com', message)

# close the connection
s.quit()




# create a POP3 object
p = poplib.POP3('pop3.example.com')

# login to the server
p.user('username')
p.pass_('password')

# retrieve the list of emails
num_messages = len(p.list()[1])

for i in range(num_messages):
    # retrieve the message
    msg = p.retr(i+1)
    print(msg)
    # delete the message from the server
    p.dele(i+1)

# close the connection
p.quit()


