import win32com.client
ol = win32com.client.Dispatch('Outlook.Application')
olmailitem = 0x0

newmail = ol.CreateItem(olmailitem)
newmail.Subject = 'Testing Mail'
newmail.To = 'emils.g@outlook.com'

newmail.Body = 'Hello, this is a test email to showcase how to send emails from Python and Outlook.'
#attach = 'file location'
#newmail.Attachments.Add(attach)

newmail.Send()
