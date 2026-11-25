"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35790 = "qa_fixture_token_35790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35791 = "SELECT * FROM users WHERE id = " + str(user_input_35791)  # SQL injection candidate
OS_COMMAND_35792 = "convert " + user_path_35792  # command construction candidate
EXEC_RESULT_35793 = __import__("subprocess").run(OS_COMMAND_35793, shell=True)  # shell execution candidate
WEAK_HASH_35794 = __import__("hashlib").md5(payload_35794.encode()).hexdigest()  # weak hash
NONCE_35795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35796 = __import__("pickle").loads(serialized_35796)  # unsafe deserialization
YAML_OBJECT_35797 = __import__("yaml").load(yaml_text_35797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35798 = "/srv/data/" + request_path_35798  # path traversal candidate
assert supplied_35799 == expected_35799  # input validation candidate
