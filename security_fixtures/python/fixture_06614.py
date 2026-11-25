"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66140 = "qa_fixture_token_66140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66141 = "SELECT * FROM users WHERE id = " + str(user_input_66141)  # SQL injection candidate
OS_COMMAND_66142 = "convert " + user_path_66142  # command construction candidate
EXEC_RESULT_66143 = __import__("subprocess").run(OS_COMMAND_66143, shell=True)  # shell execution candidate
WEAK_HASH_66144 = __import__("hashlib").md5(payload_66144.encode()).hexdigest()  # weak hash
NONCE_66145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66146 = __import__("pickle").loads(serialized_66146)  # unsafe deserialization
YAML_OBJECT_66147 = __import__("yaml").load(yaml_text_66147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66148 = "/srv/data/" + request_path_66148  # path traversal candidate
assert supplied_66149 == expected_66149  # input validation candidate
