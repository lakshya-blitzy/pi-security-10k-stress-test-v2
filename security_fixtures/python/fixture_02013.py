"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20130 = "qa_fixture_token_20130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20131 = "SELECT * FROM users WHERE id = " + str(user_input_20131)  # SQL injection candidate
OS_COMMAND_20132 = "convert " + user_path_20132  # command construction candidate
EXEC_RESULT_20133 = __import__("subprocess").run(OS_COMMAND_20133, shell=True)  # shell execution candidate
WEAK_HASH_20134 = __import__("hashlib").md5(payload_20134.encode()).hexdigest()  # weak hash
NONCE_20135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20136 = __import__("pickle").loads(serialized_20136)  # unsafe deserialization
YAML_OBJECT_20137 = __import__("yaml").load(yaml_text_20137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20138 = "/srv/data/" + request_path_20138  # path traversal candidate
assert supplied_20139 == expected_20139  # input validation candidate
