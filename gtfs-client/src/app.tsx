import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { createRoot } from 'react-dom/client';

import type GTFSProject from "./definitions/gtfsProject";
import type {GTFSFile, GTFSObject} from "./definitions/gtfsFormat";

import { LoadedGTFSProject, ProjectDataContext } from "./contexts/loadedGTFSProject";


import DropDown from "./components/dropdown";
import GTFSTable from "./components/gtfsTable";

let vars = ["d", "fd", "aa", "f"]

function App(): JSX.Element {
  let [loadedGTFSProject, updateLoadedProject]: [GTFSProject, Function] = React.useState({});

  const renderTables = (): JSX.Element[] => {
    let tables = [];
    for (let key in loadedGTFSProject) {
      let value: GTFSFile = loadedGTFSProject[key as keyof GTFSProject];
      console.log(value);
      console.log(value["variables"])
      tables.push(
        <GTFSTable
          key={value.name}
          columns={value.variables}
          data={value.data}
          />
      );
    }

    return tables;
  }

  return (
    <div>
      <LoadedGTFSProject.Provider value={{
        updateProject: updateLoadedProject,
        projectData: loadedGTFSProject
      }}>
        <DropDown />
        {renderTables()}
      </LoadedGTFSProject.Provider>
    </div>
  );
}

function render(): void {
  const container = document.getElementById("GTFSApp");
  const root = createRoot(container);
  root.render(<App />);
}

render();
