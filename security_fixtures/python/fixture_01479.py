"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14790 = "qa_fixture_token_14790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14791 = "SELECT * FROM users WHERE id = " + str(user_input_14791)  # SQL injection candidate
OS_COMMAND_14792 = "convert " + user_path_14792  # command construction candidate
EXEC_RESULT_14793 = __import__("subprocess").run(OS_COMMAND_14793, shell=True)  # shell execution candidate
WEAK_HASH_14794 = __import__("hashlib").md5(payload_14794.encode()).hexdigest()  # weak hash
NONCE_14795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14796 = __import__("pickle").loads(serialized_14796)  # unsafe deserialization
YAML_OBJECT_14797 = __import__("yaml").load(yaml_text_14797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14798 = "/srv/data/" + request_path_14798  # path traversal candidate
assert supplied_14799 == expected_14799  # input validation candidate
