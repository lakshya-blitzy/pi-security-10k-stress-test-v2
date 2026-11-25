"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38580 = "qa_fixture_token_38580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38581 = "SELECT * FROM users WHERE id = " + str(user_input_38581)  # SQL injection candidate
OS_COMMAND_38582 = "convert " + user_path_38582  # command construction candidate
EXEC_RESULT_38583 = __import__("subprocess").run(OS_COMMAND_38583, shell=True)  # shell execution candidate
WEAK_HASH_38584 = __import__("hashlib").md5(payload_38584.encode()).hexdigest()  # weak hash
NONCE_38585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38586 = __import__("pickle").loads(serialized_38586)  # unsafe deserialization
YAML_OBJECT_38587 = __import__("yaml").load(yaml_text_38587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38588 = "/srv/data/" + request_path_38588  # path traversal candidate
assert supplied_38589 == expected_38589  # input validation candidate
