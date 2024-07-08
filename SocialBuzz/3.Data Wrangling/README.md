# Data Wranging with Excel

- Remove columns which are not relevant to the task in each dataset.
- Merge datasets into one dataset or table

## Wrangling process

Content table headers(Type and Category) renamed as (ContentType and ContentCategory) due to comflict they were going to cause during column merging. ReactionType table headers(Type and Score) were also renamed as (ReactionType and ReactionScore). Reactions table header(Type) renamed as (ReactionType), related according to the Data Model.

1. Content table headers(ID, ContentID, UserID, ContentType, ContentCategory, URL)
2. ReactionType table headers(ID, ReactionType, Sentiment, ReactionScore)
3. Reactions table headers(ID, ContentID, UserID, ReactionType, Datetime)

## Columns removed

- Content: I removed UserID and URL, since they were not going to help answer our project's business question/objective.
- ReactionType: No columns were removed on this file, as all the columns are going to be merged due to the relation they have with other tables according to the ##Data Model##.
- Reactions: UserID column.

## Data turned into tables

- Ctrl + T, table has headers enabled.

## Columns Added

- Month and Year

## Columns Merged(Reactions(merged))

- Content: ContentID, ContentType, and ContentCategory
- ReactionType: ReactionType, Sentiment, and ReactionScore
- Reactions: ID, ContentID, ReactionType, and Datetime

## Merging process

1. Copy table2 into table1.
2. Make a new column in table1.
3. Use VLookUp() function to copy from table2 into table1.
4. Use Autofill to fill the formula into the remaining cells.
5. Once all related columns are merged, delete table2.
