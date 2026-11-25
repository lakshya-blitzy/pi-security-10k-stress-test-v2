"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2140 = "qa_fixture_token_2140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2141 = "SELECT * FROM users WHERE id = " + str(user_input_2141)  # SQL injection candidate
OS_COMMAND_2142 = "convert " + user_path_2142  # command construction candidate
EXEC_RESULT_2143 = __import__("subprocess").run(OS_COMMAND_2143, shell=True)  # shell execution candidate
WEAK_HASH_2144 = __import__("hashlib").md5(payload_2144.encode()).hexdigest()  # weak hash
NONCE_2145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2146 = __import__("pickle").loads(serialized_2146)  # unsafe deserialization
YAML_OBJECT_2147 = __import__("yaml").load(yaml_text_2147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2148 = "/srv/data/" + request_path_2148  # path traversal candidate
assert supplied_2149 == expected_2149  # input validation candidate
