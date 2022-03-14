FROM node:16-buster

# Install packages
RUN apt-get update \
    && apt-get install -y supervisor curl \
    && rm -rf /var/lib/apt/lists/*

# Add application
WORKDIR /home/node
COPY challenge .

# Setup flag
RUN echo "Pwned{f4k3_fl4g_f0r_t3st1ng}" > /home/node/flag.txt

# Setup superivsord
COPY config/supervisord.conf /etc/supervisord.conf

# Install dependencies
RUN npm install

# Expose the port node-js is reachable on
EXPOSE 3333

# Start the node-js application
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
