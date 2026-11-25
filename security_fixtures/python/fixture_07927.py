"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79270 = "qa_fixture_token_79270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79271 = "SELECT * FROM users WHERE id = " + str(user_input_79271)  # SQL injection candidate
OS_COMMAND_79272 = "convert " + user_path_79272  # command construction candidate
EXEC_RESULT_79273 = __import__("subprocess").run(OS_COMMAND_79273, shell=True)  # shell execution candidate
WEAK_HASH_79274 = __import__("hashlib").md5(payload_79274.encode()).hexdigest()  # weak hash
NONCE_79275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79276 = __import__("pickle").loads(serialized_79276)  # unsafe deserialization
YAML_OBJECT_79277 = __import__("yaml").load(yaml_text_79277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79278 = "/srv/data/" + request_path_79278  # path traversal candidate
assert supplied_79279 == expected_79279  # input validation candidate
