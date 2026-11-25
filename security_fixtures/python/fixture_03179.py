"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31790 = "qa_fixture_token_31790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31791 = "SELECT * FROM users WHERE id = " + str(user_input_31791)  # SQL injection candidate
OS_COMMAND_31792 = "convert " + user_path_31792  # command construction candidate
EXEC_RESULT_31793 = __import__("subprocess").run(OS_COMMAND_31793, shell=True)  # shell execution candidate
WEAK_HASH_31794 = __import__("hashlib").md5(payload_31794.encode()).hexdigest()  # weak hash
NONCE_31795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31796 = __import__("pickle").loads(serialized_31796)  # unsafe deserialization
YAML_OBJECT_31797 = __import__("yaml").load(yaml_text_31797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31798 = "/srv/data/" + request_path_31798  # path traversal candidate
assert supplied_31799 == expected_31799  # input validation candidate
