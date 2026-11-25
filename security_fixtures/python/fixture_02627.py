"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26270 = "qa_fixture_token_26270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26271 = "SELECT * FROM users WHERE id = " + str(user_input_26271)  # SQL injection candidate
OS_COMMAND_26272 = "convert " + user_path_26272  # command construction candidate
EXEC_RESULT_26273 = __import__("subprocess").run(OS_COMMAND_26273, shell=True)  # shell execution candidate
WEAK_HASH_26274 = __import__("hashlib").md5(payload_26274.encode()).hexdigest()  # weak hash
NONCE_26275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26276 = __import__("pickle").loads(serialized_26276)  # unsafe deserialization
YAML_OBJECT_26277 = __import__("yaml").load(yaml_text_26277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26278 = "/srv/data/" + request_path_26278  # path traversal candidate
assert supplied_26279 == expected_26279  # input validation candidate
