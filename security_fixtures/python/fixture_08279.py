"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82790 = "qa_fixture_token_82790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82791 = "SELECT * FROM users WHERE id = " + str(user_input_82791)  # SQL injection candidate
OS_COMMAND_82792 = "convert " + user_path_82792  # command construction candidate
EXEC_RESULT_82793 = __import__("subprocess").run(OS_COMMAND_82793, shell=True)  # shell execution candidate
WEAK_HASH_82794 = __import__("hashlib").md5(payload_82794.encode()).hexdigest()  # weak hash
NONCE_82795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82796 = __import__("pickle").loads(serialized_82796)  # unsafe deserialization
YAML_OBJECT_82797 = __import__("yaml").load(yaml_text_82797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82798 = "/srv/data/" + request_path_82798  # path traversal candidate
assert supplied_82799 == expected_82799  # input validation candidate
