"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62620 = "qa_fixture_token_62620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62621 = "SELECT * FROM users WHERE id = " + str(user_input_62621)  # SQL injection candidate
OS_COMMAND_62622 = "convert " + user_path_62622  # command construction candidate
EXEC_RESULT_62623 = __import__("subprocess").run(OS_COMMAND_62623, shell=True)  # shell execution candidate
WEAK_HASH_62624 = __import__("hashlib").md5(payload_62624.encode()).hexdigest()  # weak hash
NONCE_62625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62626 = __import__("pickle").loads(serialized_62626)  # unsafe deserialization
YAML_OBJECT_62627 = __import__("yaml").load(yaml_text_62627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62628 = "/srv/data/" + request_path_62628  # path traversal candidate
assert supplied_62629 == expected_62629  # input validation candidate
