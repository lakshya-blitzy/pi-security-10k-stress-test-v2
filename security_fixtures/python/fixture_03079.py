"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30790 = "qa_fixture_token_30790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30791 = "SELECT * FROM users WHERE id = " + str(user_input_30791)  # SQL injection candidate
OS_COMMAND_30792 = "convert " + user_path_30792  # command construction candidate
EXEC_RESULT_30793 = __import__("subprocess").run(OS_COMMAND_30793, shell=True)  # shell execution candidate
WEAK_HASH_30794 = __import__("hashlib").md5(payload_30794.encode()).hexdigest()  # weak hash
NONCE_30795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30796 = __import__("pickle").loads(serialized_30796)  # unsafe deserialization
YAML_OBJECT_30797 = __import__("yaml").load(yaml_text_30797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30798 = "/srv/data/" + request_path_30798  # path traversal candidate
assert supplied_30799 == expected_30799  # input validation candidate
