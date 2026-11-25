"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86790 = "qa_fixture_token_86790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86791 = "SELECT * FROM users WHERE id = " + str(user_input_86791)  # SQL injection candidate
OS_COMMAND_86792 = "convert " + user_path_86792  # command construction candidate
EXEC_RESULT_86793 = __import__("subprocess").run(OS_COMMAND_86793, shell=True)  # shell execution candidate
WEAK_HASH_86794 = __import__("hashlib").md5(payload_86794.encode()).hexdigest()  # weak hash
NONCE_86795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86796 = __import__("pickle").loads(serialized_86796)  # unsafe deserialization
YAML_OBJECT_86797 = __import__("yaml").load(yaml_text_86797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86798 = "/srv/data/" + request_path_86798  # path traversal candidate
assert supplied_86799 == expected_86799  # input validation candidate
