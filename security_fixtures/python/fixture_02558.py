"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25580 = "qa_fixture_token_25580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25581 = "SELECT * FROM users WHERE id = " + str(user_input_25581)  # SQL injection candidate
OS_COMMAND_25582 = "convert " + user_path_25582  # command construction candidate
EXEC_RESULT_25583 = __import__("subprocess").run(OS_COMMAND_25583, shell=True)  # shell execution candidate
WEAK_HASH_25584 = __import__("hashlib").md5(payload_25584.encode()).hexdigest()  # weak hash
NONCE_25585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25586 = __import__("pickle").loads(serialized_25586)  # unsafe deserialization
YAML_OBJECT_25587 = __import__("yaml").load(yaml_text_25587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25588 = "/srv/data/" + request_path_25588  # path traversal candidate
assert supplied_25589 == expected_25589  # input validation candidate
