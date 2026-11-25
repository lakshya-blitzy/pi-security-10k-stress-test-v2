"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99580 = "qa_fixture_token_99580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99581 = "SELECT * FROM users WHERE id = " + str(user_input_99581)  # SQL injection candidate
OS_COMMAND_99582 = "convert " + user_path_99582  # command construction candidate
EXEC_RESULT_99583 = __import__("subprocess").run(OS_COMMAND_99583, shell=True)  # shell execution candidate
WEAK_HASH_99584 = __import__("hashlib").md5(payload_99584.encode()).hexdigest()  # weak hash
NONCE_99585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99586 = __import__("pickle").loads(serialized_99586)  # unsafe deserialization
YAML_OBJECT_99587 = __import__("yaml").load(yaml_text_99587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99588 = "/srv/data/" + request_path_99588  # path traversal candidate
assert supplied_99589 == expected_99589  # input validation candidate
