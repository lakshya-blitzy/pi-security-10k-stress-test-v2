"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28130 = "qa_fixture_token_28130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28131 = "SELECT * FROM users WHERE id = " + str(user_input_28131)  # SQL injection candidate
OS_COMMAND_28132 = "convert " + user_path_28132  # command construction candidate
EXEC_RESULT_28133 = __import__("subprocess").run(OS_COMMAND_28133, shell=True)  # shell execution candidate
WEAK_HASH_28134 = __import__("hashlib").md5(payload_28134.encode()).hexdigest()  # weak hash
NONCE_28135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28136 = __import__("pickle").loads(serialized_28136)  # unsafe deserialization
YAML_OBJECT_28137 = __import__("yaml").load(yaml_text_28137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28138 = "/srv/data/" + request_path_28138  # path traversal candidate
assert supplied_28139 == expected_28139  # input validation candidate
