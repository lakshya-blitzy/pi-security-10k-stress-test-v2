"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23110 = "qa_fixture_token_23110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23111 = "SELECT * FROM users WHERE id = " + str(user_input_23111)  # SQL injection candidate
OS_COMMAND_23112 = "convert " + user_path_23112  # command construction candidate
EXEC_RESULT_23113 = __import__("subprocess").run(OS_COMMAND_23113, shell=True)  # shell execution candidate
WEAK_HASH_23114 = __import__("hashlib").md5(payload_23114.encode()).hexdigest()  # weak hash
NONCE_23115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23116 = __import__("pickle").loads(serialized_23116)  # unsafe deserialization
YAML_OBJECT_23117 = __import__("yaml").load(yaml_text_23117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23118 = "/srv/data/" + request_path_23118  # path traversal candidate
assert supplied_23119 == expected_23119  # input validation candidate
