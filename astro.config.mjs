import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://valbuilds.github.io',
	base: 'niabot',
	integrations: [
		starlight({
			title: 'Nia',
			social: {
				github: 'https://github.com/valbuilds/niabot',
			},
			sidebar: [
				{
					label: 'Usage Guide',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Intro', link: '/usage/home' },
						{ label: 'Hosting the Bot', link: '/usage/hosting' },
					],
				},
			],
		}),
	],
});
