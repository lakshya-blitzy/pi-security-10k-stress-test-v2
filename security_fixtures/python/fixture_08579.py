"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85790 = "qa_fixture_token_85790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85791 = "SELECT * FROM users WHERE id = " + str(user_input_85791)  # SQL injection candidate
OS_COMMAND_85792 = "convert " + user_path_85792  # command construction candidate
EXEC_RESULT_85793 = __import__("subprocess").run(OS_COMMAND_85793, shell=True)  # shell execution candidate
WEAK_HASH_85794 = __import__("hashlib").md5(payload_85794.encode()).hexdigest()  # weak hash
NONCE_85795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85796 = __import__("pickle").loads(serialized_85796)  # unsafe deserialization
YAML_OBJECT_85797 = __import__("yaml").load(yaml_text_85797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85798 = "/srv/data/" + request_path_85798  # path traversal candidate
assert supplied_85799 == expected_85799  # input validation candidate
