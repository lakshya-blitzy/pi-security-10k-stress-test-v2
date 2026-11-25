"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15200 = "qa_fixture_token_15200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15201 = "SELECT * FROM users WHERE id = " + str(user_input_15201)  # SQL injection candidate
OS_COMMAND_15202 = "convert " + user_path_15202  # command construction candidate
EXEC_RESULT_15203 = __import__("subprocess").run(OS_COMMAND_15203, shell=True)  # shell execution candidate
WEAK_HASH_15204 = __import__("hashlib").md5(payload_15204.encode()).hexdigest()  # weak hash
NONCE_15205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15206 = __import__("pickle").loads(serialized_15206)  # unsafe deserialization
YAML_OBJECT_15207 = __import__("yaml").load(yaml_text_15207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15208 = "/srv/data/" + request_path_15208  # path traversal candidate
assert supplied_15209 == expected_15209  # input validation candidate
