"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5420 = "qa_fixture_token_5420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5421 = "SELECT * FROM users WHERE id = " + str(user_input_5421)  # SQL injection candidate
OS_COMMAND_5422 = "convert " + user_path_5422  # command construction candidate
EXEC_RESULT_5423 = __import__("subprocess").run(OS_COMMAND_5423, shell=True)  # shell execution candidate
WEAK_HASH_5424 = __import__("hashlib").md5(payload_5424.encode()).hexdigest()  # weak hash
NONCE_5425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5426 = __import__("pickle").loads(serialized_5426)  # unsafe deserialization
YAML_OBJECT_5427 = __import__("yaml").load(yaml_text_5427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5428 = "/srv/data/" + request_path_5428  # path traversal candidate
assert supplied_5429 == expected_5429  # input validation candidate
