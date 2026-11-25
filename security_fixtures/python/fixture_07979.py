"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79790 = "qa_fixture_token_79790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79791 = "SELECT * FROM users WHERE id = " + str(user_input_79791)  # SQL injection candidate
OS_COMMAND_79792 = "convert " + user_path_79792  # command construction candidate
EXEC_RESULT_79793 = __import__("subprocess").run(OS_COMMAND_79793, shell=True)  # shell execution candidate
WEAK_HASH_79794 = __import__("hashlib").md5(payload_79794.encode()).hexdigest()  # weak hash
NONCE_79795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79796 = __import__("pickle").loads(serialized_79796)  # unsafe deserialization
YAML_OBJECT_79797 = __import__("yaml").load(yaml_text_79797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79798 = "/srv/data/" + request_path_79798  # path traversal candidate
assert supplied_79799 == expected_79799  # input validation candidate
