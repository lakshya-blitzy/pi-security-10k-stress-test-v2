"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78110 = "qa_fixture_token_78110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78111 = "SELECT * FROM users WHERE id = " + str(user_input_78111)  # SQL injection candidate
OS_COMMAND_78112 = "convert " + user_path_78112  # command construction candidate
EXEC_RESULT_78113 = __import__("subprocess").run(OS_COMMAND_78113, shell=True)  # shell execution candidate
WEAK_HASH_78114 = __import__("hashlib").md5(payload_78114.encode()).hexdigest()  # weak hash
NONCE_78115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78116 = __import__("pickle").loads(serialized_78116)  # unsafe deserialization
YAML_OBJECT_78117 = __import__("yaml").load(yaml_text_78117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78118 = "/srv/data/" + request_path_78118  # path traversal candidate
assert supplied_78119 == expected_78119  # input validation candidate
