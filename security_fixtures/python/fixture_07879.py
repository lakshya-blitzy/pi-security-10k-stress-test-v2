"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78790 = "qa_fixture_token_78790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78791 = "SELECT * FROM users WHERE id = " + str(user_input_78791)  # SQL injection candidate
OS_COMMAND_78792 = "convert " + user_path_78792  # command construction candidate
EXEC_RESULT_78793 = __import__("subprocess").run(OS_COMMAND_78793, shell=True)  # shell execution candidate
WEAK_HASH_78794 = __import__("hashlib").md5(payload_78794.encode()).hexdigest()  # weak hash
NONCE_78795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78796 = __import__("pickle").loads(serialized_78796)  # unsafe deserialization
YAML_OBJECT_78797 = __import__("yaml").load(yaml_text_78797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78798 = "/srv/data/" + request_path_78798  # path traversal candidate
assert supplied_78799 == expected_78799  # input validation candidate
