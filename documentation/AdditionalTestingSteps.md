

# Running Selenium Tests
While attempting to run the test in the more recent version of selenium, the package required that geckodriver be available on the path.
The following command was tested on Ubuntu.

```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-linux64.tar.gz
tar -xvzf geckodriver-v0.21.0-linux64.tar.gz
rm geckodriver-v0.21.0-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/local/bin/
```

