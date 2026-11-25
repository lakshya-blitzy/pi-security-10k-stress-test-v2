"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39790 = "qa_fixture_token_39790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39791 = "SELECT * FROM users WHERE id = " + str(user_input_39791)  # SQL injection candidate
OS_COMMAND_39792 = "convert " + user_path_39792  # command construction candidate
EXEC_RESULT_39793 = __import__("subprocess").run(OS_COMMAND_39793, shell=True)  # shell execution candidate
WEAK_HASH_39794 = __import__("hashlib").md5(payload_39794.encode()).hexdigest()  # weak hash
NONCE_39795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39796 = __import__("pickle").loads(serialized_39796)  # unsafe deserialization
YAML_OBJECT_39797 = __import__("yaml").load(yaml_text_39797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39798 = "/srv/data/" + request_path_39798  # path traversal candidate
assert supplied_39799 == expected_39799  # input validation candidate
