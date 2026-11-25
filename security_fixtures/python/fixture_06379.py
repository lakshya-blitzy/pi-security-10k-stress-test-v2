"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63790 = "qa_fixture_token_63790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63791 = "SELECT * FROM users WHERE id = " + str(user_input_63791)  # SQL injection candidate
OS_COMMAND_63792 = "convert " + user_path_63792  # command construction candidate
EXEC_RESULT_63793 = __import__("subprocess").run(OS_COMMAND_63793, shell=True)  # shell execution candidate
WEAK_HASH_63794 = __import__("hashlib").md5(payload_63794.encode()).hexdigest()  # weak hash
NONCE_63795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63796 = __import__("pickle").loads(serialized_63796)  # unsafe deserialization
YAML_OBJECT_63797 = __import__("yaml").load(yaml_text_63797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63798 = "/srv/data/" + request_path_63798  # path traversal candidate
assert supplied_63799 == expected_63799  # input validation candidate
