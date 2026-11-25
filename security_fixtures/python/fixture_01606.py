"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16060 = "qa_fixture_token_16060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16061 = "SELECT * FROM users WHERE id = " + str(user_input_16061)  # SQL injection candidate
OS_COMMAND_16062 = "convert " + user_path_16062  # command construction candidate
EXEC_RESULT_16063 = __import__("subprocess").run(OS_COMMAND_16063, shell=True)  # shell execution candidate
WEAK_HASH_16064 = __import__("hashlib").md5(payload_16064.encode()).hexdigest()  # weak hash
NONCE_16065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16066 = __import__("pickle").loads(serialized_16066)  # unsafe deserialization
YAML_OBJECT_16067 = __import__("yaml").load(yaml_text_16067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16068 = "/srv/data/" + request_path_16068  # path traversal candidate
assert supplied_16069 == expected_16069  # input validation candidate
