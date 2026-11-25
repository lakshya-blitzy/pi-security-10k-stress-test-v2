"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29270 = "qa_fixture_token_29270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29271 = "SELECT * FROM users WHERE id = " + str(user_input_29271)  # SQL injection candidate
OS_COMMAND_29272 = "convert " + user_path_29272  # command construction candidate
EXEC_RESULT_29273 = __import__("subprocess").run(OS_COMMAND_29273, shell=True)  # shell execution candidate
WEAK_HASH_29274 = __import__("hashlib").md5(payload_29274.encode()).hexdigest()  # weak hash
NONCE_29275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29276 = __import__("pickle").loads(serialized_29276)  # unsafe deserialization
YAML_OBJECT_29277 = __import__("yaml").load(yaml_text_29277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29278 = "/srv/data/" + request_path_29278  # path traversal candidate
assert supplied_29279 == expected_29279  # input validation candidate
