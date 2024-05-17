const { overrideDevServer } = require('customize-cra');

const devServerConfig = () => config => {
  return {
    ...config,
    allowedHosts: 'all', // Adjust this as needed
  };
};

module.exports = {
  devServer: overrideDevServer(devServerConfig())
};

