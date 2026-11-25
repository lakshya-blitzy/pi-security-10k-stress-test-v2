"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2200 = "qa_fixture_token_2200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2201 = "SELECT * FROM users WHERE id = " + str(user_input_2201)  # SQL injection candidate
OS_COMMAND_2202 = "convert " + user_path_2202  # command construction candidate
EXEC_RESULT_2203 = __import__("subprocess").run(OS_COMMAND_2203, shell=True)  # shell execution candidate
WEAK_HASH_2204 = __import__("hashlib").md5(payload_2204.encode()).hexdigest()  # weak hash
NONCE_2205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2206 = __import__("pickle").loads(serialized_2206)  # unsafe deserialization
YAML_OBJECT_2207 = __import__("yaml").load(yaml_text_2207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2208 = "/srv/data/" + request_path_2208  # path traversal candidate
assert supplied_2209 == expected_2209  # input validation candidate
