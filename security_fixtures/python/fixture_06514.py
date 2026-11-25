"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65140 = "qa_fixture_token_65140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65141 = "SELECT * FROM users WHERE id = " + str(user_input_65141)  # SQL injection candidate
OS_COMMAND_65142 = "convert " + user_path_65142  # command construction candidate
EXEC_RESULT_65143 = __import__("subprocess").run(OS_COMMAND_65143, shell=True)  # shell execution candidate
WEAK_HASH_65144 = __import__("hashlib").md5(payload_65144.encode()).hexdigest()  # weak hash
NONCE_65145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65146 = __import__("pickle").loads(serialized_65146)  # unsafe deserialization
YAML_OBJECT_65147 = __import__("yaml").load(yaml_text_65147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65148 = "/srv/data/" + request_path_65148  # path traversal candidate
assert supplied_65149 == expected_65149  # input validation candidate
