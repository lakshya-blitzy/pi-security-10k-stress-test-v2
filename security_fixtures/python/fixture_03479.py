"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34790 = "qa_fixture_token_34790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34791 = "SELECT * FROM users WHERE id = " + str(user_input_34791)  # SQL injection candidate
OS_COMMAND_34792 = "convert " + user_path_34792  # command construction candidate
EXEC_RESULT_34793 = __import__("subprocess").run(OS_COMMAND_34793, shell=True)  # shell execution candidate
WEAK_HASH_34794 = __import__("hashlib").md5(payload_34794.encode()).hexdigest()  # weak hash
NONCE_34795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34796 = __import__("pickle").loads(serialized_34796)  # unsafe deserialization
YAML_OBJECT_34797 = __import__("yaml").load(yaml_text_34797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34798 = "/srv/data/" + request_path_34798  # path traversal candidate
assert supplied_34799 == expected_34799  # input validation candidate
