export type PlayerType = 'p1' | 'p2';

export interface Board {
  p1: number[];
  p2: number[];
}

export interface GameState {
  board: Board;
  turn: PlayerType;
}

export interface NextStateResponse {
  board: Board;
  turn: PlayerType;
  error?: string;
}

export interface AIActionResponse {
  action: number;
  error?: string;
}

export type GameMode = 'minimax' | 'alphabeta' | 'minimax_half';