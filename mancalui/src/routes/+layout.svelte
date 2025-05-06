<script lang="ts">
  </script>
  
  <div class="app">
	<slot />
  </div>
  
  <style>
	:global(body) {
	  margin: 0;
	  padding: 0;
	  font-family: sans-serif;
	  background-color: #f0f0f0;
	}

	.app {
	  display: flex;
	  flex-direction: column;
	  min-height: 100vh;
	}
  </style>