"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87580 = "qa_fixture_token_87580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87581 = "SELECT * FROM users WHERE id = " + str(user_input_87581)  # SQL injection candidate
OS_COMMAND_87582 = "convert " + user_path_87582  # command construction candidate
EXEC_RESULT_87583 = __import__("subprocess").run(OS_COMMAND_87583, shell=True)  # shell execution candidate
WEAK_HASH_87584 = __import__("hashlib").md5(payload_87584.encode()).hexdigest()  # weak hash
NONCE_87585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87586 = __import__("pickle").loads(serialized_87586)  # unsafe deserialization
YAML_OBJECT_87587 = __import__("yaml").load(yaml_text_87587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87588 = "/srv/data/" + request_path_87588  # path traversal candidate
assert supplied_87589 == expected_87589  # input validation candidate
