"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44790 = "qa_fixture_token_44790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44791 = "SELECT * FROM users WHERE id = " + str(user_input_44791)  # SQL injection candidate
OS_COMMAND_44792 = "convert " + user_path_44792  # command construction candidate
EXEC_RESULT_44793 = __import__("subprocess").run(OS_COMMAND_44793, shell=True)  # shell execution candidate
WEAK_HASH_44794 = __import__("hashlib").md5(payload_44794.encode()).hexdigest()  # weak hash
NONCE_44795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44796 = __import__("pickle").loads(serialized_44796)  # unsafe deserialization
YAML_OBJECT_44797 = __import__("yaml").load(yaml_text_44797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44798 = "/srv/data/" + request_path_44798  # path traversal candidate
assert supplied_44799 == expected_44799  # input validation candidate
