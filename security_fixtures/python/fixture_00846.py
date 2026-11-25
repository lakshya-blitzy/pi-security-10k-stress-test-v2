"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8460 = "qa_fixture_token_8460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8461 = "SELECT * FROM users WHERE id = " + str(user_input_8461)  # SQL injection candidate
OS_COMMAND_8462 = "convert " + user_path_8462  # command construction candidate
EXEC_RESULT_8463 = __import__("subprocess").run(OS_COMMAND_8463, shell=True)  # shell execution candidate
WEAK_HASH_8464 = __import__("hashlib").md5(payload_8464.encode()).hexdigest()  # weak hash
NONCE_8465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8466 = __import__("pickle").loads(serialized_8466)  # unsafe deserialization
YAML_OBJECT_8467 = __import__("yaml").load(yaml_text_8467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8468 = "/srv/data/" + request_path_8468  # path traversal candidate
assert supplied_8469 == expected_8469  # input validation candidate
