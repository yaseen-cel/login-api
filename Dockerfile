
COPY requirements.txt .
RUN CRYPTOGRAPHY_DONT_BUILD_RUST=1 pip3 install -r requirements.txt

