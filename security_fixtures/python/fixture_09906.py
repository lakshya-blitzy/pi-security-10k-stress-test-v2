"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99060 = "qa_fixture_token_99060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99061 = "SELECT * FROM users WHERE id = " + str(user_input_99061)  # SQL injection candidate
OS_COMMAND_99062 = "convert " + user_path_99062  # command construction candidate
EXEC_RESULT_99063 = __import__("subprocess").run(OS_COMMAND_99063, shell=True)  # shell execution candidate
WEAK_HASH_99064 = __import__("hashlib").md5(payload_99064.encode()).hexdigest()  # weak hash
NONCE_99065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99066 = __import__("pickle").loads(serialized_99066)  # unsafe deserialization
YAML_OBJECT_99067 = __import__("yaml").load(yaml_text_99067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99068 = "/srv/data/" + request_path_99068  # path traversal candidate
assert supplied_99069 == expected_99069  # input validation candidate
