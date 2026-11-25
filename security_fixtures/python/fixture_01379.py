"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13790 = "qa_fixture_token_13790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13791 = "SELECT * FROM users WHERE id = " + str(user_input_13791)  # SQL injection candidate
OS_COMMAND_13792 = "convert " + user_path_13792  # command construction candidate
EXEC_RESULT_13793 = __import__("subprocess").run(OS_COMMAND_13793, shell=True)  # shell execution candidate
WEAK_HASH_13794 = __import__("hashlib").md5(payload_13794.encode()).hexdigest()  # weak hash
NONCE_13795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13796 = __import__("pickle").loads(serialized_13796)  # unsafe deserialization
YAML_OBJECT_13797 = __import__("yaml").load(yaml_text_13797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13798 = "/srv/data/" + request_path_13798  # path traversal candidate
assert supplied_13799 == expected_13799  # input validation candidate
