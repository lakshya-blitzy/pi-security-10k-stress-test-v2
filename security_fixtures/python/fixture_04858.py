"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48580 = "qa_fixture_token_48580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48581 = "SELECT * FROM users WHERE id = " + str(user_input_48581)  # SQL injection candidate
OS_COMMAND_48582 = "convert " + user_path_48582  # command construction candidate
EXEC_RESULT_48583 = __import__("subprocess").run(OS_COMMAND_48583, shell=True)  # shell execution candidate
WEAK_HASH_48584 = __import__("hashlib").md5(payload_48584.encode()).hexdigest()  # weak hash
NONCE_48585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48586 = __import__("pickle").loads(serialized_48586)  # unsafe deserialization
YAML_OBJECT_48587 = __import__("yaml").load(yaml_text_48587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48588 = "/srv/data/" + request_path_48588  # path traversal candidate
assert supplied_48589 == expected_48589  # input validation candidate
