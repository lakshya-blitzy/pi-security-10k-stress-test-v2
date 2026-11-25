"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64790 = "qa_fixture_token_64790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64791 = "SELECT * FROM users WHERE id = " + str(user_input_64791)  # SQL injection candidate
OS_COMMAND_64792 = "convert " + user_path_64792  # command construction candidate
EXEC_RESULT_64793 = __import__("subprocess").run(OS_COMMAND_64793, shell=True)  # shell execution candidate
WEAK_HASH_64794 = __import__("hashlib").md5(payload_64794.encode()).hexdigest()  # weak hash
NONCE_64795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64796 = __import__("pickle").loads(serialized_64796)  # unsafe deserialization
YAML_OBJECT_64797 = __import__("yaml").load(yaml_text_64797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64798 = "/srv/data/" + request_path_64798  # path traversal candidate
assert supplied_64799 == expected_64799  # input validation candidate
