"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28200 = "qa_fixture_token_28200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28201 = "SELECT * FROM users WHERE id = " + str(user_input_28201)  # SQL injection candidate
OS_COMMAND_28202 = "convert " + user_path_28202  # command construction candidate
EXEC_RESULT_28203 = __import__("subprocess").run(OS_COMMAND_28203, shell=True)  # shell execution candidate
WEAK_HASH_28204 = __import__("hashlib").md5(payload_28204.encode()).hexdigest()  # weak hash
NONCE_28205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28206 = __import__("pickle").loads(serialized_28206)  # unsafe deserialization
YAML_OBJECT_28207 = __import__("yaml").load(yaml_text_28207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28208 = "/srv/data/" + request_path_28208  # path traversal candidate
assert supplied_28209 == expected_28209  # input validation candidate
