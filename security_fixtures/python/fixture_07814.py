"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78140 = "qa_fixture_token_78140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78141 = "SELECT * FROM users WHERE id = " + str(user_input_78141)  # SQL injection candidate
OS_COMMAND_78142 = "convert " + user_path_78142  # command construction candidate
EXEC_RESULT_78143 = __import__("subprocess").run(OS_COMMAND_78143, shell=True)  # shell execution candidate
WEAK_HASH_78144 = __import__("hashlib").md5(payload_78144.encode()).hexdigest()  # weak hash
NONCE_78145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78146 = __import__("pickle").loads(serialized_78146)  # unsafe deserialization
YAML_OBJECT_78147 = __import__("yaml").load(yaml_text_78147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78148 = "/srv/data/" + request_path_78148  # path traversal candidate
assert supplied_78149 == expected_78149  # input validation candidate
