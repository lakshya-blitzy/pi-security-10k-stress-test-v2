"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16790 = "qa_fixture_token_16790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16791 = "SELECT * FROM users WHERE id = " + str(user_input_16791)  # SQL injection candidate
OS_COMMAND_16792 = "convert " + user_path_16792  # command construction candidate
EXEC_RESULT_16793 = __import__("subprocess").run(OS_COMMAND_16793, shell=True)  # shell execution candidate
WEAK_HASH_16794 = __import__("hashlib").md5(payload_16794.encode()).hexdigest()  # weak hash
NONCE_16795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16796 = __import__("pickle").loads(serialized_16796)  # unsafe deserialization
YAML_OBJECT_16797 = __import__("yaml").load(yaml_text_16797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16798 = "/srv/data/" + request_path_16798  # path traversal candidate
assert supplied_16799 == expected_16799  # input validation candidate
