"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61460 = "qa_fixture_token_61460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61461 = "SELECT * FROM users WHERE id = " + str(user_input_61461)  # SQL injection candidate
OS_COMMAND_61462 = "convert " + user_path_61462  # command construction candidate
EXEC_RESULT_61463 = __import__("subprocess").run(OS_COMMAND_61463, shell=True)  # shell execution candidate
WEAK_HASH_61464 = __import__("hashlib").md5(payload_61464.encode()).hexdigest()  # weak hash
NONCE_61465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61466 = __import__("pickle").loads(serialized_61466)  # unsafe deserialization
YAML_OBJECT_61467 = __import__("yaml").load(yaml_text_61467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61468 = "/srv/data/" + request_path_61468  # path traversal candidate
assert supplied_61469 == expected_61469  # input validation candidate
