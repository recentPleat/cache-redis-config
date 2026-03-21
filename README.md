# cache-redis-config
======================================================

## Description

`cache-redis-config` is a lightweight, configurable Redis cache implementation for Node.js applications. It provides a simple and intuitive API for storing and retrieving data from Redis, with optional caching and configuration options.

## Features

### Key Features

*   **Configurable**: Easily customize cache behavior, expiration, and Redis connection settings
*   **Flexible API**: Simple and intuitive API for storing and retrieving data from Redis
*   **Multi-environment support**: Seamlessly switch between debug, development, and production environments
*   **Multi-cache support**: Store and retrieve data from multiple Redis instances

### Benefits

*   **Improved performance**: Reduce the number of database queries and improve application responsiveness
*   **Enhanced security**: Store sensitive data securely in Redis, with optional encryption
*   **Scalable architecture**: Easily integrate with microservices and distributed systems

## Technologies Used

*   **Node.js**: The project is built using Node.js and utilizes its asynchronous I/O capabilities
*   **Redis**: The project utilizes the Redis client library to interact with Redis instances
*   **Typescript**: The project uses TypeScript for type checking and code maintenance
*   **ESLint**: The project uses ESLint for code linting and quality checks

## Installation

### Prerequisites

*   **Node.js**: Install Node.js (>=14.17.0) on your system
*   **Redis**: Install Redis on your system and configure it for use with this project
*   **npm**: Install npm (>=6.14.13) on your system

### Installation Steps

1.  **Clone the repository**: Clone the repository using your preferred method (e.g., `git clone`)
2.  **Install dependencies**: Run `npm install` to install all project dependencies
3.  **Configure environment variables**: Set environment variables for Redis connection settings (e.g., `REDIS_HOST`, `REDIS_PORT`)
4.  **Start the project**: Run `npm start` to start the project in development mode
5.  **Test the project**: Run `npm test` to execute unit tests and integration tests

## Usage

### Basic Usage

```typescript
import { RedisCache } from 'cache-redis-config';

const cache = new RedisCache({
  host: 'localhost',
  port: 6379,
});

// Set data in Redis
cache.set('key', 'value');

// Retrieve data from Redis
const retrievedValue = cache.get('key');
```

### Advanced Usage

```typescript
import { RedisCache } from 'cache-redis-config';

const cache = new RedisCache({
  host: 'localhost',
  port: 6379,
  expiration: 60, // 1 minute
  encryption: true,
});

// Set data with expiration and encryption
cache.set('key', 'value', { expiration: 60, encryption: true });

// Retrieve data with expiration and encryption
const retrievedValue = cache.get('key', { expiration: 60, encryption: true });
```

## Contributing

Contributions are welcome and encouraged! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to contribute to the project.

## License

`cache-redis-config` is released under the [MIT License](LICENSE.md).

## Author

The author of this project is [Your Name](https://yourname.com).

## Versioning

We use [SemVer](https://semver.org/) for versioning. For the changelog, please see the [CHANGELOG.md](CHANGELOG.md) file.