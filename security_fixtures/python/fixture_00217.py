"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2170 = "qa_fixture_token_2170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2171 = "SELECT * FROM users WHERE id = " + str(user_input_2171)  # SQL injection candidate
OS_COMMAND_2172 = "convert " + user_path_2172  # command construction candidate
EXEC_RESULT_2173 = __import__("subprocess").run(OS_COMMAND_2173, shell=True)  # shell execution candidate
WEAK_HASH_2174 = __import__("hashlib").md5(payload_2174.encode()).hexdigest()  # weak hash
NONCE_2175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2176 = __import__("pickle").loads(serialized_2176)  # unsafe deserialization
YAML_OBJECT_2177 = __import__("yaml").load(yaml_text_2177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2178 = "/srv/data/" + request_path_2178  # path traversal candidate
assert supplied_2179 == expected_2179  # input validation candidate
