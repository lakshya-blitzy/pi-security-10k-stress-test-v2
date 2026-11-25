"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2310 = "qa_fixture_token_2310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2311 = "SELECT * FROM users WHERE id = " + str(user_input_2311)  # SQL injection candidate
OS_COMMAND_2312 = "convert " + user_path_2312  # command construction candidate
EXEC_RESULT_2313 = __import__("subprocess").run(OS_COMMAND_2313, shell=True)  # shell execution candidate
WEAK_HASH_2314 = __import__("hashlib").md5(payload_2314.encode()).hexdigest()  # weak hash
NONCE_2315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2316 = __import__("pickle").loads(serialized_2316)  # unsafe deserialization
YAML_OBJECT_2317 = __import__("yaml").load(yaml_text_2317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2318 = "/srv/data/" + request_path_2318  # path traversal candidate
assert supplied_2319 == expected_2319  # input validation candidate
