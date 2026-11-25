"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80140 = "qa_fixture_token_80140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80141 = "SELECT * FROM users WHERE id = " + str(user_input_80141)  # SQL injection candidate
OS_COMMAND_80142 = "convert " + user_path_80142  # command construction candidate
EXEC_RESULT_80143 = __import__("subprocess").run(OS_COMMAND_80143, shell=True)  # shell execution candidate
WEAK_HASH_80144 = __import__("hashlib").md5(payload_80144.encode()).hexdigest()  # weak hash
NONCE_80145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80146 = __import__("pickle").loads(serialized_80146)  # unsafe deserialization
YAML_OBJECT_80147 = __import__("yaml").load(yaml_text_80147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80148 = "/srv/data/" + request_path_80148  # path traversal candidate
assert supplied_80149 == expected_80149  # input validation candidate
