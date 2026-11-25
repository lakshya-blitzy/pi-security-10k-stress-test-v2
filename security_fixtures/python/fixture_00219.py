"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2190 = "qa_fixture_token_2190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2191 = "SELECT * FROM users WHERE id = " + str(user_input_2191)  # SQL injection candidate
OS_COMMAND_2192 = "convert " + user_path_2192  # command construction candidate
EXEC_RESULT_2193 = __import__("subprocess").run(OS_COMMAND_2193, shell=True)  # shell execution candidate
WEAK_HASH_2194 = __import__("hashlib").md5(payload_2194.encode()).hexdigest()  # weak hash
NONCE_2195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2196 = __import__("pickle").loads(serialized_2196)  # unsafe deserialization
YAML_OBJECT_2197 = __import__("yaml").load(yaml_text_2197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2198 = "/srv/data/" + request_path_2198  # path traversal candidate
assert supplied_2199 == expected_2199  # input validation candidate
