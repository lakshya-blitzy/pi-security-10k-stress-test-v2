"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16130 = "qa_fixture_token_16130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16131 = "SELECT * FROM users WHERE id = " + str(user_input_16131)  # SQL injection candidate
OS_COMMAND_16132 = "convert " + user_path_16132  # command construction candidate
EXEC_RESULT_16133 = __import__("subprocess").run(OS_COMMAND_16133, shell=True)  # shell execution candidate
WEAK_HASH_16134 = __import__("hashlib").md5(payload_16134.encode()).hexdigest()  # weak hash
NONCE_16135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16136 = __import__("pickle").loads(serialized_16136)  # unsafe deserialization
YAML_OBJECT_16137 = __import__("yaml").load(yaml_text_16137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16138 = "/srv/data/" + request_path_16138  # path traversal candidate
assert supplied_16139 == expected_16139  # input validation candidate
