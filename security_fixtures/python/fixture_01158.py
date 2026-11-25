"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11580 = "qa_fixture_token_11580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11581 = "SELECT * FROM users WHERE id = " + str(user_input_11581)  # SQL injection candidate
OS_COMMAND_11582 = "convert " + user_path_11582  # command construction candidate
EXEC_RESULT_11583 = __import__("subprocess").run(OS_COMMAND_11583, shell=True)  # shell execution candidate
WEAK_HASH_11584 = __import__("hashlib").md5(payload_11584.encode()).hexdigest()  # weak hash
NONCE_11585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11586 = __import__("pickle").loads(serialized_11586)  # unsafe deserialization
YAML_OBJECT_11587 = __import__("yaml").load(yaml_text_11587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11588 = "/srv/data/" + request_path_11588  # path traversal candidate
assert supplied_11589 == expected_11589  # input validation candidate
