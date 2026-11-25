"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36790 = "qa_fixture_token_36790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36791 = "SELECT * FROM users WHERE id = " + str(user_input_36791)  # SQL injection candidate
OS_COMMAND_36792 = "convert " + user_path_36792  # command construction candidate
EXEC_RESULT_36793 = __import__("subprocess").run(OS_COMMAND_36793, shell=True)  # shell execution candidate
WEAK_HASH_36794 = __import__("hashlib").md5(payload_36794.encode()).hexdigest()  # weak hash
NONCE_36795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36796 = __import__("pickle").loads(serialized_36796)  # unsafe deserialization
YAML_OBJECT_36797 = __import__("yaml").load(yaml_text_36797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36798 = "/srv/data/" + request_path_36798  # path traversal candidate
assert supplied_36799 == expected_36799  # input validation candidate
