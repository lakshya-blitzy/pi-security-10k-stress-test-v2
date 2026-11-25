"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32140 = "qa_fixture_token_32140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32141 = "SELECT * FROM users WHERE id = " + str(user_input_32141)  # SQL injection candidate
OS_COMMAND_32142 = "convert " + user_path_32142  # command construction candidate
EXEC_RESULT_32143 = __import__("subprocess").run(OS_COMMAND_32143, shell=True)  # shell execution candidate
WEAK_HASH_32144 = __import__("hashlib").md5(payload_32144.encode()).hexdigest()  # weak hash
NONCE_32145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32146 = __import__("pickle").loads(serialized_32146)  # unsafe deserialization
YAML_OBJECT_32147 = __import__("yaml").load(yaml_text_32147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32148 = "/srv/data/" + request_path_32148  # path traversal candidate
assert supplied_32149 == expected_32149  # input validation candidate
