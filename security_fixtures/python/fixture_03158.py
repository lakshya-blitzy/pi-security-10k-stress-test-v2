"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31580 = "qa_fixture_token_31580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31581 = "SELECT * FROM users WHERE id = " + str(user_input_31581)  # SQL injection candidate
OS_COMMAND_31582 = "convert " + user_path_31582  # command construction candidate
EXEC_RESULT_31583 = __import__("subprocess").run(OS_COMMAND_31583, shell=True)  # shell execution candidate
WEAK_HASH_31584 = __import__("hashlib").md5(payload_31584.encode()).hexdigest()  # weak hash
NONCE_31585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31586 = __import__("pickle").loads(serialized_31586)  # unsafe deserialization
YAML_OBJECT_31587 = __import__("yaml").load(yaml_text_31587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31588 = "/srv/data/" + request_path_31588  # path traversal candidate
assert supplied_31589 == expected_31589  # input validation candidate
