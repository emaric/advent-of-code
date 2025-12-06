<script lang="ts">
	import { goto } from '$app/navigation';
	import { writable } from 'svelte/store';
	import type { PageData } from './$types';
	import Modal from '$lib/components/Modal.svelte';
	import Markdown from '$lib/components/Markdown.svelte';
	import { onMount } from 'svelte';

	interface Props {
		data: PageData;
	}
	let { data: _data }: Props = $props();

	let data = $state({ ..._data });

	onMount(async () => {
		await updateDays(_data.year);
		await updateData(_data.year, _data.day);
	});

	$effect(() => {
		const yearParam = _data.year;
		const dayParam = _data.day;
		updateDays(yearParam);
		updateData(yearParam, dayParam);
	});

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

	async function updateData(year: number, day: number) {
		if (day <= 0) {
			data.day = 0
			await updateDays(year)
		} else {
			const res = await fetch(`/api/solutions/${year}/${day}`);
			let { records } = await res.json();
			records = records.map((r: any) => {
				return {
					...r,
					timestamp: new Date(Date.parse(r.timestamp))
				};
			});
			data = { ...data, records, year, day };
		}
	}

	async function updateDays(year: number) {
		const res = await fetch(`/api/solutions/${year}/days`);
		const newDays = await res.json();
		data.days = newDays.days;
		if (data.day == 0) {
			data.day = data.days.at(-1) ?? 1;
			goto(`/solutions/${year}/${data.day}`);
		}
	}

	function timeAgo(utc: Date): string {
		const diff = Date.now() - utc.getTime();

		const units = [
			{ name: 'year', ms: 365 * 24 * 60 * 60 * 1000 },
			{ name: 'month', ms: 30 * 24 * 60 * 60 * 1000 },
			{ name: 'day', ms: 24 * 60 * 60 * 1000 },
			{ name: 'hour', ms: 60 * 60 * 1000 },
			{ name: 'minute', ms: 60 * 1000 },
			{ name: 'second', ms: 1000 }
		];

		for (const u of units) {
			const val = Math.floor(diff / u.ms);
			if (val > 0) {
				return val === 1 ? `1 ${u.name} ago` : `${val} ${u.name}s ago`;
			}
		}

		return 'just now';
	}
</script>

<svelte:head>
	<title>Solutions</title>
	<meta name="description" content="About Advent of Code Solutions" />
</svelte:head>

<h1>{data.year}</h1>

<div class="days-container">
	<div>
		{#each data.days as day}
			<a class={day == data.day ? 'selected' : ''} href="/solutions/{data.year}/{day}"
				>{String(day).padStart(2, '0')}</a
			>
		{/each}
	</div>
</div>

<table class="record-table">
	<thead>
		<tr>
			<th>Day</th>
			<th>Part</th>
			<th>Time</th>
			<th>By</th>
			<th style="text-align: left;">Notes</th>
			<th>Timestamp</th>
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
				<td>{record.person}</td>
				<td class="notes">{record.comment}</td>
				<td class="timestamp">{timeAgo(record.timestamp)}</td>
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
		font-weight: 200;
		color: var(--color-text);
	}

	td,
	th {
		text-align: center;
		padding: 0.5rem;
	}

	.timestamp {
		font-size: x-small;
	}

	.notes {
		width: 100%;
		font-size: small;
		text-align: left;
	}

	.days-container {
		display: grid;
		justify-items: center;
		margin-bottom: 1rem;
	}

	.days-container a {
		margin: 1rem;
	}

	.days-container a::before {
		content: '[';
	}

	.days-container a::after {
		content: ']';
	}

	a.selected {
		color: var(--color-text);
	}

	a.selected:hover {
		cursor: default;
	}

	a.selected::before {
		content: '';
	}

	a.selected::after {
		content: '';
	}
</style>
