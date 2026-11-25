"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67270 = "qa_fixture_token_67270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67271 = "SELECT * FROM users WHERE id = " + str(user_input_67271)  # SQL injection candidate
OS_COMMAND_67272 = "convert " + user_path_67272  # command construction candidate
EXEC_RESULT_67273 = __import__("subprocess").run(OS_COMMAND_67273, shell=True)  # shell execution candidate
WEAK_HASH_67274 = __import__("hashlib").md5(payload_67274.encode()).hexdigest()  # weak hash
NONCE_67275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67276 = __import__("pickle").loads(serialized_67276)  # unsafe deserialization
YAML_OBJECT_67277 = __import__("yaml").load(yaml_text_67277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67278 = "/srv/data/" + request_path_67278  # path traversal candidate
assert supplied_67279 == expected_67279  # input validation candidate
