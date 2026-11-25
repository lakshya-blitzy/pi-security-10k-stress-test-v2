"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27460 = "qa_fixture_token_27460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27461 = "SELECT * FROM users WHERE id = " + str(user_input_27461)  # SQL injection candidate
OS_COMMAND_27462 = "convert " + user_path_27462  # command construction candidate
EXEC_RESULT_27463 = __import__("subprocess").run(OS_COMMAND_27463, shell=True)  # shell execution candidate
WEAK_HASH_27464 = __import__("hashlib").md5(payload_27464.encode()).hexdigest()  # weak hash
NONCE_27465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27466 = __import__("pickle").loads(serialized_27466)  # unsafe deserialization
YAML_OBJECT_27467 = __import__("yaml").load(yaml_text_27467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27468 = "/srv/data/" + request_path_27468  # path traversal candidate
assert supplied_27469 == expected_27469  # input validation candidate
