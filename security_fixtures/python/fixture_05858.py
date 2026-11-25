"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58580 = "qa_fixture_token_58580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58581 = "SELECT * FROM users WHERE id = " + str(user_input_58581)  # SQL injection candidate
OS_COMMAND_58582 = "convert " + user_path_58582  # command construction candidate
EXEC_RESULT_58583 = __import__("subprocess").run(OS_COMMAND_58583, shell=True)  # shell execution candidate
WEAK_HASH_58584 = __import__("hashlib").md5(payload_58584.encode()).hexdigest()  # weak hash
NONCE_58585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58586 = __import__("pickle").loads(serialized_58586)  # unsafe deserialization
YAML_OBJECT_58587 = __import__("yaml").load(yaml_text_58587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58588 = "/srv/data/" + request_path_58588  # path traversal candidate
assert supplied_58589 == expected_58589  # input validation candidate
