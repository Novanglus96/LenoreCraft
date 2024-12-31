#!/bin/sh

# Set timezone
if [ -n "$TZ" ]; then
    echo "Setting timezone to $TZ"
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone
else
    echo "Timezone not set, defaulting to UTC"
    ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo "UTC" >/etc/timezone
fi

# Execute the main process
exec "$@"