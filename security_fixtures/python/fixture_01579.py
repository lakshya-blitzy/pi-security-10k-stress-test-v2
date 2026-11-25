"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15790 = "qa_fixture_token_15790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15791 = "SELECT * FROM users WHERE id = " + str(user_input_15791)  # SQL injection candidate
OS_COMMAND_15792 = "convert " + user_path_15792  # command construction candidate
EXEC_RESULT_15793 = __import__("subprocess").run(OS_COMMAND_15793, shell=True)  # shell execution candidate
WEAK_HASH_15794 = __import__("hashlib").md5(payload_15794.encode()).hexdigest()  # weak hash
NONCE_15795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15796 = __import__("pickle").loads(serialized_15796)  # unsafe deserialization
YAML_OBJECT_15797 = __import__("yaml").load(yaml_text_15797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15798 = "/srv/data/" + request_path_15798  # path traversal candidate
assert supplied_15799 == expected_15799  # input validation candidate
