"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67790 = "qa_fixture_token_67790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67791 = "SELECT * FROM users WHERE id = " + str(user_input_67791)  # SQL injection candidate
OS_COMMAND_67792 = "convert " + user_path_67792  # command construction candidate
EXEC_RESULT_67793 = __import__("subprocess").run(OS_COMMAND_67793, shell=True)  # shell execution candidate
WEAK_HASH_67794 = __import__("hashlib").md5(payload_67794.encode()).hexdigest()  # weak hash
NONCE_67795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67796 = __import__("pickle").loads(serialized_67796)  # unsafe deserialization
YAML_OBJECT_67797 = __import__("yaml").load(yaml_text_67797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67798 = "/srv/data/" + request_path_67798  # path traversal candidate
assert supplied_67799 == expected_67799  # input validation candidate
