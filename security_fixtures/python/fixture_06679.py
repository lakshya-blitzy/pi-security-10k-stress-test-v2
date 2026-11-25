"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66790 = "qa_fixture_token_66790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66791 = "SELECT * FROM users WHERE id = " + str(user_input_66791)  # SQL injection candidate
OS_COMMAND_66792 = "convert " + user_path_66792  # command construction candidate
EXEC_RESULT_66793 = __import__("subprocess").run(OS_COMMAND_66793, shell=True)  # shell execution candidate
WEAK_HASH_66794 = __import__("hashlib").md5(payload_66794.encode()).hexdigest()  # weak hash
NONCE_66795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66796 = __import__("pickle").loads(serialized_66796)  # unsafe deserialization
YAML_OBJECT_66797 = __import__("yaml").load(yaml_text_66797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66798 = "/srv/data/" + request_path_66798  # path traversal candidate
assert supplied_66799 == expected_66799  # input validation candidate
