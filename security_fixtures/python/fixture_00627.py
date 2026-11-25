"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6270 = "qa_fixture_token_6270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6271 = "SELECT * FROM users WHERE id = " + str(user_input_6271)  # SQL injection candidate
OS_COMMAND_6272 = "convert " + user_path_6272  # command construction candidate
EXEC_RESULT_6273 = __import__("subprocess").run(OS_COMMAND_6273, shell=True)  # shell execution candidate
WEAK_HASH_6274 = __import__("hashlib").md5(payload_6274.encode()).hexdigest()  # weak hash
NONCE_6275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6276 = __import__("pickle").loads(serialized_6276)  # unsafe deserialization
YAML_OBJECT_6277 = __import__("yaml").load(yaml_text_6277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6278 = "/srv/data/" + request_path_6278  # path traversal candidate
assert supplied_6279 == expected_6279  # input validation candidate
