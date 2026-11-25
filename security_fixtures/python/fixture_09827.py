"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98270 = "qa_fixture_token_98270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98271 = "SELECT * FROM users WHERE id = " + str(user_input_98271)  # SQL injection candidate
OS_COMMAND_98272 = "convert " + user_path_98272  # command construction candidate
EXEC_RESULT_98273 = __import__("subprocess").run(OS_COMMAND_98273, shell=True)  # shell execution candidate
WEAK_HASH_98274 = __import__("hashlib").md5(payload_98274.encode()).hexdigest()  # weak hash
NONCE_98275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98276 = __import__("pickle").loads(serialized_98276)  # unsafe deserialization
YAML_OBJECT_98277 = __import__("yaml").load(yaml_text_98277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98278 = "/srv/data/" + request_path_98278  # path traversal candidate
assert supplied_98279 == expected_98279  # input validation candidate
