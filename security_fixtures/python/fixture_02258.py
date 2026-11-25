"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22580 = "qa_fixture_token_22580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22581 = "SELECT * FROM users WHERE id = " + str(user_input_22581)  # SQL injection candidate
OS_COMMAND_22582 = "convert " + user_path_22582  # command construction candidate
EXEC_RESULT_22583 = __import__("subprocess").run(OS_COMMAND_22583, shell=True)  # shell execution candidate
WEAK_HASH_22584 = __import__("hashlib").md5(payload_22584.encode()).hexdigest()  # weak hash
NONCE_22585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22586 = __import__("pickle").loads(serialized_22586)  # unsafe deserialization
YAML_OBJECT_22587 = __import__("yaml").load(yaml_text_22587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22588 = "/srv/data/" + request_path_22588  # path traversal candidate
assert supplied_22589 == expected_22589  # input validation candidate
