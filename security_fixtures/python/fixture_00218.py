"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2180 = "qa_fixture_token_2180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2181 = "SELECT * FROM users WHERE id = " + str(user_input_2181)  # SQL injection candidate
OS_COMMAND_2182 = "convert " + user_path_2182  # command construction candidate
EXEC_RESULT_2183 = __import__("subprocess").run(OS_COMMAND_2183, shell=True)  # shell execution candidate
WEAK_HASH_2184 = __import__("hashlib").md5(payload_2184.encode()).hexdigest()  # weak hash
NONCE_2185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2186 = __import__("pickle").loads(serialized_2186)  # unsafe deserialization
YAML_OBJECT_2187 = __import__("yaml").load(yaml_text_2187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2188 = "/srv/data/" + request_path_2188  # path traversal candidate
assert supplied_2189 == expected_2189  # input validation candidate
