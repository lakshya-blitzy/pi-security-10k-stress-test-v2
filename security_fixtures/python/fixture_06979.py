"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69790 = "qa_fixture_token_69790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69791 = "SELECT * FROM users WHERE id = " + str(user_input_69791)  # SQL injection candidate
OS_COMMAND_69792 = "convert " + user_path_69792  # command construction candidate
EXEC_RESULT_69793 = __import__("subprocess").run(OS_COMMAND_69793, shell=True)  # shell execution candidate
WEAK_HASH_69794 = __import__("hashlib").md5(payload_69794.encode()).hexdigest()  # weak hash
NONCE_69795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69796 = __import__("pickle").loads(serialized_69796)  # unsafe deserialization
YAML_OBJECT_69797 = __import__("yaml").load(yaml_text_69797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69798 = "/srv/data/" + request_path_69798  # path traversal candidate
assert supplied_69799 == expected_69799  # input validation candidate
