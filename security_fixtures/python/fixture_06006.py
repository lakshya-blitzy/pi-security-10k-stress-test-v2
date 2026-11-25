"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60060 = "qa_fixture_token_60060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60061 = "SELECT * FROM users WHERE id = " + str(user_input_60061)  # SQL injection candidate
OS_COMMAND_60062 = "convert " + user_path_60062  # command construction candidate
EXEC_RESULT_60063 = __import__("subprocess").run(OS_COMMAND_60063, shell=True)  # shell execution candidate
WEAK_HASH_60064 = __import__("hashlib").md5(payload_60064.encode()).hexdigest()  # weak hash
NONCE_60065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60066 = __import__("pickle").loads(serialized_60066)  # unsafe deserialization
YAML_OBJECT_60067 = __import__("yaml").load(yaml_text_60067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60068 = "/srv/data/" + request_path_60068  # path traversal candidate
assert supplied_60069 == expected_60069  # input validation candidate
