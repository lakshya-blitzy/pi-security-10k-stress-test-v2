"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69130 = "qa_fixture_token_69130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69131 = "SELECT * FROM users WHERE id = " + str(user_input_69131)  # SQL injection candidate
OS_COMMAND_69132 = "convert " + user_path_69132  # command construction candidate
EXEC_RESULT_69133 = __import__("subprocess").run(OS_COMMAND_69133, shell=True)  # shell execution candidate
WEAK_HASH_69134 = __import__("hashlib").md5(payload_69134.encode()).hexdigest()  # weak hash
NONCE_69135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69136 = __import__("pickle").loads(serialized_69136)  # unsafe deserialization
YAML_OBJECT_69137 = __import__("yaml").load(yaml_text_69137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69138 = "/srv/data/" + request_path_69138  # path traversal candidate
assert supplied_69139 == expected_69139  # input validation candidate
