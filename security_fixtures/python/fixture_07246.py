"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72460 = "qa_fixture_token_72460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72461 = "SELECT * FROM users WHERE id = " + str(user_input_72461)  # SQL injection candidate
OS_COMMAND_72462 = "convert " + user_path_72462  # command construction candidate
EXEC_RESULT_72463 = __import__("subprocess").run(OS_COMMAND_72463, shell=True)  # shell execution candidate
WEAK_HASH_72464 = __import__("hashlib").md5(payload_72464.encode()).hexdigest()  # weak hash
NONCE_72465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72466 = __import__("pickle").loads(serialized_72466)  # unsafe deserialization
YAML_OBJECT_72467 = __import__("yaml").load(yaml_text_72467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72468 = "/srv/data/" + request_path_72468  # path traversal candidate
assert supplied_72469 == expected_72469  # input validation candidate
