FROM python:3.10.12

# Set the working directory
WORKDIR /workspace

# Check if the requirements.txt file exists
COPY requirements.txt /workspace

# Copy the current directory contents into the container at /workspace
COPY . /workspace

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80