#!/bin/sh

# Set timezone
if [ -n "$TZ" ]; then
    echo "Setting timezone to $TZ"
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ >/etc/timezone
else
    echo "Timezone not set, defaulting to UTC"
    ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo "UTC" >/etc/timezone
fi

# Load environment variables from .env file
cat <<EOF > /usr/share/nginx/html/config.js
window.__APP_CONFIG__ = {
  VITE_API_KEY: "${VITE_API_KEY}"
};
EOF

# Execute the main process
exec "$@"
