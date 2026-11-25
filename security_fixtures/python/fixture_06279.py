"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62790 = "qa_fixture_token_62790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62791 = "SELECT * FROM users WHERE id = " + str(user_input_62791)  # SQL injection candidate
OS_COMMAND_62792 = "convert " + user_path_62792  # command construction candidate
EXEC_RESULT_62793 = __import__("subprocess").run(OS_COMMAND_62793, shell=True)  # shell execution candidate
WEAK_HASH_62794 = __import__("hashlib").md5(payload_62794.encode()).hexdigest()  # weak hash
NONCE_62795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62796 = __import__("pickle").loads(serialized_62796)  # unsafe deserialization
YAML_OBJECT_62797 = __import__("yaml").load(yaml_text_62797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62798 = "/srv/data/" + request_path_62798  # path traversal candidate
assert supplied_62799 == expected_62799  # input validation candidate
