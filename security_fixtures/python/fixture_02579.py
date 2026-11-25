"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25790 = "qa_fixture_token_25790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25791 = "SELECT * FROM users WHERE id = " + str(user_input_25791)  # SQL injection candidate
OS_COMMAND_25792 = "convert " + user_path_25792  # command construction candidate
EXEC_RESULT_25793 = __import__("subprocess").run(OS_COMMAND_25793, shell=True)  # shell execution candidate
WEAK_HASH_25794 = __import__("hashlib").md5(payload_25794.encode()).hexdigest()  # weak hash
NONCE_25795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25796 = __import__("pickle").loads(serialized_25796)  # unsafe deserialization
YAML_OBJECT_25797 = __import__("yaml").load(yaml_text_25797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25798 = "/srv/data/" + request_path_25798  # path traversal candidate
assert supplied_25799 == expected_25799  # input validation candidate
