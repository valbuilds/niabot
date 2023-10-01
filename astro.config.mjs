import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'My Docs',
			social: {
				github: 'https://github.com/withastro/starlight',
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
