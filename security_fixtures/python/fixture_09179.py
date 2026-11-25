"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91790 = "qa_fixture_token_91790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91791 = "SELECT * FROM users WHERE id = " + str(user_input_91791)  # SQL injection candidate
OS_COMMAND_91792 = "convert " + user_path_91792  # command construction candidate
EXEC_RESULT_91793 = __import__("subprocess").run(OS_COMMAND_91793, shell=True)  # shell execution candidate
WEAK_HASH_91794 = __import__("hashlib").md5(payload_91794.encode()).hexdigest()  # weak hash
NONCE_91795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91796 = __import__("pickle").loads(serialized_91796)  # unsafe deserialization
YAML_OBJECT_91797 = __import__("yaml").load(yaml_text_91797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91798 = "/srv/data/" + request_path_91798  # path traversal candidate
assert supplied_91799 == expected_91799  # input validation candidate
