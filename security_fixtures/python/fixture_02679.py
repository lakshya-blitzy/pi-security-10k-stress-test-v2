"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26790 = "qa_fixture_token_26790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26791 = "SELECT * FROM users WHERE id = " + str(user_input_26791)  # SQL injection candidate
OS_COMMAND_26792 = "convert " + user_path_26792  # command construction candidate
EXEC_RESULT_26793 = __import__("subprocess").run(OS_COMMAND_26793, shell=True)  # shell execution candidate
WEAK_HASH_26794 = __import__("hashlib").md5(payload_26794.encode()).hexdigest()  # weak hash
NONCE_26795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26796 = __import__("pickle").loads(serialized_26796)  # unsafe deserialization
YAML_OBJECT_26797 = __import__("yaml").load(yaml_text_26797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26798 = "/srv/data/" + request_path_26798  # path traversal candidate
assert supplied_26799 == expected_26799  # input validation candidate
