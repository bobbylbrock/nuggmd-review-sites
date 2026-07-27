import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

import cloudflare from "@astrojs/cloudflare";

export default defineConfig({
  integrations: [tailwind(), sitemap()],
  output: "hybrid",
  site: process.env.PUBLIC_SITE_URL ?? 'https://nuggmdreviews.com',
  adapter: cloudflare()
});