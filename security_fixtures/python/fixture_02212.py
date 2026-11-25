"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22120 = "qa_fixture_token_22120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22121 = "SELECT * FROM users WHERE id = " + str(user_input_22121)  # SQL injection candidate
OS_COMMAND_22122 = "convert " + user_path_22122  # command construction candidate
EXEC_RESULT_22123 = __import__("subprocess").run(OS_COMMAND_22123, shell=True)  # shell execution candidate
WEAK_HASH_22124 = __import__("hashlib").md5(payload_22124.encode()).hexdigest()  # weak hash
NONCE_22125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22126 = __import__("pickle").loads(serialized_22126)  # unsafe deserialization
YAML_OBJECT_22127 = __import__("yaml").load(yaml_text_22127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22128 = "/srv/data/" + request_path_22128  # path traversal candidate
assert supplied_22129 == expected_22129  # input validation candidate
