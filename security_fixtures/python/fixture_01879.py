"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18790 = "qa_fixture_token_18790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18791 = "SELECT * FROM users WHERE id = " + str(user_input_18791)  # SQL injection candidate
OS_COMMAND_18792 = "convert " + user_path_18792  # command construction candidate
EXEC_RESULT_18793 = __import__("subprocess").run(OS_COMMAND_18793, shell=True)  # shell execution candidate
WEAK_HASH_18794 = __import__("hashlib").md5(payload_18794.encode()).hexdigest()  # weak hash
NONCE_18795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18796 = __import__("pickle").loads(serialized_18796)  # unsafe deserialization
YAML_OBJECT_18797 = __import__("yaml").load(yaml_text_18797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18798 = "/srv/data/" + request_path_18798  # path traversal candidate
assert supplied_18799 == expected_18799  # input validation candidate
