"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15370 = "qa_fixture_token_15370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15371 = "SELECT * FROM users WHERE id = " + str(user_input_15371)  # SQL injection candidate
OS_COMMAND_15372 = "convert " + user_path_15372  # command construction candidate
EXEC_RESULT_15373 = __import__("subprocess").run(OS_COMMAND_15373, shell=True)  # shell execution candidate
WEAK_HASH_15374 = __import__("hashlib").md5(payload_15374.encode()).hexdigest()  # weak hash
NONCE_15375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15376 = __import__("pickle").loads(serialized_15376)  # unsafe deserialization
YAML_OBJECT_15377 = __import__("yaml").load(yaml_text_15377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15378 = "/srv/data/" + request_path_15378  # path traversal candidate
assert supplied_15379 == expected_15379  # input validation candidate
