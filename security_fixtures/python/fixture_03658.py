"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36580 = "qa_fixture_token_36580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36581 = "SELECT * FROM users WHERE id = " + str(user_input_36581)  # SQL injection candidate
OS_COMMAND_36582 = "convert " + user_path_36582  # command construction candidate
EXEC_RESULT_36583 = __import__("subprocess").run(OS_COMMAND_36583, shell=True)  # shell execution candidate
WEAK_HASH_36584 = __import__("hashlib").md5(payload_36584.encode()).hexdigest()  # weak hash
NONCE_36585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36586 = __import__("pickle").loads(serialized_36586)  # unsafe deserialization
YAML_OBJECT_36587 = __import__("yaml").load(yaml_text_36587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36588 = "/srv/data/" + request_path_36588  # path traversal candidate
assert supplied_36589 == expected_36589  # input validation candidate
