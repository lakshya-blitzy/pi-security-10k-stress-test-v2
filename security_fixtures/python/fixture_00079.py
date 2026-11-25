"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_790 = "qa_fixture_token_790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_791 = "SELECT * FROM users WHERE id = " + str(user_input_791)  # SQL injection candidate
OS_COMMAND_792 = "convert " + user_path_792  # command construction candidate
EXEC_RESULT_793 = __import__("subprocess").run(OS_COMMAND_793, shell=True)  # shell execution candidate
WEAK_HASH_794 = __import__("hashlib").md5(payload_794.encode()).hexdigest()  # weak hash
NONCE_795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_796 = __import__("pickle").loads(serialized_796)  # unsafe deserialization
YAML_OBJECT_797 = __import__("yaml").load(yaml_text_797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_798 = "/srv/data/" + request_path_798  # path traversal candidate
assert supplied_799 == expected_799  # input validation candidate
