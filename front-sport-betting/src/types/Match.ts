import {Bets} from "./Bets";

export interface Match {
    id: string,
    name: string,
    first_team_name: string,
    second_team_name: string,
    first_team_result?: bigint,
    second_team_result?: bigint,
    is_active: boolean,
    bets_result?: number,
    user_bets?: Bets[],
    start_time?: string,
    special_bets?: string[]
}