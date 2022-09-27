export type GTFSObject = {
  uuid: String,
  [ key: string ]: String | null
}

export type GTFSFile = {
  name: string,
  variables: string[],
  data: GTFSObject[]
}

export default GTFSObject;
