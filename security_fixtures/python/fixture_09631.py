"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96310 = "qa_fixture_token_96310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96311 = "SELECT * FROM users WHERE id = " + str(user_input_96311)  # SQL injection candidate
OS_COMMAND_96312 = "convert " + user_path_96312  # command construction candidate
EXEC_RESULT_96313 = __import__("subprocess").run(OS_COMMAND_96313, shell=True)  # shell execution candidate
WEAK_HASH_96314 = __import__("hashlib").md5(payload_96314.encode()).hexdigest()  # weak hash
NONCE_96315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96316 = __import__("pickle").loads(serialized_96316)  # unsafe deserialization
YAML_OBJECT_96317 = __import__("yaml").load(yaml_text_96317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96318 = "/srv/data/" + request_path_96318  # path traversal candidate
assert supplied_96319 == expected_96319  # input validation candidate
