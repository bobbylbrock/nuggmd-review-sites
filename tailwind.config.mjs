/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'nugg-blue': '#1E4A7D',
        'nugg-red': '#D46870',
        'nugg-tint': '#7892b1',
        'nugg-dark': '#0f253f',
        'nugg-shade': '#183b64',
        'nugg-shade1': '#aa535a',
        'nugg-tint1': '#dd868d',
        'nugg-green': '#52B781',
        'nugg-block1': '#D2DBE5',
        'nugg-block2': '#F0F0F0',
        'nugg-text': '#060f19',
        'nugg-error': '#F4AC38',
      },
      fontFamily: {
        sans: ["'Futura PT'", "'Century Gothic'", "'Trebuchet MS'", 'sans-serif'],
      },
      borderRadius: {
        brand: '10px',
      },
    },
  },
  plugins: [],
};
