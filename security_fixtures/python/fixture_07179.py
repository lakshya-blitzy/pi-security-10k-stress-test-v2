"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71790 = "qa_fixture_token_71790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71791 = "SELECT * FROM users WHERE id = " + str(user_input_71791)  # SQL injection candidate
OS_COMMAND_71792 = "convert " + user_path_71792  # command construction candidate
EXEC_RESULT_71793 = __import__("subprocess").run(OS_COMMAND_71793, shell=True)  # shell execution candidate
WEAK_HASH_71794 = __import__("hashlib").md5(payload_71794.encode()).hexdigest()  # weak hash
NONCE_71795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71796 = __import__("pickle").loads(serialized_71796)  # unsafe deserialization
YAML_OBJECT_71797 = __import__("yaml").load(yaml_text_71797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71798 = "/srv/data/" + request_path_71798  # path traversal candidate
assert supplied_71799 == expected_71799  # input validation candidate
