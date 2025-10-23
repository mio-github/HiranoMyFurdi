/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'furdi-pink': '#FF69B4',
        'furdi-pink-light': '#FFE4E1',
        'furdi-pink-dark': '#FF1493',
        'ios-gray': '#F5F5F5',
        'ios-text': '#1C1C1E',
        'ios-text-secondary': '#3A3A3C',
        'ios-separator': '#E5E5E7',
      },
      fontFamily: {
        'sans': ['-apple-system', 'BlinkMacSystemFont', 'SF Pro Text', 'Helvetica Neue', 'sans-serif'],
        'display': ['-apple-system', 'BlinkMacSystemFont', 'SF Pro Display', 'Helvetica Neue', 'sans-serif'],
      },
      boxShadow: {
        'ios': '0 2px 8px rgba(0, 0, 0, 0.1)',
        'ios-card': '0 1px 3px rgba(0, 0, 0, 0.12)',
      },
      borderRadius: {
        'ios': '10px',
        'ios-lg': '20px',
      },
    },
  },
  plugins: [],
}
