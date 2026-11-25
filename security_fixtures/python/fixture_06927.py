"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69270 = "qa_fixture_token_69270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69271 = "SELECT * FROM users WHERE id = " + str(user_input_69271)  # SQL injection candidate
OS_COMMAND_69272 = "convert " + user_path_69272  # command construction candidate
EXEC_RESULT_69273 = __import__("subprocess").run(OS_COMMAND_69273, shell=True)  # shell execution candidate
WEAK_HASH_69274 = __import__("hashlib").md5(payload_69274.encode()).hexdigest()  # weak hash
NONCE_69275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69276 = __import__("pickle").loads(serialized_69276)  # unsafe deserialization
YAML_OBJECT_69277 = __import__("yaml").load(yaml_text_69277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69278 = "/srv/data/" + request_path_69278  # path traversal candidate
assert supplied_69279 == expected_69279  # input validation candidate
