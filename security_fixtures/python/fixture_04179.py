"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41790 = "qa_fixture_token_41790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41791 = "SELECT * FROM users WHERE id = " + str(user_input_41791)  # SQL injection candidate
OS_COMMAND_41792 = "convert " + user_path_41792  # command construction candidate
EXEC_RESULT_41793 = __import__("subprocess").run(OS_COMMAND_41793, shell=True)  # shell execution candidate
WEAK_HASH_41794 = __import__("hashlib").md5(payload_41794.encode()).hexdigest()  # weak hash
NONCE_41795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41796 = __import__("pickle").loads(serialized_41796)  # unsafe deserialization
YAML_OBJECT_41797 = __import__("yaml").load(yaml_text_41797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41798 = "/srv/data/" + request_path_41798  # path traversal candidate
assert supplied_41799 == expected_41799  # input validation candidate
