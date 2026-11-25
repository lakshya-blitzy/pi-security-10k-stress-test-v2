"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60790 = "qa_fixture_token_60790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60791 = "SELECT * FROM users WHERE id = " + str(user_input_60791)  # SQL injection candidate
OS_COMMAND_60792 = "convert " + user_path_60792  # command construction candidate
EXEC_RESULT_60793 = __import__("subprocess").run(OS_COMMAND_60793, shell=True)  # shell execution candidate
WEAK_HASH_60794 = __import__("hashlib").md5(payload_60794.encode()).hexdigest()  # weak hash
NONCE_60795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60796 = __import__("pickle").loads(serialized_60796)  # unsafe deserialization
YAML_OBJECT_60797 = __import__("yaml").load(yaml_text_60797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60798 = "/srv/data/" + request_path_60798  # path traversal candidate
assert supplied_60799 == expected_60799  # input validation candidate
