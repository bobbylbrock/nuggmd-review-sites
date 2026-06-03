import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  integrations: [tailwind(), sitemap()],
  output: 'static',
  site: process.env.PUBLIC_SITE_URL ?? 'https://nuggmdreviews.com',
});
