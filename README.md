# Streamlit Demo Application
     
## References:     
- https://medium.com/crossml/streamlit-2256000541ad      
- https://medium.com/nerd-for-tech/how-to-deploy-streamlit-dashboard-with-heroku-ca00064402e8      
     
## Quick Start:     
1. Clone this repository, and cd to its folder     
2. Ramp up a virtual-environment:     
   - % python3 -m venv env     
   - % source env/bin/activate     
   - % pip install -r requirements.txt     
3. Run:     
   - % streamlit run app.py     
4. Open your browser, and go to: http://localhost:8501     
   (exit with ctrl+c)
    
## Heroku deploy   
Relevant files:   Procfile, setup.sh, runtime.txt     
WebApp URL:  https://streamlit-demo-webapp.herokuapp.com     
     
### Requirements     
- Clone the project's Git repository
- Create a new Heroku webApp + connect to Git
- Install Heroku CLI + Login
- Bind the app with Heroku CLI:
```heroku git:remote -a <appName>```

### Deploy
```
% git push heroku master
```
