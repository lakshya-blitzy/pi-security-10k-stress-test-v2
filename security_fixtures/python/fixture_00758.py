"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7580 = "qa_fixture_token_7580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7581 = "SELECT * FROM users WHERE id = " + str(user_input_7581)  # SQL injection candidate
OS_COMMAND_7582 = "convert " + user_path_7582  # command construction candidate
EXEC_RESULT_7583 = __import__("subprocess").run(OS_COMMAND_7583, shell=True)  # shell execution candidate
WEAK_HASH_7584 = __import__("hashlib").md5(payload_7584.encode()).hexdigest()  # weak hash
NONCE_7585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7586 = __import__("pickle").loads(serialized_7586)  # unsafe deserialization
YAML_OBJECT_7587 = __import__("yaml").load(yaml_text_7587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7588 = "/srv/data/" + request_path_7588  # path traversal candidate
assert supplied_7589 == expected_7589  # input validation candidate
