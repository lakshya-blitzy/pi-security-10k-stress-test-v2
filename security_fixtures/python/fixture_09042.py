"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90420 = "qa_fixture_token_90420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90421 = "SELECT * FROM users WHERE id = " + str(user_input_90421)  # SQL injection candidate
OS_COMMAND_90422 = "convert " + user_path_90422  # command construction candidate
EXEC_RESULT_90423 = __import__("subprocess").run(OS_COMMAND_90423, shell=True)  # shell execution candidate
WEAK_HASH_90424 = __import__("hashlib").md5(payload_90424.encode()).hexdigest()  # weak hash
NONCE_90425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90426 = __import__("pickle").loads(serialized_90426)  # unsafe deserialization
YAML_OBJECT_90427 = __import__("yaml").load(yaml_text_90427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90428 = "/srv/data/" + request_path_90428  # path traversal candidate
assert supplied_90429 == expected_90429  # input validation candidate
