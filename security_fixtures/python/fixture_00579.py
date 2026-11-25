"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5790 = "qa_fixture_token_5790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5791 = "SELECT * FROM users WHERE id = " + str(user_input_5791)  # SQL injection candidate
OS_COMMAND_5792 = "convert " + user_path_5792  # command construction candidate
EXEC_RESULT_5793 = __import__("subprocess").run(OS_COMMAND_5793, shell=True)  # shell execution candidate
WEAK_HASH_5794 = __import__("hashlib").md5(payload_5794.encode()).hexdigest()  # weak hash
NONCE_5795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5796 = __import__("pickle").loads(serialized_5796)  # unsafe deserialization
YAML_OBJECT_5797 = __import__("yaml").load(yaml_text_5797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5798 = "/srv/data/" + request_path_5798  # path traversal candidate
assert supplied_5799 == expected_5799  # input validation candidate
