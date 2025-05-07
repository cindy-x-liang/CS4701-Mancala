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
    
    <div class="help-panel">
      <details>
        <summary>How to Play</summary>
        <div class="help-content">
          <p><strong>Goal:</strong> Collect more stones in your store (large pit on the right) than the AI.</p>
          <p><strong>Rules:</strong></p>
          <ul>
            <li>Click on one of your pits to pick up all stones from that pit.</li>
            <li>Stones are distributed one by one counter-clockwise.</li>
            <li>If your last stone lands in your store, you get another turn.</li>
            <li>If your last stone lands in an empty pit on your side, you capture that stone and all stones in the opponent's pit directly across.</li>
            <li>Game ends when all pits on one side are empty.</li>
          </ul>
        </div>
      </details>
    </div>
  </div>
  
  <style>
    .controls {
      display: flex;
      flex-direction: column;
      gap: 15px;
      width: 100%;
    }
    
    .status-panel {
      background-color: #f8f9fa;
      border-radius: 10px;
      padding: 10px;
      border: 1px solid #dee2e6;
    }
    
    .status-message {
      margin: 0;
      font-weight: 500;
      color: #333;
    }
    
    .control-panel {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: #f8f9fa;
      border-radius: 10px;
      padding: 15px;
      border: 1px solid #dee2e6;
    }
    
    .mode-selector {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .mode-selector label {
      font-weight: 500;
    }
    
    .mode-selector select {
      padding: 8px;
      border-radius: 5px;
      border: 1px solid #ced4da;
      background-color: white;
      cursor: pointer;
    }
    
    .restart-button {
      background-color: #6c757d;
      color: white;
      border: none;
      padding: 8px 15px;
      border-radius: 5px;
      cursor: pointer;
      font-weight: 500;
      transition: background-color 0.3s;
    }
    
    .restart-button:hover {
      background-color: #5a6268;
    }
    
    .help-panel {
      background-color: #f8f9fa;
      border-radius: 10px;
      padding: 10px;
      border: 1px solid #dee2e6;
    }
    
    details summary {
      cursor: pointer;
      font-weight: 500;
      padding: 5px 0;
    }
    
    .help-content {
      padding: 10px;
      font-size: 0.9em;
    }
    
    .help-content ul {
      margin-top: 5px;
      padding-left: 20px;
    }
  </style>