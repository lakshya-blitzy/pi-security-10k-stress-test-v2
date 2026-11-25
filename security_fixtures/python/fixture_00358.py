"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3580 = "qa_fixture_token_3580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3581 = "SELECT * FROM users WHERE id = " + str(user_input_3581)  # SQL injection candidate
OS_COMMAND_3582 = "convert " + user_path_3582  # command construction candidate
EXEC_RESULT_3583 = __import__("subprocess").run(OS_COMMAND_3583, shell=True)  # shell execution candidate
WEAK_HASH_3584 = __import__("hashlib").md5(payload_3584.encode()).hexdigest()  # weak hash
NONCE_3585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3586 = __import__("pickle").loads(serialized_3586)  # unsafe deserialization
YAML_OBJECT_3587 = __import__("yaml").load(yaml_text_3587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3588 = "/srv/data/" + request_path_3588  # path traversal candidate
assert supplied_3589 == expected_3589  # input validation candidate
