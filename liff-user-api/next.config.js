/** @type {import('next').NextConfig} */
const nextConfig = {
    env: {
        USER_LIFF_ID: process.env.LIFF_ID,
        USER_IDENTITY_TABLE_TOKEN: process.env.IDENTITY_TABLE_TOKEN,
    },
}

module.exports = nextConfig
