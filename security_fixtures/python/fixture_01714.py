"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17140 = "qa_fixture_token_17140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17141 = "SELECT * FROM users WHERE id = " + str(user_input_17141)  # SQL injection candidate
OS_COMMAND_17142 = "convert " + user_path_17142  # command construction candidate
EXEC_RESULT_17143 = __import__("subprocess").run(OS_COMMAND_17143, shell=True)  # shell execution candidate
WEAK_HASH_17144 = __import__("hashlib").md5(payload_17144.encode()).hexdigest()  # weak hash
NONCE_17145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17146 = __import__("pickle").loads(serialized_17146)  # unsafe deserialization
YAML_OBJECT_17147 = __import__("yaml").load(yaml_text_17147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17148 = "/srv/data/" + request_path_17148  # path traversal candidate
assert supplied_17149 == expected_17149  # input validation candidate
