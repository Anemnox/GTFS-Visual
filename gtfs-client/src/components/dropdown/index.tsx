import React, { useState } from "react";

import { replaceGTFSFile } from "../../tools/projectDataManager";
import {LoadedGTFSProject, ProjectDataContext} from "../../contexts/loadedGTFSProject";

const serverURL = "http://localhost:5000/upload_file"

export default function DropDown(): JSX.Element {
  let [isOpen, setOpen]: [boolean, Function] = useState(false);

  const renderIcon = (): JSX.Element => {
    return (
      <div className="dropdown-icon" onClick={() => setOpen(!isOpen)}>
        TAB
      </div>
    )
  }

  const renderDropDown = (): JSX.Element => {
    return (
      <LoadedGTFSProject.Consumer>
        {projectContext => (
          <div className="dropdown-inputs">
            <input id="videoInput" type="file" accept=".txt, .zip"
                onChange={(event) => handleFile(event, projectContext)} />
            <input type="button" className="download"
              value="Download Video" onClick={() => {
                setOpen(!isOpen);
            }} />
            <input type="button" className="download"
              value="Download Data" onClick={() => {
                setOpen(!isOpen);
            }} />
          </div>
        )}
      </LoadedGTFSProject.Consumer>
    )
  }

  const handleFile = (event: React.ChangeEvent<HTMLInputElement>, projectContext: ProjectDataContext) => {
    console.log(event.target.files[0])
    sendFile("text/plain", event.target.files[0], serverURL).then((response) => {
      let responseJson = JSON.parse(response as string);
      projectContext.updateProject(replaceGTFSFile(responseJson, projectContext.projectData));
    });

    setOpen(!isOpen);
  }

  return (
    <div className="dropdown">
      {renderIcon()}
      {isOpen ? renderDropDown() : null}
    </div>
  );
}

let sendFile = (mimeType: string, file: File, target: string) => {
  let formData = new FormData()
  formData.append("txt", file, file.name);

  return new Promise(function (resolve, reject) {
    let xmlHttpRequest = new XMLHttpRequest();

    xmlHttpRequest.open('POST', target, true);

    xmlHttpRequest.onload = function () {
      if (xmlHttpRequest.status >= 200 && xmlHttpRequest.status < 300) {
        resolve(xmlHttpRequest.response);
      } else {
        reject({
          status: xmlHttpRequest.status,
          statusText: xmlHttpRequest.statusText
        });
      }
    };
    xmlHttpRequest.onerror = function () {
      reject({
        status: xmlHttpRequest.status,
        statusText: xmlHttpRequest.statusText
      });
    };
    xmlHttpRequest.send(formData);
  });
}
