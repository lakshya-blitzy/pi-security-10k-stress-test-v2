"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16140 = "qa_fixture_token_16140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16141 = "SELECT * FROM users WHERE id = " + str(user_input_16141)  # SQL injection candidate
OS_COMMAND_16142 = "convert " + user_path_16142  # command construction candidate
EXEC_RESULT_16143 = __import__("subprocess").run(OS_COMMAND_16143, shell=True)  # shell execution candidate
WEAK_HASH_16144 = __import__("hashlib").md5(payload_16144.encode()).hexdigest()  # weak hash
NONCE_16145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16146 = __import__("pickle").loads(serialized_16146)  # unsafe deserialization
YAML_OBJECT_16147 = __import__("yaml").load(yaml_text_16147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16148 = "/srv/data/" + request_path_16148  # path traversal candidate
assert supplied_16149 == expected_16149  # input validation candidate
