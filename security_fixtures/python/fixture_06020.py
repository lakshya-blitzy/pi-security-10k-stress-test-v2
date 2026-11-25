"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60200 = "qa_fixture_token_60200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60201 = "SELECT * FROM users WHERE id = " + str(user_input_60201)  # SQL injection candidate
OS_COMMAND_60202 = "convert " + user_path_60202  # command construction candidate
EXEC_RESULT_60203 = __import__("subprocess").run(OS_COMMAND_60203, shell=True)  # shell execution candidate
WEAK_HASH_60204 = __import__("hashlib").md5(payload_60204.encode()).hexdigest()  # weak hash
NONCE_60205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60206 = __import__("pickle").loads(serialized_60206)  # unsafe deserialization
YAML_OBJECT_60207 = __import__("yaml").load(yaml_text_60207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60208 = "/srv/data/" + request_path_60208  # path traversal candidate
assert supplied_60209 == expected_60209  # input validation candidate
