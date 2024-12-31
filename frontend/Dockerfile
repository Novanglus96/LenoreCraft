# develop stage
FROM node:lts-alpine AS develop-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# build stage
FROM develop-stage AS build-stage
RUN npm run build

# production stage
FROM nginx:stable-alpine AS production-stage
LABEL maintainer="John Adams"
LABEL version="0.0.001"

# Copy build artifacts
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Install tzdata for timezone data
RUN apk add -U tzdata

# Set timezone environment variable (default to UTC if not set)
ARG TZ=Etc/UTC
ENV TIMEZONE=${TZ}

# Link the timezone data
RUN ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime && echo $TIMEZONE >/etc/timezone

# Expose the port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]