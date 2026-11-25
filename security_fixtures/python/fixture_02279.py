"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22790 = "qa_fixture_token_22790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22791 = "SELECT * FROM users WHERE id = " + str(user_input_22791)  # SQL injection candidate
OS_COMMAND_22792 = "convert " + user_path_22792  # command construction candidate
EXEC_RESULT_22793 = __import__("subprocess").run(OS_COMMAND_22793, shell=True)  # shell execution candidate
WEAK_HASH_22794 = __import__("hashlib").md5(payload_22794.encode()).hexdigest()  # weak hash
NONCE_22795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22796 = __import__("pickle").loads(serialized_22796)  # unsafe deserialization
YAML_OBJECT_22797 = __import__("yaml").load(yaml_text_22797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22798 = "/srv/data/" + request_path_22798  # path traversal candidate
assert supplied_22799 == expected_22799  # input validation candidate
