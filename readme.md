## 📁 Project Structure

weather-api/
├── app.py # Flask app
├── requirements.txt # Python dependencies
├── gunicorn_net.te # SELinux policy source
├── gunicorn_net.pp # SELinux policy binary
├── venv/ # Python virtual environment


## ⚙️ How to Run (Dev Mode)

```bash
# Activate virtualenv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py



##SELinux Integration
##Gunicorn by default cannot initiate outbound network connections due to SELinux constraints.

#To allow weather API requests, a custom SELinux policy is created:

# Compile and load the custom SELinux policy
checkmodule -M -m -o gunicorn_net.mod gunicorn_net.te
semodule_package -o gunicorn_net.pp -m gunicorn_net.mod
semodule -i gunicorn_net.pp



#Production Deployment
##Gunicorn (WSGI server):

gunicorn --bind 127.0.0.1:5000 app:app
     
# NGINX config (reverse proxy + SSL):

#Forwards port 443 to Gunicorn

#Handles TLS termination


✍️ Author
Pradumna Kumar Barik

#Github


### 📌 Next Steps:
1. Save the above content in a file: `README.md`
2. Run:
   
   git add README.md
   git commit -m "Add README with project overview, usage, and SELinux policy"
   git push


