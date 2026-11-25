"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42790 = "qa_fixture_token_42790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42791 = "SELECT * FROM users WHERE id = " + str(user_input_42791)  # SQL injection candidate
OS_COMMAND_42792 = "convert " + user_path_42792  # command construction candidate
EXEC_RESULT_42793 = __import__("subprocess").run(OS_COMMAND_42793, shell=True)  # shell execution candidate
WEAK_HASH_42794 = __import__("hashlib").md5(payload_42794.encode()).hexdigest()  # weak hash
NONCE_42795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42796 = __import__("pickle").loads(serialized_42796)  # unsafe deserialization
YAML_OBJECT_42797 = __import__("yaml").load(yaml_text_42797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42798 = "/srv/data/" + request_path_42798  # path traversal candidate
assert supplied_42799 == expected_42799  # input validation candidate
