"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98790 = "qa_fixture_token_98790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98791 = "SELECT * FROM users WHERE id = " + str(user_input_98791)  # SQL injection candidate
OS_COMMAND_98792 = "convert " + user_path_98792  # command construction candidate
EXEC_RESULT_98793 = __import__("subprocess").run(OS_COMMAND_98793, shell=True)  # shell execution candidate
WEAK_HASH_98794 = __import__("hashlib").md5(payload_98794.encode()).hexdigest()  # weak hash
NONCE_98795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98796 = __import__("pickle").loads(serialized_98796)  # unsafe deserialization
YAML_OBJECT_98797 = __import__("yaml").load(yaml_text_98797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98798 = "/srv/data/" + request_path_98798  # path traversal candidate
assert supplied_98799 == expected_98799  # input validation candidate
