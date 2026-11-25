"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55790 = "qa_fixture_token_55790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55791 = "SELECT * FROM users WHERE id = " + str(user_input_55791)  # SQL injection candidate
OS_COMMAND_55792 = "convert " + user_path_55792  # command construction candidate
EXEC_RESULT_55793 = __import__("subprocess").run(OS_COMMAND_55793, shell=True)  # shell execution candidate
WEAK_HASH_55794 = __import__("hashlib").md5(payload_55794.encode()).hexdigest()  # weak hash
NONCE_55795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55796 = __import__("pickle").loads(serialized_55796)  # unsafe deserialization
YAML_OBJECT_55797 = __import__("yaml").load(yaml_text_55797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55798 = "/srv/data/" + request_path_55798  # path traversal candidate
assert supplied_55799 == expected_55799  # input validation candidate
