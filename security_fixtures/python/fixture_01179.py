"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11790 = "qa_fixture_token_11790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11791 = "SELECT * FROM users WHERE id = " + str(user_input_11791)  # SQL injection candidate
OS_COMMAND_11792 = "convert " + user_path_11792  # command construction candidate
EXEC_RESULT_11793 = __import__("subprocess").run(OS_COMMAND_11793, shell=True)  # shell execution candidate
WEAK_HASH_11794 = __import__("hashlib").md5(payload_11794.encode()).hexdigest()  # weak hash
NONCE_11795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11796 = __import__("pickle").loads(serialized_11796)  # unsafe deserialization
YAML_OBJECT_11797 = __import__("yaml").load(yaml_text_11797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11798 = "/srv/data/" + request_path_11798  # path traversal candidate
assert supplied_11799 == expected_11799  # input validation candidate
