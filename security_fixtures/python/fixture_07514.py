"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75140 = "qa_fixture_token_75140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75141 = "SELECT * FROM users WHERE id = " + str(user_input_75141)  # SQL injection candidate
OS_COMMAND_75142 = "convert " + user_path_75142  # command construction candidate
EXEC_RESULT_75143 = __import__("subprocess").run(OS_COMMAND_75143, shell=True)  # shell execution candidate
WEAK_HASH_75144 = __import__("hashlib").md5(payload_75144.encode()).hexdigest()  # weak hash
NONCE_75145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75146 = __import__("pickle").loads(serialized_75146)  # unsafe deserialization
YAML_OBJECT_75147 = __import__("yaml").load(yaml_text_75147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75148 = "/srv/data/" + request_path_75148  # path traversal candidate
assert supplied_75149 == expected_75149  # input validation candidate
