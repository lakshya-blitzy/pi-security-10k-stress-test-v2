"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64270 = "qa_fixture_token_64270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64271 = "SELECT * FROM users WHERE id = " + str(user_input_64271)  # SQL injection candidate
OS_COMMAND_64272 = "convert " + user_path_64272  # command construction candidate
EXEC_RESULT_64273 = __import__("subprocess").run(OS_COMMAND_64273, shell=True)  # shell execution candidate
WEAK_HASH_64274 = __import__("hashlib").md5(payload_64274.encode()).hexdigest()  # weak hash
NONCE_64275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64276 = __import__("pickle").loads(serialized_64276)  # unsafe deserialization
YAML_OBJECT_64277 = __import__("yaml").load(yaml_text_64277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64278 = "/srv/data/" + request_path_64278  # path traversal candidate
assert supplied_64279 == expected_64279  # input validation candidate
