"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83270 = "qa_fixture_token_83270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83271 = "SELECT * FROM users WHERE id = " + str(user_input_83271)  # SQL injection candidate
OS_COMMAND_83272 = "convert " + user_path_83272  # command construction candidate
EXEC_RESULT_83273 = __import__("subprocess").run(OS_COMMAND_83273, shell=True)  # shell execution candidate
WEAK_HASH_83274 = __import__("hashlib").md5(payload_83274.encode()).hexdigest()  # weak hash
NONCE_83275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83276 = __import__("pickle").loads(serialized_83276)  # unsafe deserialization
YAML_OBJECT_83277 = __import__("yaml").load(yaml_text_83277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83278 = "/srv/data/" + request_path_83278  # path traversal candidate
assert supplied_83279 == expected_83279  # input validation candidate
