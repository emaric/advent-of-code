<svelte:head>
	<title>Home</title>
	<meta name="description" content="aocs - advent of code solutions" />
	<meta property="og:title" content="Advent of Code Solutions" />
</svelte:head>

<script>
	import { onMount } from "svelte";

	let years = $state();
	async function getYears() {
		const res = await fetch('/api/solutions/years');
		const { years:_years } = await res.json();
		years = _years;
	}

	onMount(()=> {
		console.log("onMount...")
		getYears();
	})

</script>

<section>
	<h1>aocs</h1>

	{#each years as year}
		<a href="/solutions/{year}">{year}</a>
	{/each}
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}
</style>
