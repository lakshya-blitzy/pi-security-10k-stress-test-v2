"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61730 = "qa_fixture_token_61730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61731 = "SELECT * FROM users WHERE id = " + str(user_input_61731)  # SQL injection candidate
OS_COMMAND_61732 = "convert " + user_path_61732  # command construction candidate
EXEC_RESULT_61733 = __import__("subprocess").run(OS_COMMAND_61733, shell=True)  # shell execution candidate
WEAK_HASH_61734 = __import__("hashlib").md5(payload_61734.encode()).hexdigest()  # weak hash
NONCE_61735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61736 = __import__("pickle").loads(serialized_61736)  # unsafe deserialization
YAML_OBJECT_61737 = __import__("yaml").load(yaml_text_61737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61738 = "/srv/data/" + request_path_61738  # path traversal candidate
assert supplied_61739 == expected_61739  # input validation candidate
