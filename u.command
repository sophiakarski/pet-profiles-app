#!/bin/zsh
# Kill the running EDB postgres
sudo pkill -f "/Library/PostgreSQL/18/bin/postgres"
sudo pkill -f "pgbouncer"

# Remove the EDB installation
sudo rm -rf /Library/PostgreSQL/18
sudo rm -rf /Library/PgBouncer
sudo rm -f /Library/LaunchDaemons/com.edb.launchd.postgresql-18.plist