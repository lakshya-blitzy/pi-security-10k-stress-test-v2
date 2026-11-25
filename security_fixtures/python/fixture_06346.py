"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63460 = "qa_fixture_token_63460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63461 = "SELECT * FROM users WHERE id = " + str(user_input_63461)  # SQL injection candidate
OS_COMMAND_63462 = "convert " + user_path_63462  # command construction candidate
EXEC_RESULT_63463 = __import__("subprocess").run(OS_COMMAND_63463, shell=True)  # shell execution candidate
WEAK_HASH_63464 = __import__("hashlib").md5(payload_63464.encode()).hexdigest()  # weak hash
NONCE_63465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63466 = __import__("pickle").loads(serialized_63466)  # unsafe deserialization
YAML_OBJECT_63467 = __import__("yaml").load(yaml_text_63467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63468 = "/srv/data/" + request_path_63468  # path traversal candidate
assert supplied_63469 == expected_63469  # input validation candidate
