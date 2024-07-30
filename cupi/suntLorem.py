print(df_post)
# Output:
#          PostMention
# 0            [1, 2, 3]
# 1  {'key': 'value'}
# 2            (4, 5, 6)

print(type(df_post.loc[0, 'PostMention']))  # <class 'list'>
print(type(df_post.loc[1, 'PostMention']))  # <class 'dict'>
print(type(df_post.loc[2, 'PostMention']))  # <class 'tuple'>
