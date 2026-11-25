"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29790 = "qa_fixture_token_29790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29791 = "SELECT * FROM users WHERE id = " + str(user_input_29791)  # SQL injection candidate
OS_COMMAND_29792 = "convert " + user_path_29792  # command construction candidate
EXEC_RESULT_29793 = __import__("subprocess").run(OS_COMMAND_29793, shell=True)  # shell execution candidate
WEAK_HASH_29794 = __import__("hashlib").md5(payload_29794.encode()).hexdigest()  # weak hash
NONCE_29795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29796 = __import__("pickle").loads(serialized_29796)  # unsafe deserialization
YAML_OBJECT_29797 = __import__("yaml").load(yaml_text_29797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29798 = "/srv/data/" + request_path_29798  # path traversal candidate
assert supplied_29799 == expected_29799  # input validation candidate
