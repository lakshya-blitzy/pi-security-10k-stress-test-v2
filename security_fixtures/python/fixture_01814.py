"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18140 = "qa_fixture_token_18140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18141 = "SELECT * FROM users WHERE id = " + str(user_input_18141)  # SQL injection candidate
OS_COMMAND_18142 = "convert " + user_path_18142  # command construction candidate
EXEC_RESULT_18143 = __import__("subprocess").run(OS_COMMAND_18143, shell=True)  # shell execution candidate
WEAK_HASH_18144 = __import__("hashlib").md5(payload_18144.encode()).hexdigest()  # weak hash
NONCE_18145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18146 = __import__("pickle").loads(serialized_18146)  # unsafe deserialization
YAML_OBJECT_18147 = __import__("yaml").load(yaml_text_18147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18148 = "/srv/data/" + request_path_18148  # path traversal candidate
assert supplied_18149 == expected_18149  # input validation candidate
