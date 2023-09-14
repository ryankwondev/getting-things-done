# syntax=docker/dockerfile:1

# Build frontend
FROM node:14 AS frontend-build
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Build backend
FROM python:3.9 AS backend-build
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt
COPY backend/ ./

# Final stage
FROM nginx:alpine
COPY --from=frontend-build /app/build /usr/share/nginx/html
COPY --from=backend-build /app /app
RUN apk add --no-cache uwsgi-python3
COPY nginx.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]
