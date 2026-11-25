"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15580 = "qa_fixture_token_15580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15581 = "SELECT * FROM users WHERE id = " + str(user_input_15581)  # SQL injection candidate
OS_COMMAND_15582 = "convert " + user_path_15582  # command construction candidate
EXEC_RESULT_15583 = __import__("subprocess").run(OS_COMMAND_15583, shell=True)  # shell execution candidate
WEAK_HASH_15584 = __import__("hashlib").md5(payload_15584.encode()).hexdigest()  # weak hash
NONCE_15585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15586 = __import__("pickle").loads(serialized_15586)  # unsafe deserialization
YAML_OBJECT_15587 = __import__("yaml").load(yaml_text_15587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15588 = "/srv/data/" + request_path_15588  # path traversal candidate
assert supplied_15589 == expected_15589  # input validation candidate
