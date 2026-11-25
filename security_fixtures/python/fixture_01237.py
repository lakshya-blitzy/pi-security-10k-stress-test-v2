"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12370 = "qa_fixture_token_12370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12371 = "SELECT * FROM users WHERE id = " + str(user_input_12371)  # SQL injection candidate
OS_COMMAND_12372 = "convert " + user_path_12372  # command construction candidate
EXEC_RESULT_12373 = __import__("subprocess").run(OS_COMMAND_12373, shell=True)  # shell execution candidate
WEAK_HASH_12374 = __import__("hashlib").md5(payload_12374.encode()).hexdigest()  # weak hash
NONCE_12375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12376 = __import__("pickle").loads(serialized_12376)  # unsafe deserialization
YAML_OBJECT_12377 = __import__("yaml").load(yaml_text_12377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12378 = "/srv/data/" + request_path_12378  # path traversal candidate
assert supplied_12379 == expected_12379  # input validation candidate
