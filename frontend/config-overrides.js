var BundleTracker = require('webpack-bundle-tracker');
const _ = require('underscore');

module.exports = {
    webpack: (config, env) => {
        config.plugins.push(
            new BundleTracker({
                path: __dirname,
                filename: './build/webpack-stats.json',
            }),
        );
        config.optimization.splitChunks.name = 'vendors';

        return config;
    },
};
