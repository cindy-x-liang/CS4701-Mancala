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
    .board {
      display: flex;
      align-items: center;
      background-color: #8B4513;
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .pits {
      display: flex;
      gap: 10px;
    }
    
    .clickable {
      cursor: pointer;
      background-color: #FFD700;
    }
  </style>