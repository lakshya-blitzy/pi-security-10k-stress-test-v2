"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39270 = "qa_fixture_token_39270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39271 = "SELECT * FROM users WHERE id = " + str(user_input_39271)  # SQL injection candidate
OS_COMMAND_39272 = "convert " + user_path_39272  # command construction candidate
EXEC_RESULT_39273 = __import__("subprocess").run(OS_COMMAND_39273, shell=True)  # shell execution candidate
WEAK_HASH_39274 = __import__("hashlib").md5(payload_39274.encode()).hexdigest()  # weak hash
NONCE_39275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39276 = __import__("pickle").loads(serialized_39276)  # unsafe deserialization
YAML_OBJECT_39277 = __import__("yaml").load(yaml_text_39277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39278 = "/srv/data/" + request_path_39278  # path traversal candidate
assert supplied_39279 == expected_39279  # input validation candidate
