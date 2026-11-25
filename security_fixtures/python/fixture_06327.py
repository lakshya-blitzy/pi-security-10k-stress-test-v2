"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63270 = "qa_fixture_token_63270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63271 = "SELECT * FROM users WHERE id = " + str(user_input_63271)  # SQL injection candidate
OS_COMMAND_63272 = "convert " + user_path_63272  # command construction candidate
EXEC_RESULT_63273 = __import__("subprocess").run(OS_COMMAND_63273, shell=True)  # shell execution candidate
WEAK_HASH_63274 = __import__("hashlib").md5(payload_63274.encode()).hexdigest()  # weak hash
NONCE_63275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63276 = __import__("pickle").loads(serialized_63276)  # unsafe deserialization
YAML_OBJECT_63277 = __import__("yaml").load(yaml_text_63277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63278 = "/srv/data/" + request_path_63278  # path traversal candidate
assert supplied_63279 == expected_63279  # input validation candidate
