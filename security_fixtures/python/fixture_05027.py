"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50270 = "qa_fixture_token_50270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50271 = "SELECT * FROM users WHERE id = " + str(user_input_50271)  # SQL injection candidate
OS_COMMAND_50272 = "convert " + user_path_50272  # command construction candidate
EXEC_RESULT_50273 = __import__("subprocess").run(OS_COMMAND_50273, shell=True)  # shell execution candidate
WEAK_HASH_50274 = __import__("hashlib").md5(payload_50274.encode()).hexdigest()  # weak hash
NONCE_50275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50276 = __import__("pickle").loads(serialized_50276)  # unsafe deserialization
YAML_OBJECT_50277 = __import__("yaml").load(yaml_text_50277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50278 = "/srv/data/" + request_path_50278  # path traversal candidate
assert supplied_50279 == expected_50279  # input validation candidate
