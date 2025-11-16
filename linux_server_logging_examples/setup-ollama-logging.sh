#!/bin/bash
# Setup script for Ollama plain text logging

set -e

echo "Step 1: Creating log directory..."
sudo mkdir -p /var/log/ollama

echo "Step 2: Setting ownership..."
sudo chown ollama:ollama /var/log/ollama

echo "Step 3: Setting permissions..."
sudo chmod 755 /var/log/ollama

echo "Step 4: Backing up current service file..."
sudo cp /etc/systemd/system/ollama.service /etc/systemd/system/ollama.service.backup.$(date +%Y%m%d_%H%M%S)

echo "Step 5: Installing modified service file..."
sudo cp /tmp/ollama.service.new /etc/systemd/system/ollama.service

echo "Step 6: Reloading systemd daemon..."
sudo systemctl daemon-reload

echo "Step 7: Restarting ollama service..."
sudo systemctl restart ollama

echo "Step 8: Checking service status..."
sudo systemctl status ollama --no-pager -l

echo ""
echo "Step 9: Waiting 2 seconds for logs to be written..."
sleep 2

echo "Step 10: Checking log file..."
ls -lh /var/log/ollama/
echo ""
echo "Latest log entries:"
sudo tail -20 /var/log/ollama/ollama.log

echo ""
echo "Step 11: Installing log rotation configuration..."
sudo cp /tmp/logrotate-ollama /etc/logrotate.d/ollama

echo ""
echo "Setup complete!"
echo ""
echo "You can now view logs with:"
echo "  tail -f /var/log/ollama/ollama.log"
echo "  grep 'pattern' /var/log/ollama/ollama.log"
echo "  cat /var/log/ollama/ollama.log"