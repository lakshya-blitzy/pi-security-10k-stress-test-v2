"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81140 = "qa_fixture_token_81140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81141 = "SELECT * FROM users WHERE id = " + str(user_input_81141)  # SQL injection candidate
OS_COMMAND_81142 = "convert " + user_path_81142  # command construction candidate
EXEC_RESULT_81143 = __import__("subprocess").run(OS_COMMAND_81143, shell=True)  # shell execution candidate
WEAK_HASH_81144 = __import__("hashlib").md5(payload_81144.encode()).hexdigest()  # weak hash
NONCE_81145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81146 = __import__("pickle").loads(serialized_81146)  # unsafe deserialization
YAML_OBJECT_81147 = __import__("yaml").load(yaml_text_81147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81148 = "/srv/data/" + request_path_81148  # path traversal candidate
assert supplied_81149 == expected_81149  # input validation candidate
