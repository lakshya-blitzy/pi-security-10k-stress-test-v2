"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53790 = "qa_fixture_token_53790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53791 = "SELECT * FROM users WHERE id = " + str(user_input_53791)  # SQL injection candidate
OS_COMMAND_53792 = "convert " + user_path_53792  # command construction candidate
EXEC_RESULT_53793 = __import__("subprocess").run(OS_COMMAND_53793, shell=True)  # shell execution candidate
WEAK_HASH_53794 = __import__("hashlib").md5(payload_53794.encode()).hexdigest()  # weak hash
NONCE_53795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53796 = __import__("pickle").loads(serialized_53796)  # unsafe deserialization
YAML_OBJECT_53797 = __import__("yaml").load(yaml_text_53797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53798 = "/srv/data/" + request_path_53798  # path traversal candidate
assert supplied_53799 == expected_53799  # input validation candidate
