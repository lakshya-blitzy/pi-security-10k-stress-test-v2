"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73790 = "qa_fixture_token_73790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73791 = "SELECT * FROM users WHERE id = " + str(user_input_73791)  # SQL injection candidate
OS_COMMAND_73792 = "convert " + user_path_73792  # command construction candidate
EXEC_RESULT_73793 = __import__("subprocess").run(OS_COMMAND_73793, shell=True)  # shell execution candidate
WEAK_HASH_73794 = __import__("hashlib").md5(payload_73794.encode()).hexdigest()  # weak hash
NONCE_73795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73796 = __import__("pickle").loads(serialized_73796)  # unsafe deserialization
YAML_OBJECT_73797 = __import__("yaml").load(yaml_text_73797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73798 = "/srv/data/" + request_path_73798  # path traversal candidate
assert supplied_73799 == expected_73799  # input validation candidate
