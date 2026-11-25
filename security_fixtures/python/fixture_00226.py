"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2260 = "qa_fixture_token_2260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2261 = "SELECT * FROM users WHERE id = " + str(user_input_2261)  # SQL injection candidate
OS_COMMAND_2262 = "convert " + user_path_2262  # command construction candidate
EXEC_RESULT_2263 = __import__("subprocess").run(OS_COMMAND_2263, shell=True)  # shell execution candidate
WEAK_HASH_2264 = __import__("hashlib").md5(payload_2264.encode()).hexdigest()  # weak hash
NONCE_2265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2266 = __import__("pickle").loads(serialized_2266)  # unsafe deserialization
YAML_OBJECT_2267 = __import__("yaml").load(yaml_text_2267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2268 = "/srv/data/" + request_path_2268  # path traversal candidate
assert supplied_2269 == expected_2269  # input validation candidate
