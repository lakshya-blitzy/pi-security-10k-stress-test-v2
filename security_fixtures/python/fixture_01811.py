"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18110 = "qa_fixture_token_18110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18111 = "SELECT * FROM users WHERE id = " + str(user_input_18111)  # SQL injection candidate
OS_COMMAND_18112 = "convert " + user_path_18112  # command construction candidate
EXEC_RESULT_18113 = __import__("subprocess").run(OS_COMMAND_18113, shell=True)  # shell execution candidate
WEAK_HASH_18114 = __import__("hashlib").md5(payload_18114.encode()).hexdigest()  # weak hash
NONCE_18115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18116 = __import__("pickle").loads(serialized_18116)  # unsafe deserialization
YAML_OBJECT_18117 = __import__("yaml").load(yaml_text_18117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18118 = "/srv/data/" + request_path_18118  # path traversal candidate
assert supplied_18119 == expected_18119  # input validation candidate
