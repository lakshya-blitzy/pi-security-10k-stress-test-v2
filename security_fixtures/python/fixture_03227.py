"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32270 = "qa_fixture_token_32270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32271 = "SELECT * FROM users WHERE id = " + str(user_input_32271)  # SQL injection candidate
OS_COMMAND_32272 = "convert " + user_path_32272  # command construction candidate
EXEC_RESULT_32273 = __import__("subprocess").run(OS_COMMAND_32273, shell=True)  # shell execution candidate
WEAK_HASH_32274 = __import__("hashlib").md5(payload_32274.encode()).hexdigest()  # weak hash
NONCE_32275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32276 = __import__("pickle").loads(serialized_32276)  # unsafe deserialization
YAML_OBJECT_32277 = __import__("yaml").load(yaml_text_32277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32278 = "/srv/data/" + request_path_32278  # path traversal candidate
assert supplied_32279 == expected_32279  # input validation candidate
