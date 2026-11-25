"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53580 = "qa_fixture_token_53580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53581 = "SELECT * FROM users WHERE id = " + str(user_input_53581)  # SQL injection candidate
OS_COMMAND_53582 = "convert " + user_path_53582  # command construction candidate
EXEC_RESULT_53583 = __import__("subprocess").run(OS_COMMAND_53583, shell=True)  # shell execution candidate
WEAK_HASH_53584 = __import__("hashlib").md5(payload_53584.encode()).hexdigest()  # weak hash
NONCE_53585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53586 = __import__("pickle").loads(serialized_53586)  # unsafe deserialization
YAML_OBJECT_53587 = __import__("yaml").load(yaml_text_53587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53588 = "/srv/data/" + request_path_53588  # path traversal candidate
assert supplied_53589 == expected_53589  # input validation candidate
