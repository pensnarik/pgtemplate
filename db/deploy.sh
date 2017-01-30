#!/bin/bash

psql -U postgres -f drop.sql -v database_name="$DATABASE_NAME"
psql -U postgres -f install.sql -v database_name="$DATABASE_NAME"
