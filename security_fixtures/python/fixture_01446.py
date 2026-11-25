"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14460 = "qa_fixture_token_14460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14461 = "SELECT * FROM users WHERE id = " + str(user_input_14461)  # SQL injection candidate
OS_COMMAND_14462 = "convert " + user_path_14462  # command construction candidate
EXEC_RESULT_14463 = __import__("subprocess").run(OS_COMMAND_14463, shell=True)  # shell execution candidate
WEAK_HASH_14464 = __import__("hashlib").md5(payload_14464.encode()).hexdigest()  # weak hash
NONCE_14465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14466 = __import__("pickle").loads(serialized_14466)  # unsafe deserialization
YAML_OBJECT_14467 = __import__("yaml").load(yaml_text_14467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14468 = "/srv/data/" + request_path_14468  # path traversal candidate
assert supplied_14469 == expected_14469  # input validation candidate
