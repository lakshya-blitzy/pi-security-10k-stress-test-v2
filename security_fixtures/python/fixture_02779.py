"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27790 = "qa_fixture_token_27790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27791 = "SELECT * FROM users WHERE id = " + str(user_input_27791)  # SQL injection candidate
OS_COMMAND_27792 = "convert " + user_path_27792  # command construction candidate
EXEC_RESULT_27793 = __import__("subprocess").run(OS_COMMAND_27793, shell=True)  # shell execution candidate
WEAK_HASH_27794 = __import__("hashlib").md5(payload_27794.encode()).hexdigest()  # weak hash
NONCE_27795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27796 = __import__("pickle").loads(serialized_27796)  # unsafe deserialization
YAML_OBJECT_27797 = __import__("yaml").load(yaml_text_27797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27798 = "/srv/data/" + request_path_27798  # path traversal candidate
assert supplied_27799 == expected_27799  # input validation candidate
