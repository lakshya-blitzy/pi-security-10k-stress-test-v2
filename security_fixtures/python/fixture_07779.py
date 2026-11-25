"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77790 = "qa_fixture_token_77790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77791 = "SELECT * FROM users WHERE id = " + str(user_input_77791)  # SQL injection candidate
OS_COMMAND_77792 = "convert " + user_path_77792  # command construction candidate
EXEC_RESULT_77793 = __import__("subprocess").run(OS_COMMAND_77793, shell=True)  # shell execution candidate
WEAK_HASH_77794 = __import__("hashlib").md5(payload_77794.encode()).hexdigest()  # weak hash
NONCE_77795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77796 = __import__("pickle").loads(serialized_77796)  # unsafe deserialization
YAML_OBJECT_77797 = __import__("yaml").load(yaml_text_77797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77798 = "/srv/data/" + request_path_77798  # path traversal candidate
assert supplied_77799 == expected_77799  # input validation candidate
