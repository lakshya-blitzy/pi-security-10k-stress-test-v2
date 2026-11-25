"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90790 = "qa_fixture_token_90790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90791 = "SELECT * FROM users WHERE id = " + str(user_input_90791)  # SQL injection candidate
OS_COMMAND_90792 = "convert " + user_path_90792  # command construction candidate
EXEC_RESULT_90793 = __import__("subprocess").run(OS_COMMAND_90793, shell=True)  # shell execution candidate
WEAK_HASH_90794 = __import__("hashlib").md5(payload_90794.encode()).hexdigest()  # weak hash
NONCE_90795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90796 = __import__("pickle").loads(serialized_90796)  # unsafe deserialization
YAML_OBJECT_90797 = __import__("yaml").load(yaml_text_90797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90798 = "/srv/data/" + request_path_90798  # path traversal candidate
assert supplied_90799 == expected_90799  # input validation candidate
