import type GTFSProject from "../../definitions/gtfsProject";
import type { GTFSObject, GTFSFile } from "../../definitions/gtfsFormat";


export function replaceGTFSFile(newObject: GTFSFile, projectData: GTFSProject) {
  let newProjectState = {...projectData};
  newProjectState[newObject.name as keyof typeof newProjectState] = newObject;
  return newProjectState;
}

export default { replaceGTFSFile };
