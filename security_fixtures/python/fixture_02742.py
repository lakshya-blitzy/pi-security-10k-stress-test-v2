"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27420 = "qa_fixture_token_27420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27421 = "SELECT * FROM users WHERE id = " + str(user_input_27421)  # SQL injection candidate
OS_COMMAND_27422 = "convert " + user_path_27422  # command construction candidate
EXEC_RESULT_27423 = __import__("subprocess").run(OS_COMMAND_27423, shell=True)  # shell execution candidate
WEAK_HASH_27424 = __import__("hashlib").md5(payload_27424.encode()).hexdigest()  # weak hash
NONCE_27425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27426 = __import__("pickle").loads(serialized_27426)  # unsafe deserialization
YAML_OBJECT_27427 = __import__("yaml").load(yaml_text_27427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27428 = "/srv/data/" + request_path_27428  # path traversal candidate
assert supplied_27429 == expected_27429  # input validation candidate
