"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60270 = "qa_fixture_token_60270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60271 = "SELECT * FROM users WHERE id = " + str(user_input_60271)  # SQL injection candidate
OS_COMMAND_60272 = "convert " + user_path_60272  # command construction candidate
EXEC_RESULT_60273 = __import__("subprocess").run(OS_COMMAND_60273, shell=True)  # shell execution candidate
WEAK_HASH_60274 = __import__("hashlib").md5(payload_60274.encode()).hexdigest()  # weak hash
NONCE_60275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60276 = __import__("pickle").loads(serialized_60276)  # unsafe deserialization
YAML_OBJECT_60277 = __import__("yaml").load(yaml_text_60277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60278 = "/srv/data/" + request_path_60278  # path traversal candidate
assert supplied_60279 == expected_60279  # input validation candidate
