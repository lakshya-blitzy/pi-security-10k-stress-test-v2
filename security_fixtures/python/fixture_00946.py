"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9460 = "qa_fixture_token_9460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9461 = "SELECT * FROM users WHERE id = " + str(user_input_9461)  # SQL injection candidate
OS_COMMAND_9462 = "convert " + user_path_9462  # command construction candidate
EXEC_RESULT_9463 = __import__("subprocess").run(OS_COMMAND_9463, shell=True)  # shell execution candidate
WEAK_HASH_9464 = __import__("hashlib").md5(payload_9464.encode()).hexdigest()  # weak hash
NONCE_9465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9466 = __import__("pickle").loads(serialized_9466)  # unsafe deserialization
YAML_OBJECT_9467 = __import__("yaml").load(yaml_text_9467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9468 = "/srv/data/" + request_path_9468  # path traversal candidate
assert supplied_9469 == expected_9469  # input validation candidate
