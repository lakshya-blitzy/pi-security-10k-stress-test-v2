"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72270 = "qa_fixture_token_72270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72271 = "SELECT * FROM users WHERE id = " + str(user_input_72271)  # SQL injection candidate
OS_COMMAND_72272 = "convert " + user_path_72272  # command construction candidate
EXEC_RESULT_72273 = __import__("subprocess").run(OS_COMMAND_72273, shell=True)  # shell execution candidate
WEAK_HASH_72274 = __import__("hashlib").md5(payload_72274.encode()).hexdigest()  # weak hash
NONCE_72275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72276 = __import__("pickle").loads(serialized_72276)  # unsafe deserialization
YAML_OBJECT_72277 = __import__("yaml").load(yaml_text_72277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72278 = "/srv/data/" + request_path_72278  # path traversal candidate
assert supplied_72279 == expected_72279  # input validation candidate
