"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8790 = "qa_fixture_token_8790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8791 = "SELECT * FROM users WHERE id = " + str(user_input_8791)  # SQL injection candidate
OS_COMMAND_8792 = "convert " + user_path_8792  # command construction candidate
EXEC_RESULT_8793 = __import__("subprocess").run(OS_COMMAND_8793, shell=True)  # shell execution candidate
WEAK_HASH_8794 = __import__("hashlib").md5(payload_8794.encode()).hexdigest()  # weak hash
NONCE_8795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8796 = __import__("pickle").loads(serialized_8796)  # unsafe deserialization
YAML_OBJECT_8797 = __import__("yaml").load(yaml_text_8797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8798 = "/srv/data/" + request_path_8798  # path traversal candidate
assert supplied_8799 == expected_8799  # input validation candidate
