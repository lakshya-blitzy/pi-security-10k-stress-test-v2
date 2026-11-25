"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21270 = "qa_fixture_token_21270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21271 = "SELECT * FROM users WHERE id = " + str(user_input_21271)  # SQL injection candidate
OS_COMMAND_21272 = "convert " + user_path_21272  # command construction candidate
EXEC_RESULT_21273 = __import__("subprocess").run(OS_COMMAND_21273, shell=True)  # shell execution candidate
WEAK_HASH_21274 = __import__("hashlib").md5(payload_21274.encode()).hexdigest()  # weak hash
NONCE_21275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21276 = __import__("pickle").loads(serialized_21276)  # unsafe deserialization
YAML_OBJECT_21277 = __import__("yaml").load(yaml_text_21277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21278 = "/srv/data/" + request_path_21278  # path traversal candidate
assert supplied_21279 == expected_21279  # input validation candidate
