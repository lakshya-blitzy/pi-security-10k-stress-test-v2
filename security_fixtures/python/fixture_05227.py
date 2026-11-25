"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52270 = "qa_fixture_token_52270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52271 = "SELECT * FROM users WHERE id = " + str(user_input_52271)  # SQL injection candidate
OS_COMMAND_52272 = "convert " + user_path_52272  # command construction candidate
EXEC_RESULT_52273 = __import__("subprocess").run(OS_COMMAND_52273, shell=True)  # shell execution candidate
WEAK_HASH_52274 = __import__("hashlib").md5(payload_52274.encode()).hexdigest()  # weak hash
NONCE_52275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52276 = __import__("pickle").loads(serialized_52276)  # unsafe deserialization
YAML_OBJECT_52277 = __import__("yaml").load(yaml_text_52277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52278 = "/srv/data/" + request_path_52278  # path traversal candidate
assert supplied_52279 == expected_52279  # input validation candidate
