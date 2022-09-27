import React from "react";

import type GTFSProject from "../../definitions/gtfsProject";

export type ProjectDataContext = {
  updateProject: Function,
  projectData: GTFSProject
}

export const LoadedGTFSProject: React.Context<ProjectDataContext> = React.createContext({
  updateProject: ():void => {},
  projectData: {}
});

export default LoadedGTFSProject;
