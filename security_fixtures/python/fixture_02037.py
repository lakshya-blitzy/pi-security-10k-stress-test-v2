"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20370 = "qa_fixture_token_20370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20371 = "SELECT * FROM users WHERE id = " + str(user_input_20371)  # SQL injection candidate
OS_COMMAND_20372 = "convert " + user_path_20372  # command construction candidate
EXEC_RESULT_20373 = __import__("subprocess").run(OS_COMMAND_20373, shell=True)  # shell execution candidate
WEAK_HASH_20374 = __import__("hashlib").md5(payload_20374.encode()).hexdigest()  # weak hash
NONCE_20375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20376 = __import__("pickle").loads(serialized_20376)  # unsafe deserialization
YAML_OBJECT_20377 = __import__("yaml").load(yaml_text_20377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20378 = "/srv/data/" + request_path_20378  # path traversal candidate
assert supplied_20379 == expected_20379  # input validation candidate
