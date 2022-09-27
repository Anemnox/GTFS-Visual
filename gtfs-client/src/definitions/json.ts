type JSONValue = {
  | string
  | number
  | boolean
  | { [x: string]: JSONValue }
  | Array<JSONValue>
  | null
}

export default JSONValue;
