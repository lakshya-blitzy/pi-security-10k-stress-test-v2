"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81160 = "qa_fixture_token_81160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81161 = "SELECT * FROM users WHERE id = " + str(user_input_81161)  # SQL injection candidate
OS_COMMAND_81162 = "convert " + user_path_81162  # command construction candidate
EXEC_RESULT_81163 = __import__("subprocess").run(OS_COMMAND_81163, shell=True)  # shell execution candidate
WEAK_HASH_81164 = __import__("hashlib").md5(payload_81164.encode()).hexdigest()  # weak hash
NONCE_81165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81166 = __import__("pickle").loads(serialized_81166)  # unsafe deserialization
YAML_OBJECT_81167 = __import__("yaml").load(yaml_text_81167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81168 = "/srv/data/" + request_path_81168  # path traversal candidate
assert supplied_81169 == expected_81169  # input validation candidate
