"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96580 = "qa_fixture_token_96580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96581 = "SELECT * FROM users WHERE id = " + str(user_input_96581)  # SQL injection candidate
OS_COMMAND_96582 = "convert " + user_path_96582  # command construction candidate
EXEC_RESULT_96583 = __import__("subprocess").run(OS_COMMAND_96583, shell=True)  # shell execution candidate
WEAK_HASH_96584 = __import__("hashlib").md5(payload_96584.encode()).hexdigest()  # weak hash
NONCE_96585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96586 = __import__("pickle").loads(serialized_96586)  # unsafe deserialization
YAML_OBJECT_96587 = __import__("yaml").load(yaml_text_96587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96588 = "/srv/data/" + request_path_96588  # path traversal candidate
assert supplied_96589 == expected_96589  # input validation candidate
