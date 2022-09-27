import type { GTFSObject, GTFSFile } from "../../definitions/gtfsFormat";

function buildEmptyGTFSFile(name: string, variables: string[]=[]): GTFSFile {
  return {
    name: name,
    variables: variables,
    data: []
  }
}

export default { buildEmptyGTFSFile }
