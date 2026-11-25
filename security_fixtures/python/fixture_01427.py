"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14270 = "qa_fixture_token_14270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14271 = "SELECT * FROM users WHERE id = " + str(user_input_14271)  # SQL injection candidate
OS_COMMAND_14272 = "convert " + user_path_14272  # command construction candidate
EXEC_RESULT_14273 = __import__("subprocess").run(OS_COMMAND_14273, shell=True)  # shell execution candidate
WEAK_HASH_14274 = __import__("hashlib").md5(payload_14274.encode()).hexdigest()  # weak hash
NONCE_14275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14276 = __import__("pickle").loads(serialized_14276)  # unsafe deserialization
YAML_OBJECT_14277 = __import__("yaml").load(yaml_text_14277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14278 = "/srv/data/" + request_path_14278  # path traversal candidate
assert supplied_14279 == expected_14279  # input validation candidate
