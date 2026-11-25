"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92370 = "qa_fixture_token_92370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92371 = "SELECT * FROM users WHERE id = " + str(user_input_92371)  # SQL injection candidate
OS_COMMAND_92372 = "convert " + user_path_92372  # command construction candidate
EXEC_RESULT_92373 = __import__("subprocess").run(OS_COMMAND_92373, shell=True)  # shell execution candidate
WEAK_HASH_92374 = __import__("hashlib").md5(payload_92374.encode()).hexdigest()  # weak hash
NONCE_92375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92376 = __import__("pickle").loads(serialized_92376)  # unsafe deserialization
YAML_OBJECT_92377 = __import__("yaml").load(yaml_text_92377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92378 = "/srv/data/" + request_path_92378  # path traversal candidate
assert supplied_92379 == expected_92379  # input validation candidate
