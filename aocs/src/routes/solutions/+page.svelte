<script lang="ts">
	import { writable } from 'svelte/store';
	import type { PageData } from './$types';
	import Modal from '$lib/components/Modal.svelte';
	import Markdown from '$lib/components/Markdown.svelte';

	interface Props {
		data: PageData;
	}
	let { data }: Props = $props();

	// svelte-ignore non_reactive_update
	let modalOpen = writable(false);
	// svelte-ignore non_reactive_update
	let modalTitle = writable('');
	let modalContent = writable('');

	function showCode(code: string, event: Event) {
		event.preventDefault(); // prevent <a> navigation
		modalContent.set(code);
		modalOpen.set(true);
		modalTitle.set('code');
	}
</script>

<svelte:head>
	<title>Solutions</title>
	<meta name="description" content="About Advent of Code Solutions" />
</svelte:head>

<h1>solutions</h1>

<h2>{data.year}</h2>

<table class="record-table">
	<thead>
		<tr>
			<th>Day</th>
			<th>Part</th>
			<th>Time</th>
			<th>Timestamp</th>
			<th>By</th>
			<th style="text-align: left;">Notes</th>
		</tr>
	</thead>
	<tbody>
		{#each data.records as record}
			<tr>
				<td>{String(record.day).padStart(2, '0')}</td>
				<td>{record.part}</td>
				<td>
					<!-- svelte-ignore a11y_invalid_attribute -->
					<a href="#" onclick={(e) => showCode(record.code.trim(), e)}>
						{record.result_time.toFixed(4)}
					</a>
				</td>
				<td class="timestamp"
					>{record.timestamp.toLocaleString('en-US', {
						year: 'numeric',
						month: '2-digit',
						day: '2-digit',
						hour: '2-digit',
						minute: '2-digit',
						second: '2-digit',
						hour12: false,
						timeZone: 'UTC'
					})}</td
				>
				<td>{record.person}</td>
				<td class="notes">{record.comment}</td>
			</tr>
		{/each}
	</tbody>
</table>

<Modal bind:open={modalOpen} bind:title={modalTitle}>
	<Markdown>
```python
{$modalContent}
```
	</Markdown>
</Modal>

<style>
	h1 {
		margin-bottom: 1em;
	}

	h2 {
		text-align: center;
		margin-bottom: 1em;
	}

	thead th {
		font-weight: 400;
		color: var(--color-theme-2);
	}

	td,
	th {
		text-align: center;
		padding: 0.5em;
	}

	.timestamp {
		font-size: small;
	}

	.notes {
		font-size: small;
		text-align: left;
	}
</style>
