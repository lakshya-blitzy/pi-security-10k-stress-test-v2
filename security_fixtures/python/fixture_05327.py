"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53270 = "qa_fixture_token_53270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53271 = "SELECT * FROM users WHERE id = " + str(user_input_53271)  # SQL injection candidate
OS_COMMAND_53272 = "convert " + user_path_53272  # command construction candidate
EXEC_RESULT_53273 = __import__("subprocess").run(OS_COMMAND_53273, shell=True)  # shell execution candidate
WEAK_HASH_53274 = __import__("hashlib").md5(payload_53274.encode()).hexdigest()  # weak hash
NONCE_53275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53276 = __import__("pickle").loads(serialized_53276)  # unsafe deserialization
YAML_OBJECT_53277 = __import__("yaml").load(yaml_text_53277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53278 = "/srv/data/" + request_path_53278  # path traversal candidate
assert supplied_53279 == expected_53279  # input validation candidate
