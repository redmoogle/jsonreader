# JSON READER:
#### DiscordPy GuildData Management Module

## Important Info:

A /data folder must exist

## Common Terms:

key: file name to save/pull from (Stored as guild_KEY.json)
guild: ID of the guild (automatically turned into a string)

## Functions

### create_file()

#### Creates a Key
#### Returns: Success(T/F)

* bot: Bot Instance
* key: File/Key to make
* default: Default value stored for each guild
* wipe: Wipes the file if it exists

### read_file()

#### Read a Key from a guild ID
#### Returns: JSON for that guild

* guild: ID of the guild
* key: File/Key to read

### write_file()

#### Write to a key
#### Returns: Success(T/F)

* guild: ID of the guild
* key: File/Key to read
* value: Modified Value

### remove()

#### Remove a guild from a Key
#### Returns: Success(T/F)

* guild: ID of the guild
* key: File/Key to remove guild from

### check_exist()

#### Checks if a Key exists
#### Returns: Success(T/F)

* key: Check the existance of a key/file

### dump()

#### Dumps the entire JSON
#### Returns: JSON of the Key

* key: Key to dump full json from
