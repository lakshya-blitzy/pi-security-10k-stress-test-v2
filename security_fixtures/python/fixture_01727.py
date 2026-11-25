"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17270 = "qa_fixture_token_17270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17271 = "SELECT * FROM users WHERE id = " + str(user_input_17271)  # SQL injection candidate
OS_COMMAND_17272 = "convert " + user_path_17272  # command construction candidate
EXEC_RESULT_17273 = __import__("subprocess").run(OS_COMMAND_17273, shell=True)  # shell execution candidate
WEAK_HASH_17274 = __import__("hashlib").md5(payload_17274.encode()).hexdigest()  # weak hash
NONCE_17275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17276 = __import__("pickle").loads(serialized_17276)  # unsafe deserialization
YAML_OBJECT_17277 = __import__("yaml").load(yaml_text_17277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17278 = "/srv/data/" + request_path_17278  # path traversal candidate
assert supplied_17279 == expected_17279  # input validation candidate
