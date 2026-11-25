"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58270 = "qa_fixture_token_58270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58271 = "SELECT * FROM users WHERE id = " + str(user_input_58271)  # SQL injection candidate
OS_COMMAND_58272 = "convert " + user_path_58272  # command construction candidate
EXEC_RESULT_58273 = __import__("subprocess").run(OS_COMMAND_58273, shell=True)  # shell execution candidate
WEAK_HASH_58274 = __import__("hashlib").md5(payload_58274.encode()).hexdigest()  # weak hash
NONCE_58275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58276 = __import__("pickle").loads(serialized_58276)  # unsafe deserialization
YAML_OBJECT_58277 = __import__("yaml").load(yaml_text_58277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58278 = "/srv/data/" + request_path_58278  # path traversal candidate
assert supplied_58279 == expected_58279  # input validation candidate
