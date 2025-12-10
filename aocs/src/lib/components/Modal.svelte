<script lang="ts">
	import { writable } from 'svelte/store';

	export let open = writable(false); // control modal visibility
    export let title = writable('');
	let fontSize = 12; // initial font size in px
	let width = 800;
	let height = 600;

	function close() {
		open.set(false);
	}

	// Ctrl + scroll to adjust font size
	function handleWheel(event: WheelEvent) {
		if (event.ctrlKey) {
			event.preventDefault(); // prevent zooming the page
			if (event.deltaY < 0) fontSize += 1;
			else fontSize = Math.max(8, fontSize - 1);
		}
	}

	let resizer: HTMLDivElement;

	// Optional: drag to resize
	let isResizing = false;
	let startX: number, startY: number, startWidth: number, startHeight: number;

	function pointerDown(event: PointerEvent) {
		isResizing = true;
		startX = event.clientX;
		startY = event.clientY;
		startWidth = width;
		startHeight = height;
		window.addEventListener('pointermove', pointerMove);
		window.addEventListener('pointerup', pointerUp);
	}

	function pointerMove(event: PointerEvent) {
		if (!isResizing) return;
		width = Math.max(200, startWidth + event.clientX - startX);
		height = Math.max(100, startHeight + event.clientY - startY);
	}

	function pointerUp() {
		isResizing = false;
		window.removeEventListener('pointermove', pointerMove);
		window.removeEventListener('pointerup', pointerUp);
	}
</script>

{#if $open}
	<!-- svelte-ignore a11y_click_events_have_key_events -->
	<!-- svelte-ignore a11y_no_static_element_interactions -->
	<div class="backdrop" onclick={close}></div>

	<div
		class="modal"
		onwheel={handleWheel}
		style="width:{width}px; height:{height}px; font-size:{fontSize}px;"
	>
		<div class="modal-header">
			<span>{$title}</span>
			<button class="close-btn" onclick={close}>×</button>
		</div>

		<div class="modal-body">
			<slot></slot>
		</div>

		
	</div>
{/if}

<style>
	.backdrop {
		position: fixed;
		inset: 0;
		background: rgba(0,0,0,0.5);
		z-index: 10;
	}

	.modal {
		position: fixed;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		background: rgb(22,22,29);
		border-radius: 8px;
		box-shadow: 0 0 20px rgba(0,0,0,0.6);
		display: flex;
		flex-direction: column;
		overflow: hidden;
		z-index: 11;
		max-width: 100vw;
		max-height: 100vh;
	}

	.modal-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 0.5rem 1rem;
		background: rgb(12,12,19);
		cursor: move; /* optional: indicate draggable */
	}

	.close-btn {
		background: none;
		border: none;
		font-size: 1.2rem;
		cursor: pointer;
        color: var(--color-theme-1);
	}

	.modal-body {
		flex: 1;
		padding: 1rem;
		overflow: auto;
	}

	.resizer {
		width: 16px;
		height: 16px;
		background: var(--color-theme-2);
		position: absolute;
		right: 0;
		bottom: 0;
		cursor: se-resize;
	}
</style>
