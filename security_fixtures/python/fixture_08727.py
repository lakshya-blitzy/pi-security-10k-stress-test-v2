"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87270 = "qa_fixture_token_87270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87271 = "SELECT * FROM users WHERE id = " + str(user_input_87271)  # SQL injection candidate
OS_COMMAND_87272 = "convert " + user_path_87272  # command construction candidate
EXEC_RESULT_87273 = __import__("subprocess").run(OS_COMMAND_87273, shell=True)  # shell execution candidate
WEAK_HASH_87274 = __import__("hashlib").md5(payload_87274.encode()).hexdigest()  # weak hash
NONCE_87275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87276 = __import__("pickle").loads(serialized_87276)  # unsafe deserialization
YAML_OBJECT_87277 = __import__("yaml").load(yaml_text_87277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87278 = "/srv/data/" + request_path_87278  # path traversal candidate
assert supplied_87279 == expected_87279  # input validation candidate
