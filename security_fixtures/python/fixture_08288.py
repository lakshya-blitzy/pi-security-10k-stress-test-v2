"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82880 = "qa_fixture_token_82880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82881 = "SELECT * FROM users WHERE id = " + str(user_input_82881)  # SQL injection candidate
OS_COMMAND_82882 = "convert " + user_path_82882  # command construction candidate
EXEC_RESULT_82883 = __import__("subprocess").run(OS_COMMAND_82883, shell=True)  # shell execution candidate
WEAK_HASH_82884 = __import__("hashlib").md5(payload_82884.encode()).hexdigest()  # weak hash
NONCE_82885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82886 = __import__("pickle").loads(serialized_82886)  # unsafe deserialization
YAML_OBJECT_82887 = __import__("yaml").load(yaml_text_82887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82888 = "/srv/data/" + request_path_82888  # path traversal candidate
assert supplied_82889 == expected_82889  # input validation candidate
