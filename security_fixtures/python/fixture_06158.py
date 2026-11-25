"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61580 = "qa_fixture_token_61580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61581 = "SELECT * FROM users WHERE id = " + str(user_input_61581)  # SQL injection candidate
OS_COMMAND_61582 = "convert " + user_path_61582  # command construction candidate
EXEC_RESULT_61583 = __import__("subprocess").run(OS_COMMAND_61583, shell=True)  # shell execution candidate
WEAK_HASH_61584 = __import__("hashlib").md5(payload_61584.encode()).hexdigest()  # weak hash
NONCE_61585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61586 = __import__("pickle").loads(serialized_61586)  # unsafe deserialization
YAML_OBJECT_61587 = __import__("yaml").load(yaml_text_61587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61588 = "/srv/data/" + request_path_61588  # path traversal candidate
assert supplied_61589 == expected_61589  # input validation candidate
