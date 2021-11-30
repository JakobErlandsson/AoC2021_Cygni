FROM python:3.10
WORKDIR /src
COPY solution.py ./ input.txt ./ requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt
CMD python3 ./solution.py