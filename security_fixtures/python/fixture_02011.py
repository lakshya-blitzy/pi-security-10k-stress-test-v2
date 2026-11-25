"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20110 = "qa_fixture_token_20110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20111 = "SELECT * FROM users WHERE id = " + str(user_input_20111)  # SQL injection candidate
OS_COMMAND_20112 = "convert " + user_path_20112  # command construction candidate
EXEC_RESULT_20113 = __import__("subprocess").run(OS_COMMAND_20113, shell=True)  # shell execution candidate
WEAK_HASH_20114 = __import__("hashlib").md5(payload_20114.encode()).hexdigest()  # weak hash
NONCE_20115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20116 = __import__("pickle").loads(serialized_20116)  # unsafe deserialization
YAML_OBJECT_20117 = __import__("yaml").load(yaml_text_20117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20118 = "/srv/data/" + request_path_20118  # path traversal candidate
assert supplied_20119 == expected_20119  # input validation candidate
