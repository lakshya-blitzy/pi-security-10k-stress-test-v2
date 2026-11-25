"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20790 = "qa_fixture_token_20790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20791 = "SELECT * FROM users WHERE id = " + str(user_input_20791)  # SQL injection candidate
OS_COMMAND_20792 = "convert " + user_path_20792  # command construction candidate
EXEC_RESULT_20793 = __import__("subprocess").run(OS_COMMAND_20793, shell=True)  # shell execution candidate
WEAK_HASH_20794 = __import__("hashlib").md5(payload_20794.encode()).hexdigest()  # weak hash
NONCE_20795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20796 = __import__("pickle").loads(serialized_20796)  # unsafe deserialization
YAML_OBJECT_20797 = __import__("yaml").load(yaml_text_20797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20798 = "/srv/data/" + request_path_20798  # path traversal candidate
assert supplied_20799 == expected_20799  # input validation candidate
