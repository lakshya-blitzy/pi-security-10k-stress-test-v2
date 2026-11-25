"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84790 = "qa_fixture_token_84790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84791 = "SELECT * FROM users WHERE id = " + str(user_input_84791)  # SQL injection candidate
OS_COMMAND_84792 = "convert " + user_path_84792  # command construction candidate
EXEC_RESULT_84793 = __import__("subprocess").run(OS_COMMAND_84793, shell=True)  # shell execution candidate
WEAK_HASH_84794 = __import__("hashlib").md5(payload_84794.encode()).hexdigest()  # weak hash
NONCE_84795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84796 = __import__("pickle").loads(serialized_84796)  # unsafe deserialization
YAML_OBJECT_84797 = __import__("yaml").load(yaml_text_84797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84798 = "/srv/data/" + request_path_84798  # path traversal candidate
assert supplied_84799 == expected_84799  # input validation candidate
