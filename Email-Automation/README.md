## Steps to use
<hr>

- Generate an app password to send emails using `smtplib`
    - Go to your [google account](https://myaccount.google.com/)
    - Go to security -> Signing in to Google -> App Passwords
    - Generate a new app password (copy the password to your clipboard)

- Open `config.env`, enter your email-id and the generated app password
- Open `sample_csv.csv` and change both the email ids to valid email-ids( on which you can verify the emails) and names.
- In the certificates folder, rename the first file to the username of first email-id and second file to username of second email-id.
- Run `pip install -r requirements.txt` to install all the required modules
- Run the python file