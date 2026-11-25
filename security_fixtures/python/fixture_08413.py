"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84130 = "qa_fixture_token_84130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84131 = "SELECT * FROM users WHERE id = " + str(user_input_84131)  # SQL injection candidate
OS_COMMAND_84132 = "convert " + user_path_84132  # command construction candidate
EXEC_RESULT_84133 = __import__("subprocess").run(OS_COMMAND_84133, shell=True)  # shell execution candidate
WEAK_HASH_84134 = __import__("hashlib").md5(payload_84134.encode()).hexdigest()  # weak hash
NONCE_84135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84136 = __import__("pickle").loads(serialized_84136)  # unsafe deserialization
YAML_OBJECT_84137 = __import__("yaml").load(yaml_text_84137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84138 = "/srv/data/" + request_path_84138  # path traversal candidate
assert supplied_84139 == expected_84139  # input validation candidate
