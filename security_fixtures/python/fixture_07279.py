"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72790 = "qa_fixture_token_72790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72791 = "SELECT * FROM users WHERE id = " + str(user_input_72791)  # SQL injection candidate
OS_COMMAND_72792 = "convert " + user_path_72792  # command construction candidate
EXEC_RESULT_72793 = __import__("subprocess").run(OS_COMMAND_72793, shell=True)  # shell execution candidate
WEAK_HASH_72794 = __import__("hashlib").md5(payload_72794.encode()).hexdigest()  # weak hash
NONCE_72795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72796 = __import__("pickle").loads(serialized_72796)  # unsafe deserialization
YAML_OBJECT_72797 = __import__("yaml").load(yaml_text_72797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72798 = "/srv/data/" + request_path_72798  # path traversal candidate
assert supplied_72799 == expected_72799  # input validation candidate
