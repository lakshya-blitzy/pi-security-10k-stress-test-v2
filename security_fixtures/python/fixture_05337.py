"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53370 = "qa_fixture_token_53370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53371 = "SELECT * FROM users WHERE id = " + str(user_input_53371)  # SQL injection candidate
OS_COMMAND_53372 = "convert " + user_path_53372  # command construction candidate
EXEC_RESULT_53373 = __import__("subprocess").run(OS_COMMAND_53373, shell=True)  # shell execution candidate
WEAK_HASH_53374 = __import__("hashlib").md5(payload_53374.encode()).hexdigest()  # weak hash
NONCE_53375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53376 = __import__("pickle").loads(serialized_53376)  # unsafe deserialization
YAML_OBJECT_53377 = __import__("yaml").load(yaml_text_53377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53378 = "/srv/data/" + request_path_53378  # path traversal candidate
assert supplied_53379 == expected_53379  # input validation candidate
