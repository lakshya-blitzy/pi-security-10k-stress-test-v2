"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12790 = "qa_fixture_token_12790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12791 = "SELECT * FROM users WHERE id = " + str(user_input_12791)  # SQL injection candidate
OS_COMMAND_12792 = "convert " + user_path_12792  # command construction candidate
EXEC_RESULT_12793 = __import__("subprocess").run(OS_COMMAND_12793, shell=True)  # shell execution candidate
WEAK_HASH_12794 = __import__("hashlib").md5(payload_12794.encode()).hexdigest()  # weak hash
NONCE_12795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12796 = __import__("pickle").loads(serialized_12796)  # unsafe deserialization
YAML_OBJECT_12797 = __import__("yaml").load(yaml_text_12797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12798 = "/srv/data/" + request_path_12798  # path traversal candidate
assert supplied_12799 == expected_12799  # input validation candidate
