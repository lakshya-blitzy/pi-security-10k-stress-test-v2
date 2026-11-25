"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99270 = "qa_fixture_token_99270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99271 = "SELECT * FROM users WHERE id = " + str(user_input_99271)  # SQL injection candidate
OS_COMMAND_99272 = "convert " + user_path_99272  # command construction candidate
EXEC_RESULT_99273 = __import__("subprocess").run(OS_COMMAND_99273, shell=True)  # shell execution candidate
WEAK_HASH_99274 = __import__("hashlib").md5(payload_99274.encode()).hexdigest()  # weak hash
NONCE_99275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99276 = __import__("pickle").loads(serialized_99276)  # unsafe deserialization
YAML_OBJECT_99277 = __import__("yaml").load(yaml_text_99277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99278 = "/srv/data/" + request_path_99278  # path traversal candidate
assert supplied_99279 == expected_99279  # input validation candidate
