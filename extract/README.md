# STEP 1 - Execute following script in RoboMongo Shell ####

# Note Update DeviceId and Trasnmit Times to the ones you want

```
var cursor = db.getCollection('telemetry').find({'deviceId' : '300234064222900' ,'transmitTime' : 
{ $gte : new ISODate('2017-07-18T20:00:04.000Z'),
   $lte: new ISODate('2017-07-20T23:05:46.000Z')}})

var telemetry = cursor.toArray();
print (telemetry);

for(i=0;i < telemetry.length;i++) {
    if(i==0)
        print('Latitude',",",'Longitude',",",'Altitude',",",'Temperature',",",'Barometer',",",'Sound',",",'Transmit Time',",",'DeviceId')
   
   if(telemetry[i].sensors)
   {
    print (telemetry[i].location.coordinates[1],",",
           telemetry[i].location.coordinates[0],",",
           telemetry[i].altitude,",",
           telemetry[i].sensors.temperature,",",
           telemetry[i].sensors.barometer,",",
           telemetry[i].sensors.sound,",",
           telemetry[i].transmitTime,",",
           telemetry[i].deviceId)
   }
}

```

# STEP 2 - Copy paste the results in logs.txt file in this directory ###

# STEP 3 - Run formatAndCustomizeCSV (Just formats the csv)
cd extract  and run python formatAndCustomizeCSV.py 'MAVERICK20160620'. (Here MAVERICK20160620 is the dynamic filename you want for the csv callsign and flightDate)

# STEP 4 - Add creds to use plot line
   Now we will use plotly to generate some graphs for the attached csv data
   # Prerequisites
   Create a free account on plotly.com and then regenerate key to get your api key
   Enter python interpreter on the terminal
     ```
     python

     import plotly  
     plotly.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
     ```
     cat  ~/.plotly/.credentials to see (Credentials must have been set)

# STEP 5 Update following environment variables to be able to send emails
PLOTLY_EMAIL_USERNAME
PLOTLY_EMAIL_PASSWORD
     

# STEP 6 Run plotLine.py  (Generates line chart and emails graph reports)
It will ask for filename for csv and x-axis and y-axis keys). Once you provide those options it will generate up/down plots for you in the browser (provided you are signed in) and send emails to recepients.
Just click on export to download jpeg versions of that.


