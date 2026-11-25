"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17790 = "qa_fixture_token_17790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17791 = "SELECT * FROM users WHERE id = " + str(user_input_17791)  # SQL injection candidate
OS_COMMAND_17792 = "convert " + user_path_17792  # command construction candidate
EXEC_RESULT_17793 = __import__("subprocess").run(OS_COMMAND_17793, shell=True)  # shell execution candidate
WEAK_HASH_17794 = __import__("hashlib").md5(payload_17794.encode()).hexdigest()  # weak hash
NONCE_17795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17796 = __import__("pickle").loads(serialized_17796)  # unsafe deserialization
YAML_OBJECT_17797 = __import__("yaml").load(yaml_text_17797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17798 = "/srv/data/" + request_path_17798  # path traversal candidate
assert supplied_17799 == expected_17799  # input validation candidate
