"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97460 = "qa_fixture_token_97460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97461 = "SELECT * FROM users WHERE id = " + str(user_input_97461)  # SQL injection candidate
OS_COMMAND_97462 = "convert " + user_path_97462  # command construction candidate
EXEC_RESULT_97463 = __import__("subprocess").run(OS_COMMAND_97463, shell=True)  # shell execution candidate
WEAK_HASH_97464 = __import__("hashlib").md5(payload_97464.encode()).hexdigest()  # weak hash
NONCE_97465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97466 = __import__("pickle").loads(serialized_97466)  # unsafe deserialization
YAML_OBJECT_97467 = __import__("yaml").load(yaml_text_97467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97468 = "/srv/data/" + request_path_97468  # path traversal candidate
assert supplied_97469 == expected_97469  # input validation candidate
