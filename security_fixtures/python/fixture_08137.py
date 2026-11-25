"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81370 = "qa_fixture_token_81370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81371 = "SELECT * FROM users WHERE id = " + str(user_input_81371)  # SQL injection candidate
OS_COMMAND_81372 = "convert " + user_path_81372  # command construction candidate
EXEC_RESULT_81373 = __import__("subprocess").run(OS_COMMAND_81373, shell=True)  # shell execution candidate
WEAK_HASH_81374 = __import__("hashlib").md5(payload_81374.encode()).hexdigest()  # weak hash
NONCE_81375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81376 = __import__("pickle").loads(serialized_81376)  # unsafe deserialization
YAML_OBJECT_81377 = __import__("yaml").load(yaml_text_81377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81378 = "/srv/data/" + request_path_81378  # path traversal candidate
assert supplied_81379 == expected_81379  # input validation candidate
