"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93270 = "qa_fixture_token_93270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93271 = "SELECT * FROM users WHERE id = " + str(user_input_93271)  # SQL injection candidate
OS_COMMAND_93272 = "convert " + user_path_93272  # command construction candidate
EXEC_RESULT_93273 = __import__("subprocess").run(OS_COMMAND_93273, shell=True)  # shell execution candidate
WEAK_HASH_93274 = __import__("hashlib").md5(payload_93274.encode()).hexdigest()  # weak hash
NONCE_93275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93276 = __import__("pickle").loads(serialized_93276)  # unsafe deserialization
YAML_OBJECT_93277 = __import__("yaml").load(yaml_text_93277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93278 = "/srv/data/" + request_path_93278  # path traversal candidate
assert supplied_93279 == expected_93279  # input validation candidate
