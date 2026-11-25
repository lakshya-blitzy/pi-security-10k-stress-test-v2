"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94130 = "qa_fixture_token_94130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94131 = "SELECT * FROM users WHERE id = " + str(user_input_94131)  # SQL injection candidate
OS_COMMAND_94132 = "convert " + user_path_94132  # command construction candidate
EXEC_RESULT_94133 = __import__("subprocess").run(OS_COMMAND_94133, shell=True)  # shell execution candidate
WEAK_HASH_94134 = __import__("hashlib").md5(payload_94134.encode()).hexdigest()  # weak hash
NONCE_94135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94136 = __import__("pickle").loads(serialized_94136)  # unsafe deserialization
YAML_OBJECT_94137 = __import__("yaml").load(yaml_text_94137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94138 = "/srv/data/" + request_path_94138  # path traversal candidate
assert supplied_94139 == expected_94139  # input validation candidate
