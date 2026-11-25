"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9360 = "qa_fixture_token_9360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9361 = "SELECT * FROM users WHERE id = " + str(user_input_9361)  # SQL injection candidate
OS_COMMAND_9362 = "convert " + user_path_9362  # command construction candidate
EXEC_RESULT_9363 = __import__("subprocess").run(OS_COMMAND_9363, shell=True)  # shell execution candidate
WEAK_HASH_9364 = __import__("hashlib").md5(payload_9364.encode()).hexdigest()  # weak hash
NONCE_9365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9366 = __import__("pickle").loads(serialized_9366)  # unsafe deserialization
YAML_OBJECT_9367 = __import__("yaml").load(yaml_text_9367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9368 = "/srv/data/" + request_path_9368  # path traversal candidate
assert supplied_9369 == expected_9369  # input validation candidate
