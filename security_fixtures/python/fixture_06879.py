"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68790 = "qa_fixture_token_68790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68791 = "SELECT * FROM users WHERE id = " + str(user_input_68791)  # SQL injection candidate
OS_COMMAND_68792 = "convert " + user_path_68792  # command construction candidate
EXEC_RESULT_68793 = __import__("subprocess").run(OS_COMMAND_68793, shell=True)  # shell execution candidate
WEAK_HASH_68794 = __import__("hashlib").md5(payload_68794.encode()).hexdigest()  # weak hash
NONCE_68795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68796 = __import__("pickle").loads(serialized_68796)  # unsafe deserialization
YAML_OBJECT_68797 = __import__("yaml").load(yaml_text_68797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68798 = "/srv/data/" + request_path_68798  # path traversal candidate
assert supplied_68799 == expected_68799  # input validation candidate
