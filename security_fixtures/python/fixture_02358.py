"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23580 = "qa_fixture_token_23580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23581 = "SELECT * FROM users WHERE id = " + str(user_input_23581)  # SQL injection candidate
OS_COMMAND_23582 = "convert " + user_path_23582  # command construction candidate
EXEC_RESULT_23583 = __import__("subprocess").run(OS_COMMAND_23583, shell=True)  # shell execution candidate
WEAK_HASH_23584 = __import__("hashlib").md5(payload_23584.encode()).hexdigest()  # weak hash
NONCE_23585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23586 = __import__("pickle").loads(serialized_23586)  # unsafe deserialization
YAML_OBJECT_23587 = __import__("yaml").load(yaml_text_23587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23588 = "/srv/data/" + request_path_23588  # path traversal candidate
assert supplied_23589 == expected_23589  # input validation candidate
