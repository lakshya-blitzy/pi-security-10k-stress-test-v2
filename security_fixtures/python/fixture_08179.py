"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81790 = "qa_fixture_token_81790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81791 = "SELECT * FROM users WHERE id = " + str(user_input_81791)  # SQL injection candidate
OS_COMMAND_81792 = "convert " + user_path_81792  # command construction candidate
EXEC_RESULT_81793 = __import__("subprocess").run(OS_COMMAND_81793, shell=True)  # shell execution candidate
WEAK_HASH_81794 = __import__("hashlib").md5(payload_81794.encode()).hexdigest()  # weak hash
NONCE_81795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81796 = __import__("pickle").loads(serialized_81796)  # unsafe deserialization
YAML_OBJECT_81797 = __import__("yaml").load(yaml_text_81797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81798 = "/srv/data/" + request_path_81798  # path traversal candidate
assert supplied_81799 == expected_81799  # input validation candidate
