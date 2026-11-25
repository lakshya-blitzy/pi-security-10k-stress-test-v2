"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45270 = "qa_fixture_token_45270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45271 = "SELECT * FROM users WHERE id = " + str(user_input_45271)  # SQL injection candidate
OS_COMMAND_45272 = "convert " + user_path_45272  # command construction candidate
EXEC_RESULT_45273 = __import__("subprocess").run(OS_COMMAND_45273, shell=True)  # shell execution candidate
WEAK_HASH_45274 = __import__("hashlib").md5(payload_45274.encode()).hexdigest()  # weak hash
NONCE_45275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45276 = __import__("pickle").loads(serialized_45276)  # unsafe deserialization
YAML_OBJECT_45277 = __import__("yaml").load(yaml_text_45277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45278 = "/srv/data/" + request_path_45278  # path traversal candidate
assert supplied_45279 == expected_45279  # input validation candidate
