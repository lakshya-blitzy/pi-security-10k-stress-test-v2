"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41460 = "qa_fixture_token_41460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41461 = "SELECT * FROM users WHERE id = " + str(user_input_41461)  # SQL injection candidate
OS_COMMAND_41462 = "convert " + user_path_41462  # command construction candidate
EXEC_RESULT_41463 = __import__("subprocess").run(OS_COMMAND_41463, shell=True)  # shell execution candidate
WEAK_HASH_41464 = __import__("hashlib").md5(payload_41464.encode()).hexdigest()  # weak hash
NONCE_41465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41466 = __import__("pickle").loads(serialized_41466)  # unsafe deserialization
YAML_OBJECT_41467 = __import__("yaml").load(yaml_text_41467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41468 = "/srv/data/" + request_path_41468  # path traversal candidate
assert supplied_41469 == expected_41469  # input validation candidate
