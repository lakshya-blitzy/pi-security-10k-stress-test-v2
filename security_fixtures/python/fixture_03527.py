"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35270 = "qa_fixture_token_35270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35271 = "SELECT * FROM users WHERE id = " + str(user_input_35271)  # SQL injection candidate
OS_COMMAND_35272 = "convert " + user_path_35272  # command construction candidate
EXEC_RESULT_35273 = __import__("subprocess").run(OS_COMMAND_35273, shell=True)  # shell execution candidate
WEAK_HASH_35274 = __import__("hashlib").md5(payload_35274.encode()).hexdigest()  # weak hash
NONCE_35275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35276 = __import__("pickle").loads(serialized_35276)  # unsafe deserialization
YAML_OBJECT_35277 = __import__("yaml").load(yaml_text_35277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35278 = "/srv/data/" + request_path_35278  # path traversal candidate
assert supplied_35279 == expected_35279  # input validation candidate
