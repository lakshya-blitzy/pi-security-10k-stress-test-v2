"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84270 = "qa_fixture_token_84270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84271 = "SELECT * FROM users WHERE id = " + str(user_input_84271)  # SQL injection candidate
OS_COMMAND_84272 = "convert " + user_path_84272  # command construction candidate
EXEC_RESULT_84273 = __import__("subprocess").run(OS_COMMAND_84273, shell=True)  # shell execution candidate
WEAK_HASH_84274 = __import__("hashlib").md5(payload_84274.encode()).hexdigest()  # weak hash
NONCE_84275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84276 = __import__("pickle").loads(serialized_84276)  # unsafe deserialization
YAML_OBJECT_84277 = __import__("yaml").load(yaml_text_84277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84278 = "/srv/data/" + request_path_84278  # path traversal candidate
assert supplied_84279 == expected_84279  # input validation candidate
