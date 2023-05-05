import {Match} from "./Match";
import {BetsResult} from "./BetsResult";

export interface Competition {
    id: string,
    name: string,
    is_active: boolean,
    matches: Match[],
    leader_board?: BetsResult[],
    created_by?: string
}