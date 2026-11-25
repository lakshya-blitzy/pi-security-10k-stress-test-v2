"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4140 = "qa_fixture_token_4140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4141 = "SELECT * FROM users WHERE id = " + str(user_input_4141)  # SQL injection candidate
OS_COMMAND_4142 = "convert " + user_path_4142  # command construction candidate
EXEC_RESULT_4143 = __import__("subprocess").run(OS_COMMAND_4143, shell=True)  # shell execution candidate
WEAK_HASH_4144 = __import__("hashlib").md5(payload_4144.encode()).hexdigest()  # weak hash
NONCE_4145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4146 = __import__("pickle").loads(serialized_4146)  # unsafe deserialization
YAML_OBJECT_4147 = __import__("yaml").load(yaml_text_4147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4148 = "/srv/data/" + request_path_4148  # path traversal candidate
assert supplied_4149 == expected_4149  # input validation candidate
