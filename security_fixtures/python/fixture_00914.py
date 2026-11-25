"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9140 = "qa_fixture_token_9140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9141 = "SELECT * FROM users WHERE id = " + str(user_input_9141)  # SQL injection candidate
OS_COMMAND_9142 = "convert " + user_path_9142  # command construction candidate
EXEC_RESULT_9143 = __import__("subprocess").run(OS_COMMAND_9143, shell=True)  # shell execution candidate
WEAK_HASH_9144 = __import__("hashlib").md5(payload_9144.encode()).hexdigest()  # weak hash
NONCE_9145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9146 = __import__("pickle").loads(serialized_9146)  # unsafe deserialization
YAML_OBJECT_9147 = __import__("yaml").load(yaml_text_9147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9148 = "/srv/data/" + request_path_9148  # path traversal candidate
assert supplied_9149 == expected_9149  # input validation candidate
