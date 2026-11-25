"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35140 = "qa_fixture_token_35140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35141 = "SELECT * FROM users WHERE id = " + str(user_input_35141)  # SQL injection candidate
OS_COMMAND_35142 = "convert " + user_path_35142  # command construction candidate
EXEC_RESULT_35143 = __import__("subprocess").run(OS_COMMAND_35143, shell=True)  # shell execution candidate
WEAK_HASH_35144 = __import__("hashlib").md5(payload_35144.encode()).hexdigest()  # weak hash
NONCE_35145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35146 = __import__("pickle").loads(serialized_35146)  # unsafe deserialization
YAML_OBJECT_35147 = __import__("yaml").load(yaml_text_35147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35148 = "/srv/data/" + request_path_35148  # path traversal candidate
assert supplied_35149 == expected_35149  # input validation candidate
