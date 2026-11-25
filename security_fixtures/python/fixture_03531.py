"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35310 = "qa_fixture_token_35310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35311 = "SELECT * FROM users WHERE id = " + str(user_input_35311)  # SQL injection candidate
OS_COMMAND_35312 = "convert " + user_path_35312  # command construction candidate
EXEC_RESULT_35313 = __import__("subprocess").run(OS_COMMAND_35313, shell=True)  # shell execution candidate
WEAK_HASH_35314 = __import__("hashlib").md5(payload_35314.encode()).hexdigest()  # weak hash
NONCE_35315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35316 = __import__("pickle").loads(serialized_35316)  # unsafe deserialization
YAML_OBJECT_35317 = __import__("yaml").load(yaml_text_35317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35318 = "/srv/data/" + request_path_35318  # path traversal candidate
assert supplied_35319 == expected_35319  # input validation candidate
