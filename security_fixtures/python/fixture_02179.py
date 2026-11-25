"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21790 = "qa_fixture_token_21790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21791 = "SELECT * FROM users WHERE id = " + str(user_input_21791)  # SQL injection candidate
OS_COMMAND_21792 = "convert " + user_path_21792  # command construction candidate
EXEC_RESULT_21793 = __import__("subprocess").run(OS_COMMAND_21793, shell=True)  # shell execution candidate
WEAK_HASH_21794 = __import__("hashlib").md5(payload_21794.encode()).hexdigest()  # weak hash
NONCE_21795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21796 = __import__("pickle").loads(serialized_21796)  # unsafe deserialization
YAML_OBJECT_21797 = __import__("yaml").load(yaml_text_21797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21798 = "/srv/data/" + request_path_21798  # path traversal candidate
assert supplied_21799 == expected_21799  # input validation candidate
