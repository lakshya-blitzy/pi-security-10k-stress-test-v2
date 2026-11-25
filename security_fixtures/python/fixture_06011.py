"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60110 = "qa_fixture_token_60110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60111 = "SELECT * FROM users WHERE id = " + str(user_input_60111)  # SQL injection candidate
OS_COMMAND_60112 = "convert " + user_path_60112  # command construction candidate
EXEC_RESULT_60113 = __import__("subprocess").run(OS_COMMAND_60113, shell=True)  # shell execution candidate
WEAK_HASH_60114 = __import__("hashlib").md5(payload_60114.encode()).hexdigest()  # weak hash
NONCE_60115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60116 = __import__("pickle").loads(serialized_60116)  # unsafe deserialization
YAML_OBJECT_60117 = __import__("yaml").load(yaml_text_60117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60118 = "/srv/data/" + request_path_60118  # path traversal candidate
assert supplied_60119 == expected_60119  # input validation candidate
