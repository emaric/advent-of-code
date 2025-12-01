<script lang="ts">
	import { resolve } from '$app/paths';
</script>

<svelte:head>
	<title>About</title>
	<meta name="description" content="About Advent of Code Solutions" />
</svelte:head>

<div class="text-column">
	<h1>About AoCS</h1>

	<p>
		AOCS (Advent of Code Solutions) is a website dedicated to displaying run results
		and outputs from the annual <a href="https://adventofcode.com">Advent of Code</a>
		puzzles. Each year brings a new set of programming challenges, and this site
		presents clean, organized results from solving those problems.
	</p>

	<p>
		Additional experimental tools and interactive views may be added over time.
		For now, feel free to explore the run outputs and compare results across days
		and years.
	</p>
</div>

<style>
p {
	margin-top: 3em;
}
</style>