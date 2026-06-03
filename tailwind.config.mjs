/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'nugg-blue':   'var(--nugg-blue)',
        'nugg-red':    'var(--nugg-red)',
        'nugg-tint':   'var(--nugg-tint)',
        'nugg-dark':   'var(--nugg-dark)',
        'nugg-shade':  'var(--nugg-shade)',
        'nugg-shade1': 'var(--nugg-shade1)',
        'nugg-tint1':  'var(--nugg-tint1)',
        'nugg-green':  '#52B781',
        'nugg-block1': 'var(--nugg-block1)',
        'nugg-block2': '#F0F0F0',
        'nugg-text':   'var(--nugg-text)',
        'nugg-error':  '#F4AC38',
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
