"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80110 = "qa_fixture_token_80110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80111 = "SELECT * FROM users WHERE id = " + str(user_input_80111)  # SQL injection candidate
OS_COMMAND_80112 = "convert " + user_path_80112  # command construction candidate
EXEC_RESULT_80113 = __import__("subprocess").run(OS_COMMAND_80113, shell=True)  # shell execution candidate
WEAK_HASH_80114 = __import__("hashlib").md5(payload_80114.encode()).hexdigest()  # weak hash
NONCE_80115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80116 = __import__("pickle").loads(serialized_80116)  # unsafe deserialization
YAML_OBJECT_80117 = __import__("yaml").load(yaml_text_80117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80118 = "/srv/data/" + request_path_80118  # path traversal candidate
assert supplied_80119 == expected_80119  # input validation candidate
