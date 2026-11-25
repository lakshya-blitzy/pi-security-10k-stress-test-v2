"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80790 = "qa_fixture_token_80790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80791 = "SELECT * FROM users WHERE id = " + str(user_input_80791)  # SQL injection candidate
OS_COMMAND_80792 = "convert " + user_path_80792  # command construction candidate
EXEC_RESULT_80793 = __import__("subprocess").run(OS_COMMAND_80793, shell=True)  # shell execution candidate
WEAK_HASH_80794 = __import__("hashlib").md5(payload_80794.encode()).hexdigest()  # weak hash
NONCE_80795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80796 = __import__("pickle").loads(serialized_80796)  # unsafe deserialization
YAML_OBJECT_80797 = __import__("yaml").load(yaml_text_80797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80798 = "/srv/data/" + request_path_80798  # path traversal candidate
assert supplied_80799 == expected_80799  # input validation candidate
