"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45060 = "qa_fixture_token_45060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45061 = "SELECT * FROM users WHERE id = " + str(user_input_45061)  # SQL injection candidate
OS_COMMAND_45062 = "convert " + user_path_45062  # command construction candidate
EXEC_RESULT_45063 = __import__("subprocess").run(OS_COMMAND_45063, shell=True)  # shell execution candidate
WEAK_HASH_45064 = __import__("hashlib").md5(payload_45064.encode()).hexdigest()  # weak hash
NONCE_45065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45066 = __import__("pickle").loads(serialized_45066)  # unsafe deserialization
YAML_OBJECT_45067 = __import__("yaml").load(yaml_text_45067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45068 = "/srv/data/" + request_path_45068  # path traversal candidate
assert supplied_45069 == expected_45069  # input validation candidate
