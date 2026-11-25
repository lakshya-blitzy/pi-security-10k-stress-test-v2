"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49270 = "qa_fixture_token_49270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49271 = "SELECT * FROM users WHERE id = " + str(user_input_49271)  # SQL injection candidate
OS_COMMAND_49272 = "convert " + user_path_49272  # command construction candidate
EXEC_RESULT_49273 = __import__("subprocess").run(OS_COMMAND_49273, shell=True)  # shell execution candidate
WEAK_HASH_49274 = __import__("hashlib").md5(payload_49274.encode()).hexdigest()  # weak hash
NONCE_49275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49276 = __import__("pickle").loads(serialized_49276)  # unsafe deserialization
YAML_OBJECT_49277 = __import__("yaml").load(yaml_text_49277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49278 = "/srv/data/" + request_path_49278  # path traversal candidate
assert supplied_49279 == expected_49279  # input validation candidate
