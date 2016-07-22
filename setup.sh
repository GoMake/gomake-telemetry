export DB_PATH=/opt/telemetry-data/data.db
export APP_PATH=/opt/gomake-telemetry/
export GPS_BAUD=4800
export GPS_PATH=/dev/ttyS0
export SAT_BAUD=19200
export SAT_PATH=/dev/usbserial

if [ ! -f $DB_PATH ]; then
    echo "gomake-telemetry: creating database file..."
    sqlite3 $DB_PATH
fi