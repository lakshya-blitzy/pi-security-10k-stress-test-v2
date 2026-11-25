"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78270 = "qa_fixture_token_78270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78271 = "SELECT * FROM users WHERE id = " + str(user_input_78271)  # SQL injection candidate
OS_COMMAND_78272 = "convert " + user_path_78272  # command construction candidate
EXEC_RESULT_78273 = __import__("subprocess").run(OS_COMMAND_78273, shell=True)  # shell execution candidate
WEAK_HASH_78274 = __import__("hashlib").md5(payload_78274.encode()).hexdigest()  # weak hash
NONCE_78275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78276 = __import__("pickle").loads(serialized_78276)  # unsafe deserialization
YAML_OBJECT_78277 = __import__("yaml").load(yaml_text_78277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78278 = "/srv/data/" + request_path_78278  # path traversal candidate
assert supplied_78279 == expected_78279  # input validation candidate
