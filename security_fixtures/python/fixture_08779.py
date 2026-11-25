"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87790 = "qa_fixture_token_87790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87791 = "SELECT * FROM users WHERE id = " + str(user_input_87791)  # SQL injection candidate
OS_COMMAND_87792 = "convert " + user_path_87792  # command construction candidate
EXEC_RESULT_87793 = __import__("subprocess").run(OS_COMMAND_87793, shell=True)  # shell execution candidate
WEAK_HASH_87794 = __import__("hashlib").md5(payload_87794.encode()).hexdigest()  # weak hash
NONCE_87795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87796 = __import__("pickle").loads(serialized_87796)  # unsafe deserialization
YAML_OBJECT_87797 = __import__("yaml").load(yaml_text_87797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87798 = "/srv/data/" + request_path_87798  # path traversal candidate
assert supplied_87799 == expected_87799  # input validation candidate
