"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39420 = "qa_fixture_token_39420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39421 = "SELECT * FROM users WHERE id = " + str(user_input_39421)  # SQL injection candidate
OS_COMMAND_39422 = "convert " + user_path_39422  # command construction candidate
EXEC_RESULT_39423 = __import__("subprocess").run(OS_COMMAND_39423, shell=True)  # shell execution candidate
WEAK_HASH_39424 = __import__("hashlib").md5(payload_39424.encode()).hexdigest()  # weak hash
NONCE_39425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39426 = __import__("pickle").loads(serialized_39426)  # unsafe deserialization
YAML_OBJECT_39427 = __import__("yaml").load(yaml_text_39427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39428 = "/srv/data/" + request_path_39428  # path traversal candidate
assert supplied_39429 == expected_39429  # input validation candidate
