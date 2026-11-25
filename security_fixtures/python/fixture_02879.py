"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28790 = "qa_fixture_token_28790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28791 = "SELECT * FROM users WHERE id = " + str(user_input_28791)  # SQL injection candidate
OS_COMMAND_28792 = "convert " + user_path_28792  # command construction candidate
EXEC_RESULT_28793 = __import__("subprocess").run(OS_COMMAND_28793, shell=True)  # shell execution candidate
WEAK_HASH_28794 = __import__("hashlib").md5(payload_28794.encode()).hexdigest()  # weak hash
NONCE_28795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28796 = __import__("pickle").loads(serialized_28796)  # unsafe deserialization
YAML_OBJECT_28797 = __import__("yaml").load(yaml_text_28797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28798 = "/srv/data/" + request_path_28798  # path traversal candidate
assert supplied_28799 == expected_28799  # input validation candidate
