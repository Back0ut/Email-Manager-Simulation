class EmailManager:
    def __init__(self):
        self.emails = []

    def create_email(self, sender, recipient, subject, body):
        email = {'sender': sender, 'recipient': recipient, 'subject': subject, 'body': body, 'replies': []}
        self.emails.append(email)
        print("Email created successfully.")

    def edit_email(self, email_index, new_body):
        if 0 <= email_index < len(self.emails):
            self.emails[email_index]['body'] = new_body
            print("Email edited successfully.")
        
        else: print("Invalid email index.")

    def delete_email(self, email_index):
        if 0 <= email_index < len(self.emails):
            del self.emails[email_index]
            print("Email deleted successfully.")
        
        else: print("Invalid email index.")

    def reply_to_email(self, email_index, reply_body):
        if 0 <= email_index < len(self.emails):
            reply = {'sender': self.emails[email_index]['recipient'], 'recipient': self.emails[email_index]['sender'], 'body': reply_body}
            self.emails[email_index]['replies'].append(reply)
            print("Reply sent successfully.")
        
        else: print("Invalid email index.")

    def view_emails(self):
        if self.emails:
            for i, email in enumerate(self.emails):
                print(f"Email {i}:\nSender: {email['sender']}\nRecipient: {email['recipient']}\nSubject: {email['subject']}\nBody: {email['body']}")
                if email['replies']:
                    print("Replies:")
                    for reply in email['replies']:
                        print(f"\tFrom: {reply['sender']}\n\tTo: {reply['recipient']}\n\tBody: {reply['body']}")
                print()
        
        else: print("No emails found.")

create_email = input('Create Email? Y/N: ')

if create_email.upper() == 'Y':
    email_manager = EmailManager()

    actions = ''
    print('Type quit to quit')

    while actions.lower() != 'quit':
        actions = input('Send / View / Delete / Edit / Reply: ')

        if actions.lower() == 'send':
            sender_email, recipent, subject, body = input('Email of Sender: '), input('Recipient: '), input('Subject: '), input('Body: ')
            email_manager.create_email(sender_email, recipent, subject, body)
        
        elif actions.lower() == 'edit':
            edited_email = int(input('Index of email: '))
            new_body = input('Edited text: ')

            email_manager.edit_email(edited_email, new_body)
        elif actions.lower() == 'delete':
            deleted_email = int(input('Index of email: '))
            email_manager.delete_email(deleted_email)
        
        elif actions.lower() == 'view':
            email_manager.view_emails()
        
        elif actions.lower() == 'reply':
            email_replied, reply_body = int(input('Index of email: ')), input('Reply Body: ')
            email_manager.reply_to_email(email_replied, reply_body)