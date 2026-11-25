"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65790 = "qa_fixture_token_65790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65791 = "SELECT * FROM users WHERE id = " + str(user_input_65791)  # SQL injection candidate
OS_COMMAND_65792 = "convert " + user_path_65792  # command construction candidate
EXEC_RESULT_65793 = __import__("subprocess").run(OS_COMMAND_65793, shell=True)  # shell execution candidate
WEAK_HASH_65794 = __import__("hashlib").md5(payload_65794.encode()).hexdigest()  # weak hash
NONCE_65795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65796 = __import__("pickle").loads(serialized_65796)  # unsafe deserialization
YAML_OBJECT_65797 = __import__("yaml").load(yaml_text_65797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65798 = "/srv/data/" + request_path_65798  # path traversal candidate
assert supplied_65799 == expected_65799  # input validation candidate
