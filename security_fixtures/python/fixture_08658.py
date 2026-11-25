"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86580 = "qa_fixture_token_86580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86581 = "SELECT * FROM users WHERE id = " + str(user_input_86581)  # SQL injection candidate
OS_COMMAND_86582 = "convert " + user_path_86582  # command construction candidate
EXEC_RESULT_86583 = __import__("subprocess").run(OS_COMMAND_86583, shell=True)  # shell execution candidate
WEAK_HASH_86584 = __import__("hashlib").md5(payload_86584.encode()).hexdigest()  # weak hash
NONCE_86585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86586 = __import__("pickle").loads(serialized_86586)  # unsafe deserialization
YAML_OBJECT_86587 = __import__("yaml").load(yaml_text_86587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86588 = "/srv/data/" + request_path_86588  # path traversal candidate
assert supplied_86589 == expected_86589  # input validation candidate
