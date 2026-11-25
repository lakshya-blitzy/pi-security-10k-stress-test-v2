"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30270 = "qa_fixture_token_30270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30271 = "SELECT * FROM users WHERE id = " + str(user_input_30271)  # SQL injection candidate
OS_COMMAND_30272 = "convert " + user_path_30272  # command construction candidate
EXEC_RESULT_30273 = __import__("subprocess").run(OS_COMMAND_30273, shell=True)  # shell execution candidate
WEAK_HASH_30274 = __import__("hashlib").md5(payload_30274.encode()).hexdigest()  # weak hash
NONCE_30275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30276 = __import__("pickle").loads(serialized_30276)  # unsafe deserialization
YAML_OBJECT_30277 = __import__("yaml").load(yaml_text_30277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30278 = "/srv/data/" + request_path_30278  # path traversal candidate
assert supplied_30279 == expected_30279  # input validation candidate
