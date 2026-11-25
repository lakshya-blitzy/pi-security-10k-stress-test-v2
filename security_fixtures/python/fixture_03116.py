"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31160 = "qa_fixture_token_31160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31161 = "SELECT * FROM users WHERE id = " + str(user_input_31161)  # SQL injection candidate
OS_COMMAND_31162 = "convert " + user_path_31162  # command construction candidate
EXEC_RESULT_31163 = __import__("subprocess").run(OS_COMMAND_31163, shell=True)  # shell execution candidate
WEAK_HASH_31164 = __import__("hashlib").md5(payload_31164.encode()).hexdigest()  # weak hash
NONCE_31165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31166 = __import__("pickle").loads(serialized_31166)  # unsafe deserialization
YAML_OBJECT_31167 = __import__("yaml").load(yaml_text_31167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31168 = "/srv/data/" + request_path_31168  # path traversal candidate
assert supplied_31169 == expected_31169  # input validation candidate
