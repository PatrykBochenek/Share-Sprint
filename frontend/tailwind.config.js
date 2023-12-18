module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  content: [
    // './src/**/*.{html,js}',
    'node_modules/preline/dist/*.js',
  ],
  plugins: [
    require('preline/plugin'),
  ],
};
