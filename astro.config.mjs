import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://YangJunJoo.github.io',
  base: '/YangJunSite',
  integrations: [tailwind()],
  output: 'static',
});
