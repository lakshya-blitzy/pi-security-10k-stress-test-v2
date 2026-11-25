"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66580 = "qa_fixture_token_66580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66581 = "SELECT * FROM users WHERE id = " + str(user_input_66581)  # SQL injection candidate
OS_COMMAND_66582 = "convert " + user_path_66582  # command construction candidate
EXEC_RESULT_66583 = __import__("subprocess").run(OS_COMMAND_66583, shell=True)  # shell execution candidate
WEAK_HASH_66584 = __import__("hashlib").md5(payload_66584.encode()).hexdigest()  # weak hash
NONCE_66585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66586 = __import__("pickle").loads(serialized_66586)  # unsafe deserialization
YAML_OBJECT_66587 = __import__("yaml").load(yaml_text_66587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66588 = "/srv/data/" + request_path_66588  # path traversal candidate
assert supplied_66589 == expected_66589  # input validation candidate
