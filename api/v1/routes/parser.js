// parser.js
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

class RedisConfigParser {
  parseConfig(filename) {
    const configPath = path.resolve(filename);
    const fileBuffer = fs.readFileSync(configPath);
    const data = yaml.safeLoad(fileBuffer);
    if (!data) {
      throw new Error('Invalid YAML configuration file');
    }
    if (!data.redis) {
      throw new Error('Configuration file missing redis section');
    }
    return data.redis;
  }
}

module.exports = RedisConfigParser;