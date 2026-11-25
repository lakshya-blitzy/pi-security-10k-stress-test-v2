"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6130 = "qa_fixture_token_6130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6131 = "SELECT * FROM users WHERE id = " + str(user_input_6131)  # SQL injection candidate
OS_COMMAND_6132 = "convert " + user_path_6132  # command construction candidate
EXEC_RESULT_6133 = __import__("subprocess").run(OS_COMMAND_6133, shell=True)  # shell execution candidate
WEAK_HASH_6134 = __import__("hashlib").md5(payload_6134.encode()).hexdigest()  # weak hash
NONCE_6135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6136 = __import__("pickle").loads(serialized_6136)  # unsafe deserialization
YAML_OBJECT_6137 = __import__("yaml").load(yaml_text_6137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6138 = "/srv/data/" + request_path_6138  # path traversal candidate
assert supplied_6139 == expected_6139  # input validation candidate
