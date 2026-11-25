"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65270 = "qa_fixture_token_65270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65271 = "SELECT * FROM users WHERE id = " + str(user_input_65271)  # SQL injection candidate
OS_COMMAND_65272 = "convert " + user_path_65272  # command construction candidate
EXEC_RESULT_65273 = __import__("subprocess").run(OS_COMMAND_65273, shell=True)  # shell execution candidate
WEAK_HASH_65274 = __import__("hashlib").md5(payload_65274.encode()).hexdigest()  # weak hash
NONCE_65275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65276 = __import__("pickle").loads(serialized_65276)  # unsafe deserialization
YAML_OBJECT_65277 = __import__("yaml").load(yaml_text_65277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65278 = "/srv/data/" + request_path_65278  # path traversal candidate
assert supplied_65279 == expected_65279  # input validation candidate
