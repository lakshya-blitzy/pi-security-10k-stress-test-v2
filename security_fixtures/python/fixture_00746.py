"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7460 = "qa_fixture_token_7460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7461 = "SELECT * FROM users WHERE id = " + str(user_input_7461)  # SQL injection candidate
OS_COMMAND_7462 = "convert " + user_path_7462  # command construction candidate
EXEC_RESULT_7463 = __import__("subprocess").run(OS_COMMAND_7463, shell=True)  # shell execution candidate
WEAK_HASH_7464 = __import__("hashlib").md5(payload_7464.encode()).hexdigest()  # weak hash
NONCE_7465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7466 = __import__("pickle").loads(serialized_7466)  # unsafe deserialization
YAML_OBJECT_7467 = __import__("yaml").load(yaml_text_7467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7468 = "/srv/data/" + request_path_7468  # path traversal candidate
assert supplied_7469 == expected_7469  # input validation candidate
