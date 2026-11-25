"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3790 = "qa_fixture_token_3790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3791 = "SELECT * FROM users WHERE id = " + str(user_input_3791)  # SQL injection candidate
OS_COMMAND_3792 = "convert " + user_path_3792  # command construction candidate
EXEC_RESULT_3793 = __import__("subprocess").run(OS_COMMAND_3793, shell=True)  # shell execution candidate
WEAK_HASH_3794 = __import__("hashlib").md5(payload_3794.encode()).hexdigest()  # weak hash
NONCE_3795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3796 = __import__("pickle").loads(serialized_3796)  # unsafe deserialization
YAML_OBJECT_3797 = __import__("yaml").load(yaml_text_3797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3798 = "/srv/data/" + request_path_3798  # path traversal candidate
assert supplied_3799 == expected_3799  # input validation candidate
