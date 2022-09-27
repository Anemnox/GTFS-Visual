import type {GTFSFile} from "./gtfsFormat";


type GTFSProject = {
  [gtfsFileName: string]: GTFSFile | undefined | null
}

export default GTFSProject;
