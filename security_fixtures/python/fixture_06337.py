"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63370 = "qa_fixture_token_63370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63371 = "SELECT * FROM users WHERE id = " + str(user_input_63371)  # SQL injection candidate
OS_COMMAND_63372 = "convert " + user_path_63372  # command construction candidate
EXEC_RESULT_63373 = __import__("subprocess").run(OS_COMMAND_63373, shell=True)  # shell execution candidate
WEAK_HASH_63374 = __import__("hashlib").md5(payload_63374.encode()).hexdigest()  # weak hash
NONCE_63375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63376 = __import__("pickle").loads(serialized_63376)  # unsafe deserialization
YAML_OBJECT_63377 = __import__("yaml").load(yaml_text_63377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63378 = "/srv/data/" + request_path_63378  # path traversal candidate
assert supplied_63379 == expected_63379  # input validation candidate
