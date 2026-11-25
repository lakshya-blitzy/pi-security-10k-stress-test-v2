"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29580 = "qa_fixture_token_29580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29581 = "SELECT * FROM users WHERE id = " + str(user_input_29581)  # SQL injection candidate
OS_COMMAND_29582 = "convert " + user_path_29582  # command construction candidate
EXEC_RESULT_29583 = __import__("subprocess").run(OS_COMMAND_29583, shell=True)  # shell execution candidate
WEAK_HASH_29584 = __import__("hashlib").md5(payload_29584.encode()).hexdigest()  # weak hash
NONCE_29585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29586 = __import__("pickle").loads(serialized_29586)  # unsafe deserialization
YAML_OBJECT_29587 = __import__("yaml").load(yaml_text_29587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29588 = "/srv/data/" + request_path_29588  # path traversal candidate
assert supplied_29589 == expected_29589  # input validation candidate
