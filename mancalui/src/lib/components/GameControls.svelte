<script lang="ts">
    // TODO remove use of deprecated createEventDispatcher
    import { createEventDispatcher } from 'svelte';
    import type { GameMode } from '$lib/types';
    
    export let gameStatus: string = 'Playing';
    export let gameMode: GameMode = 'alphabeta';
    export let depth: number = 2;
    
    const dispatch = createEventDispatcher<{
      restart: void;
      change: Event;
      depthChange: number;
    }>();
    
    function handleRestart(): void {
      dispatch('restart');
    }
    
    function handleModeChange(event: Event): void {
      dispatch('change', event);
    }

    const handleDepthChange = (event: Event): void => { 
      dispatch('depthChange', parseInt((event.target as HTMLInputElement).value));
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
        <label for="ai-depth" class="depth-label">AI Depth (higher is harder):</label>
        <input 
          type="number" 
          id="ai-depth" 
          min="1" 
          max="8"
          bind:value={depth}
          on:change={handleDepthChange}
          class="depth-input"
        />
      </div>
      
      <button class="restart-button" on:click={handleRestart}>
        Restart Game
      </button>
    </div>
  </div>
  
  <style>
  </style>