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

<table class="record-table">
	<thead>
		<tr>
			<th>Year</th>
			<th>Day</th>
			<th>Part</th>
			<th>Result Time (seconds)</th>
			<th>Timestamp</th>
			<th>Owner</th>
			<th>Code</th>
		</tr>
	</thead>
	<tbody>
		{#each data.records as record}
			<tr>
				<td>{record.year}</td>
				<td>{String(record.day).padStart(2, '0')}</td>
				<td>{record.part}</td>
				<td>{record.result_time.toFixed(6)}</td>
				<td>{record.timestamp.toLocaleString()}</td>
				<td>{record.person}</td>
				<td>
					<!-- svelte-ignore a11y_invalid_attribute -->
					<a href="#" onclick={(e) => showCode(record.code, e)}> View Code </a>
				</td>
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

	thead th {
		font-weight: 400;
		color: var(--color-theme-1);
	}

	td,
	th {
		text-align: center;
		padding: 0.5em;
	}
</style>
