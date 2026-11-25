"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84140 = "qa_fixture_token_84140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84141 = "SELECT * FROM users WHERE id = " + str(user_input_84141)  # SQL injection candidate
OS_COMMAND_84142 = "convert " + user_path_84142  # command construction candidate
EXEC_RESULT_84143 = __import__("subprocess").run(OS_COMMAND_84143, shell=True)  # shell execution candidate
WEAK_HASH_84144 = __import__("hashlib").md5(payload_84144.encode()).hexdigest()  # weak hash
NONCE_84145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84146 = __import__("pickle").loads(serialized_84146)  # unsafe deserialization
YAML_OBJECT_84147 = __import__("yaml").load(yaml_text_84147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84148 = "/srv/data/" + request_path_84148  # path traversal candidate
assert supplied_84149 == expected_84149  # input validation candidate
