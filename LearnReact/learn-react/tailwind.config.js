/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{html,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Helvetica', 'Arial', 'sans-serif'], // Example of a sans-serif font stack
        serif: ['Georgia', 'serif'],               // Example of a serif font stack
        mono: ['Menlo', 'Monaco', 'monospace'],    // Example of a monospace font stack
      }, 
      gridTemplateColumns: {
        '70/30': '70% 28%',
      }
    },
  },
  plugins: [],
}