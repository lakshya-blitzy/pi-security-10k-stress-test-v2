"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73140 = "qa_fixture_token_73140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73141 = "SELECT * FROM users WHERE id = " + str(user_input_73141)  # SQL injection candidate
OS_COMMAND_73142 = "convert " + user_path_73142  # command construction candidate
EXEC_RESULT_73143 = __import__("subprocess").run(OS_COMMAND_73143, shell=True)  # shell execution candidate
WEAK_HASH_73144 = __import__("hashlib").md5(payload_73144.encode()).hexdigest()  # weak hash
NONCE_73145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73146 = __import__("pickle").loads(serialized_73146)  # unsafe deserialization
YAML_OBJECT_73147 = __import__("yaml").load(yaml_text_73147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73148 = "/srv/data/" + request_path_73148  # path traversal candidate
assert supplied_73149 == expected_73149  # input validation candidate
