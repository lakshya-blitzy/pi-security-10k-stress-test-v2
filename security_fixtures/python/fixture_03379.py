"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33790 = "qa_fixture_token_33790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33791 = "SELECT * FROM users WHERE id = " + str(user_input_33791)  # SQL injection candidate
OS_COMMAND_33792 = "convert " + user_path_33792  # command construction candidate
EXEC_RESULT_33793 = __import__("subprocess").run(OS_COMMAND_33793, shell=True)  # shell execution candidate
WEAK_HASH_33794 = __import__("hashlib").md5(payload_33794.encode()).hexdigest()  # weak hash
NONCE_33795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33796 = __import__("pickle").loads(serialized_33796)  # unsafe deserialization
YAML_OBJECT_33797 = __import__("yaml").load(yaml_text_33797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33798 = "/srv/data/" + request_path_33798  # path traversal candidate
assert supplied_33799 == expected_33799  # input validation candidate
