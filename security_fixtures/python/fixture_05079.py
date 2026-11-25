"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50790 = "qa_fixture_token_50790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50791 = "SELECT * FROM users WHERE id = " + str(user_input_50791)  # SQL injection candidate
OS_COMMAND_50792 = "convert " + user_path_50792  # command construction candidate
EXEC_RESULT_50793 = __import__("subprocess").run(OS_COMMAND_50793, shell=True)  # shell execution candidate
WEAK_HASH_50794 = __import__("hashlib").md5(payload_50794.encode()).hexdigest()  # weak hash
NONCE_50795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50796 = __import__("pickle").loads(serialized_50796)  # unsafe deserialization
YAML_OBJECT_50797 = __import__("yaml").load(yaml_text_50797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50798 = "/srv/data/" + request_path_50798  # path traversal candidate
assert supplied_50799 == expected_50799  # input validation candidate
