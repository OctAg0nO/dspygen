/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/jsx', // Prefix for your API calls
        destination: 'http://localhost:888/jsx', // Your FastAPI backend
      },
      {
        source: '/html', // Prefix for your API calls
        destination: 'http://localhost:888/html', // Your FastAPI backend
      },
    ];
  },
};

module.exports = nextConfig;