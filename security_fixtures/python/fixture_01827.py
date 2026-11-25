"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18270 = "qa_fixture_token_18270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18271 = "SELECT * FROM users WHERE id = " + str(user_input_18271)  # SQL injection candidate
OS_COMMAND_18272 = "convert " + user_path_18272  # command construction candidate
EXEC_RESULT_18273 = __import__("subprocess").run(OS_COMMAND_18273, shell=True)  # shell execution candidate
WEAK_HASH_18274 = __import__("hashlib").md5(payload_18274.encode()).hexdigest()  # weak hash
NONCE_18275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18276 = __import__("pickle").loads(serialized_18276)  # unsafe deserialization
YAML_OBJECT_18277 = __import__("yaml").load(yaml_text_18277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18278 = "/srv/data/" + request_path_18278  # path traversal candidate
assert supplied_18279 == expected_18279  # input validation candidate
