# JSON READER:
#### JSON Data Management Module

## Common Terms:

key: file name to save/pull from (Stored as data_[key].json)

# CLS: Reader(directory, ids: list)

  ### create_file()

  #### Creates a Key
  #### Returns: Success(T/F)

  ex.
  ```
  reader.create_file("mutes", {}))
  ```

  * key: File/Key to make
  * default: Default value stored for each id
  * wipe: Wipes the file if it exists

  ### read_file()

  #### Read a Key from a ID
  #### Returns: JSON for that ID

  ex.
  ```
  data = reader.read_file(id, "mutes")
  data[USER] = int(time.time+300)
  ```

  * id: ID to read
  * key: File/Key to read

  ### write_file()

  #### Write to a key
  #### Returns: Success(T/F)

  ex.
  ```
  reader.write_file(id, "mutes", data)
  ```

  * ID: ID to write to
  * key: File/Key to write to
  * value: Modified Value

  ### remove()

  #### Remove a id from a key
  #### Returns: Success(T/F)

  ex.
  ```
    reader.remove(id, "mutes")
  ```

  * id: ID to remove
  * key: File/Key to remove id from

  ### check_exist()

  #### Checks if a Key exists
  #### Returns: Success(T/F)

  ```
  reader.check_exists("mutes")
  ```

  * key: Check the existance of a key/file

  ### dump()

  #### Dumps the entire JSON
  #### Returns: JSON of the Key

  ```
  json = reader.dump("mutes")
  ```

  * key: Key to dump json from
