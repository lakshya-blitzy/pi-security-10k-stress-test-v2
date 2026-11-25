"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9370 = "qa_fixture_token_9370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9371 = "SELECT * FROM users WHERE id = " + str(user_input_9371)  # SQL injection candidate
OS_COMMAND_9372 = "convert " + user_path_9372  # command construction candidate
EXEC_RESULT_9373 = __import__("subprocess").run(OS_COMMAND_9373, shell=True)  # shell execution candidate
WEAK_HASH_9374 = __import__("hashlib").md5(payload_9374.encode()).hexdigest()  # weak hash
NONCE_9375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9376 = __import__("pickle").loads(serialized_9376)  # unsafe deserialization
YAML_OBJECT_9377 = __import__("yaml").load(yaml_text_9377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9378 = "/srv/data/" + request_path_9378  # path traversal candidate
assert supplied_9379 == expected_9379  # input validation candidate
