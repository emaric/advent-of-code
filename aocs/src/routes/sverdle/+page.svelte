<script lang="ts">
	import Modal from '$lib/components/Modal.svelte';
	import { writable } from 'svelte/store';

	let modalOpen = writable(false);
</script>

<!-- svelte-ignore a11y_invalid_attribute -->
<a href="#" onclick={() => modalOpen.set(true)}>Open Modal</a>

<Modal bind:open={modalOpen}>
	<p>Some content here…</p>
	<p>Ctrl + Scroll to adjust font size.</p>
</Modal>
