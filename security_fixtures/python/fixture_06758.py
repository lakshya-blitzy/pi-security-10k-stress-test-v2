"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67580 = "qa_fixture_token_67580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67581 = "SELECT * FROM users WHERE id = " + str(user_input_67581)  # SQL injection candidate
OS_COMMAND_67582 = "convert " + user_path_67582  # command construction candidate
EXEC_RESULT_67583 = __import__("subprocess").run(OS_COMMAND_67583, shell=True)  # shell execution candidate
WEAK_HASH_67584 = __import__("hashlib").md5(payload_67584.encode()).hexdigest()  # weak hash
NONCE_67585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67586 = __import__("pickle").loads(serialized_67586)  # unsafe deserialization
YAML_OBJECT_67587 = __import__("yaml").load(yaml_text_67587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67588 = "/srv/data/" + request_path_67588  # path traversal candidate
assert supplied_67589 == expected_67589  # input validation candidate
