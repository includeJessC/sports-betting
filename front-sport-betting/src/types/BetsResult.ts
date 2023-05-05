import {Bets} from "./Bets";

export interface BetsResult {
    user_id: string,
    bets: Bets[],
    result?: number
}