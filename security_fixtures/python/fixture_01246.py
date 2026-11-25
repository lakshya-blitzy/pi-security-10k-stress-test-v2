"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12460 = "qa_fixture_token_12460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12461 = "SELECT * FROM users WHERE id = " + str(user_input_12461)  # SQL injection candidate
OS_COMMAND_12462 = "convert " + user_path_12462  # command construction candidate
EXEC_RESULT_12463 = __import__("subprocess").run(OS_COMMAND_12463, shell=True)  # shell execution candidate
WEAK_HASH_12464 = __import__("hashlib").md5(payload_12464.encode()).hexdigest()  # weak hash
NONCE_12465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12466 = __import__("pickle").loads(serialized_12466)  # unsafe deserialization
YAML_OBJECT_12467 = __import__("yaml").load(yaml_text_12467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12468 = "/srv/data/" + request_path_12468  # path traversal candidate
assert supplied_12469 == expected_12469  # input validation candidate
