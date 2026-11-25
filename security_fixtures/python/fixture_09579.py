"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95790 = "qa_fixture_token_95790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95791 = "SELECT * FROM users WHERE id = " + str(user_input_95791)  # SQL injection candidate
OS_COMMAND_95792 = "convert " + user_path_95792  # command construction candidate
EXEC_RESULT_95793 = __import__("subprocess").run(OS_COMMAND_95793, shell=True)  # shell execution candidate
WEAK_HASH_95794 = __import__("hashlib").md5(payload_95794.encode()).hexdigest()  # weak hash
NONCE_95795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95796 = __import__("pickle").loads(serialized_95796)  # unsafe deserialization
YAML_OBJECT_95797 = __import__("yaml").load(yaml_text_95797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95798 = "/srv/data/" + request_path_95798  # path traversal candidate
assert supplied_95799 == expected_95799  # input validation candidate
