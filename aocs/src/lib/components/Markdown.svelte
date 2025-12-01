<script lang="ts">
	import { onMount } from 'svelte';
	import { writable } from 'svelte/store';
	import * as shiki from 'shiki';

	let rendered = writable('');
	let container: HTMLDivElement;
	let source = '';

	onMount(async () => {
		source = container.textContent ?? '';

		// Create highlighter with required options
		const highlighter = await shiki.createHighlighter({
			// GitHub theme
			themes: ['github-dark'],

			// Include languages you plan to highlight
			langs: ['python']
		});

		// Regex for fenced code blocks: ```lang ... ```
		const codeBlockRegex = /```(\w+)?\n([\s\S]*?)```/g;

		const html = source.replace(codeBlockRegex, (_, lang = 'text', code) => {
			return highlighter.codeToHtml(code, { lang, theme: 'github-dark' });
		});

		rendered.set(html);
	});

    
    let fontSize = 14; // initial font size in px
    // Ctrl + scroll to adjust font size
	function handleWheel(event: WheelEvent) {
		if (event.ctrlKey) {
			event.preventDefault(); // prevent zooming the page
			if (event.deltaY < 0) fontSize += 1;
			else fontSize = Math.max(8, fontSize - 1);
		}
	}
</script>

<!-- Hidden slot container -->
<div bind:this={container} style="display: none;">
	<slot></slot>
</div>

<div class="rendered" onwheel={handleWheel} style="--font-size: {fontSize}px;">
<!-- Render highlighted HTML -->
{@html $rendered}
</div>