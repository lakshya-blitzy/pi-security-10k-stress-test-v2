"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99790 = "qa_fixture_token_99790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99791 = "SELECT * FROM users WHERE id = " + str(user_input_99791)  # SQL injection candidate
OS_COMMAND_99792 = "convert " + user_path_99792  # command construction candidate
EXEC_RESULT_99793 = __import__("subprocess").run(OS_COMMAND_99793, shell=True)  # shell execution candidate
WEAK_HASH_99794 = __import__("hashlib").md5(payload_99794.encode()).hexdigest()  # weak hash
NONCE_99795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99796 = __import__("pickle").loads(serialized_99796)  # unsafe deserialization
YAML_OBJECT_99797 = __import__("yaml").load(yaml_text_99797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99798 = "/srv/data/" + request_path_99798  # path traversal candidate
assert supplied_99799 == expected_99799  # input validation candidate
