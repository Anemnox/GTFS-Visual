import React from "react";

import type GTFSObject from "../../definitions/gtfsFormat";

type GTFSTableProps = {
  columns: String[],
  data: GTFSObject[]
}

export default function GTFSTable(props: GTFSTableProps): JSX.Element {
  const renderHeaders = (): JSX.Element[] => {
    console.log("rendering headers!");
    console.log(props);
    return props.columns.map((key, i) => {
      return (
        <th key={"column-name-" + i}>{key}</th>
      );
    });
  }

  const renderData = (): JSX.Element[] => {
    if (!props.data) return null;
    return props.data.map((gtfsObject, index) => {
      return (
        <tr key={"row-" + gtfsObject.uuid}>
          {renderObjectRow(gtfsObject)}
        </tr>
      );
    });
  }

  const renderObjectRow = (gtfsData: GTFSObject): JSX.Element[] => {
    return props.columns.map((column, index) => {
      return (
        <td key={"column-" + gtfsData.uuid + "-" + column}>
          {gtfsData[column as keyof typeof gtfsData]}
        </td>
      );
    });
  }

  return (
    <table>
      <thead>
        <tr>
          {renderHeaders()}
        </tr>
      </thead>
      <tbody>
        {renderData()}
      </tbody>
    </table>
  );
}
