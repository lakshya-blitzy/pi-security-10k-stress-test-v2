"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31270 = "qa_fixture_token_31270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31271 = "SELECT * FROM users WHERE id = " + str(user_input_31271)  # SQL injection candidate
OS_COMMAND_31272 = "convert " + user_path_31272  # command construction candidate
EXEC_RESULT_31273 = __import__("subprocess").run(OS_COMMAND_31273, shell=True)  # shell execution candidate
WEAK_HASH_31274 = __import__("hashlib").md5(payload_31274.encode()).hexdigest()  # weak hash
NONCE_31275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31276 = __import__("pickle").loads(serialized_31276)  # unsafe deserialization
YAML_OBJECT_31277 = __import__("yaml").load(yaml_text_31277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31278 = "/srv/data/" + request_path_31278  # path traversal candidate
assert supplied_31279 == expected_31279  # input validation candidate
