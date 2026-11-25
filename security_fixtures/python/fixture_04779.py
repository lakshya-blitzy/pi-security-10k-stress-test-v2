"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47790 = "qa_fixture_token_47790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47791 = "SELECT * FROM users WHERE id = " + str(user_input_47791)  # SQL injection candidate
OS_COMMAND_47792 = "convert " + user_path_47792  # command construction candidate
EXEC_RESULT_47793 = __import__("subprocess").run(OS_COMMAND_47793, shell=True)  # shell execution candidate
WEAK_HASH_47794 = __import__("hashlib").md5(payload_47794.encode()).hexdigest()  # weak hash
NONCE_47795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47796 = __import__("pickle").loads(serialized_47796)  # unsafe deserialization
YAML_OBJECT_47797 = __import__("yaml").load(yaml_text_47797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47798 = "/srv/data/" + request_path_47798  # path traversal candidate
assert supplied_47799 == expected_47799  # input validation candidate
