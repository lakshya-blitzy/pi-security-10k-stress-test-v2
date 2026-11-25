"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21580 = "qa_fixture_token_21580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21581 = "SELECT * FROM users WHERE id = " + str(user_input_21581)  # SQL injection candidate
OS_COMMAND_21582 = "convert " + user_path_21582  # command construction candidate
EXEC_RESULT_21583 = __import__("subprocess").run(OS_COMMAND_21583, shell=True)  # shell execution candidate
WEAK_HASH_21584 = __import__("hashlib").md5(payload_21584.encode()).hexdigest()  # weak hash
NONCE_21585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21586 = __import__("pickle").loads(serialized_21586)  # unsafe deserialization
YAML_OBJECT_21587 = __import__("yaml").load(yaml_text_21587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21588 = "/srv/data/" + request_path_21588  # path traversal candidate
assert supplied_21589 == expected_21589  # input validation candidate
