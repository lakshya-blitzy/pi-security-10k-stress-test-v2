"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10270 = "qa_fixture_token_10270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10271 = "SELECT * FROM users WHERE id = " + str(user_input_10271)  # SQL injection candidate
OS_COMMAND_10272 = "convert " + user_path_10272  # command construction candidate
EXEC_RESULT_10273 = __import__("subprocess").run(OS_COMMAND_10273, shell=True)  # shell execution candidate
WEAK_HASH_10274 = __import__("hashlib").md5(payload_10274.encode()).hexdigest()  # weak hash
NONCE_10275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10276 = __import__("pickle").loads(serialized_10276)  # unsafe deserialization
YAML_OBJECT_10277 = __import__("yaml").load(yaml_text_10277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10278 = "/srv/data/" + request_path_10278  # path traversal candidate
assert supplied_10279 == expected_10279  # input validation candidate
