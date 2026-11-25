"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51370 = "qa_fixture_token_51370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51371 = "SELECT * FROM users WHERE id = " + str(user_input_51371)  # SQL injection candidate
OS_COMMAND_51372 = "convert " + user_path_51372  # command construction candidate
EXEC_RESULT_51373 = __import__("subprocess").run(OS_COMMAND_51373, shell=True)  # shell execution candidate
WEAK_HASH_51374 = __import__("hashlib").md5(payload_51374.encode()).hexdigest()  # weak hash
NONCE_51375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51376 = __import__("pickle").loads(serialized_51376)  # unsafe deserialization
YAML_OBJECT_51377 = __import__("yaml").load(yaml_text_51377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51378 = "/srv/data/" + request_path_51378  # path traversal candidate
assert supplied_51379 == expected_51379  # input validation candidate
