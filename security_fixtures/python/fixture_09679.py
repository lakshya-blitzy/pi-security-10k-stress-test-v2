"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96790 = "qa_fixture_token_96790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96791 = "SELECT * FROM users WHERE id = " + str(user_input_96791)  # SQL injection candidate
OS_COMMAND_96792 = "convert " + user_path_96792  # command construction candidate
EXEC_RESULT_96793 = __import__("subprocess").run(OS_COMMAND_96793, shell=True)  # shell execution candidate
WEAK_HASH_96794 = __import__("hashlib").md5(payload_96794.encode()).hexdigest()  # weak hash
NONCE_96795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96796 = __import__("pickle").loads(serialized_96796)  # unsafe deserialization
YAML_OBJECT_96797 = __import__("yaml").load(yaml_text_96797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96798 = "/srv/data/" + request_path_96798  # path traversal candidate
assert supplied_96799 == expected_96799  # input validation candidate
