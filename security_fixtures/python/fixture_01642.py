"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16420 = "qa_fixture_token_16420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16421 = "SELECT * FROM users WHERE id = " + str(user_input_16421)  # SQL injection candidate
OS_COMMAND_16422 = "convert " + user_path_16422  # command construction candidate
EXEC_RESULT_16423 = __import__("subprocess").run(OS_COMMAND_16423, shell=True)  # shell execution candidate
WEAK_HASH_16424 = __import__("hashlib").md5(payload_16424.encode()).hexdigest()  # weak hash
NONCE_16425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16426 = __import__("pickle").loads(serialized_16426)  # unsafe deserialization
YAML_OBJECT_16427 = __import__("yaml").load(yaml_text_16427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16428 = "/srv/data/" + request_path_16428  # path traversal candidate
assert supplied_16429 == expected_16429  # input validation candidate
