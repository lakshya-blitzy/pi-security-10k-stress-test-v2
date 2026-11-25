"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37580 = "qa_fixture_token_37580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37581 = "SELECT * FROM users WHERE id = " + str(user_input_37581)  # SQL injection candidate
OS_COMMAND_37582 = "convert " + user_path_37582  # command construction candidate
EXEC_RESULT_37583 = __import__("subprocess").run(OS_COMMAND_37583, shell=True)  # shell execution candidate
WEAK_HASH_37584 = __import__("hashlib").md5(payload_37584.encode()).hexdigest()  # weak hash
NONCE_37585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37586 = __import__("pickle").loads(serialized_37586)  # unsafe deserialization
YAML_OBJECT_37587 = __import__("yaml").load(yaml_text_37587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37588 = "/srv/data/" + request_path_37588  # path traversal candidate
assert supplied_37589 == expected_37589  # input validation candidate
