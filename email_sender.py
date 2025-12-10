import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com", port=587)  ##port number 587 is fixed for gmail, helps define the address in detail
    server.starttls()
    
    #receiver email
    receiver_mail = input("Enter the receiver Email : ")
    
    #mail credentials
    sender_email = "thalasoni@gmail.com"
    password = "ipsq wrbc plrm wcff"
    
    ##login
    server.login(sender_email, password)
    
    ##sending email
    subject = input("Enter the subject: ")
    body = input("Enter the body: ")
    message = f"Subject: {subject} \n\n {body}"

    server.sendmail(sender_email, receiver_mail, message)
    print("Mail sent successfully")
    
    server.quit()
except Exception as e:
    print(f"An error occurred: ", e)