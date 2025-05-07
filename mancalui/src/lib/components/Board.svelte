<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import type { Board as BoardType, PlayerType } from '$lib/types';
    
    export let board: BoardType = { 'p1': [4, 4, 4, 4, 4, 4, 0], 'p2': [4, 4, 4, 4, 4, 4, 0] };
    export let turn: PlayerType = 'p1';
    export let isGameOver: boolean = false;
    
    const dispatch = createEventDispatcher<{
      move: { pit: number }
    }>();
    
    const handlePitClick = (player: PlayerType, pitIndex: number) => {
      if (player === 'p1' && turn === 'p1' && !isGameOver && board[player][pitIndex] > 0) {
        dispatch('move', { pit: pitIndex });
      }
    }
    
    const isPitClickable = (player: PlayerType, pitIndex: number): boolean => {
      return player === 'p1' && turn === 'p1' && !isGameOver && board[player][pitIndex] > 0;
    }
  </script>
  
  <div class="board-container">
    <div class="board">
      <div class="mancala mancala-p2">
        <div class="store">
          <span class="stone-count">{board.p2[6]}</span>
        </div>
      </div>
      
      <div class="play-area">
        <div class="pits pits-p2">
          {#each [...Array(6).keys()].reverse() as pitIndex}
            <div class="pit">
              <span class="stone-count">{board.p2[pitIndex]}</span>
            </div>
          {/each}
        </div>
        
        <div class="pits pits-p1">
          {#each [...Array(6).keys()] as pitIndex}
            <div 
              class="pit"
              class:clickable={isPitClickable('p1', pitIndex)}
              on:click={() => handlePitClick('p1', pitIndex)}
            >
              <span class="stone-count">{board.p1[pitIndex]}</span>
            </div>
          {/each}
        </div>
      </div>
      
      <div class="mancala mancala-p1">
        <div class="store">
          <span class="stone-count">{board.p1[6]}</span>
        </div>
      </div>
    </div>
    
    <div class="labels">
      <div class="player-label p2-label">AI (Player 2)</div>
      <div class="player-label p1-label">You (Player 1)</div>
    </div>
    
    <div class="turn-indicator">
      {#if !isGameOver}
        <div class="turn-badge" class:your-turn={turn === 'p1'} class:ai-turn={turn === 'p2'}>
          {turn === 'p1' ? 'Your Turn' : 'AI Turn'}
        </div>
      {/if}
    </div>
  </div>
  
  <style>
    .board-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: 20px;
    }
    
    .board {
      display: flex;
      align-items: center;
      background-color: #8B4513;
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .play-area {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    
    .pits {
      display: flex;
      gap: 10px;
    }
    
    .pit {
      width: 60px;
      height: 60px;
      background-color: #D2B48C;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      font-size: 20px;
      box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    
    .clickable {
      cursor: pointer;
      background-color: #FFD700;
      transition: background-color 0.3s;
    }
    
    .clickable:hover {
      background-color: #FFA500;
      transform: scale(1.05);
    }
    
    .mancala {
      height: 150px;
      width: 70px;
      margin: 0 20px;
    }
    
    .store {
      height: 100%;
      background-color: #D2B48C;
      border-radius: 30px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      font-size: 24px;
      box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.2);
    }
    
    .labels {
      display: flex;
      justify-content: space-between;
      width: 100%;
      margin-top: 10px;
    }
    
    .player-label {
      font-weight: bold;
      margin: 0 100px;
    }
    
    .p1-label {
      color: #4CAF50;
    }
    
    .p2-label {
      color: #2196F3;
    }
    
    .turn-indicator {
      margin-top: 15px;
      height: 30px;
    }
    
    .turn-badge {
      padding: 5px 15px;
      border-radius: 15px;
      font-weight: bold;
    }
    
    .your-turn {
      background-color: #4CAF50;
      color: white;
    }
    
    .ai-turn {
      background-color: #2196F3;
      color: white;
    }
  </style>