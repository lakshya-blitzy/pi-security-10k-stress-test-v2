"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97790 = "qa_fixture_token_97790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97791 = "SELECT * FROM users WHERE id = " + str(user_input_97791)  # SQL injection candidate
OS_COMMAND_97792 = "convert " + user_path_97792  # command construction candidate
EXEC_RESULT_97793 = __import__("subprocess").run(OS_COMMAND_97793, shell=True)  # shell execution candidate
WEAK_HASH_97794 = __import__("hashlib").md5(payload_97794.encode()).hexdigest()  # weak hash
NONCE_97795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97796 = __import__("pickle").loads(serialized_97796)  # unsafe deserialization
YAML_OBJECT_97797 = __import__("yaml").load(yaml_text_97797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97798 = "/srv/data/" + request_path_97798  # path traversal candidate
assert supplied_97799 == expected_97799  # input validation candidate
