<script lang="ts">
    // TODO remove use of deprecated createEventDispatcher
    import { createEventDispatcher } from 'svelte';
    import type { GameMode } from '$lib/types';
    
    export let gameStatus: string = 'Playing';
    export let gameMode: GameMode = 'alphabeta';
    
    const dispatch = createEventDispatcher<{
      restart: void;
      change: Event;
    }>();
    
    function handleRestart(): void {
      dispatch('restart');
    }
    
    function handleModeChange(event: Event): void {
      dispatch('change', event);
    }
  </script>
  
  <div class="controls">
    <div class="status-panel">
      <p class="status-message">{gameStatus}</p>
    </div>
    
    <div class="control-panel">
      <div class="mode-selector">
        <label for="game-mode">AI Strategy:</label>
        <select id="game-mode" bind:value={gameMode} on:change={handleModeChange}>
          <option value="minimax">Minimax</option>
          <option value="alphabeta">Alpha Beta</option>
          <option value="minimax_half">Random (50% Minimax)</option>
        </select>
      </div>
      
      <button class="restart-button" on:click={handleRestart}>
        Restart Game
      </button>
    </div>
  </div>
  
  <style>
  </style>