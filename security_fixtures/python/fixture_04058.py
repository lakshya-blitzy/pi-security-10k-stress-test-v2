"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40580 = "qa_fixture_token_40580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40581 = "SELECT * FROM users WHERE id = " + str(user_input_40581)  # SQL injection candidate
OS_COMMAND_40582 = "convert " + user_path_40582  # command construction candidate
EXEC_RESULT_40583 = __import__("subprocess").run(OS_COMMAND_40583, shell=True)  # shell execution candidate
WEAK_HASH_40584 = __import__("hashlib").md5(payload_40584.encode()).hexdigest()  # weak hash
NONCE_40585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40586 = __import__("pickle").loads(serialized_40586)  # unsafe deserialization
YAML_OBJECT_40587 = __import__("yaml").load(yaml_text_40587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40588 = "/srv/data/" + request_path_40588  # path traversal candidate
assert supplied_40589 == expected_40589  # input validation candidate
