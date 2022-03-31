# JSON READER:
#### JSON Data Management Module

## Common Terms:

key: file name to save/pull from (Stored as data_[key].json)

## Functions

### create_file()

#### Creates a Key
#### Returns: Success(T/F)

ex.
```
if(guildreader.create_file(self.bot, "mutes", {}))
```

* bot: Bot Instance
* key: File/Key to make
* default: Default value stored for each guild
* wipe: Wipes the file if it exists

### read_file()

ex.
```
data = guildreader.read_file(ctx.guild.id, "mutes")
data[USER] = int(time.time+300)
```

#### Read a Key from a guild ID
#### Returns: JSON for that guild

* guild: ID of the guild
* key: File/Key to read

### write_file()

ex.
```
guildreader.write_file(ctx.guild.id, "mutes", data)
```

#### Write to a key
#### Returns: Success(T/F)

* guild: ID of the guild
* key: File/Key to read
* value: Modified Value

### remove()

#### Remove a guild from a Key
#### Returns: Success(T/F)

ex.
```
def on_guild_remove(self, guild):
  guildreader.remove(guild.id, "mutes")
```

* guild: ID of the guild
* key: File/Key to remove guild from

### check_exist()

```
if(guildreader.check_exists("mutes"))
```

#### Checks if a Key exists
#### Returns: Success(T/F)

* key: Check the existance of a key/file

### dump()

```
json = guildreader.dump("mutes")
```

#### Dumps the entire JSON
#### Returns: JSON of the Key

* key: Key to dump full json from
