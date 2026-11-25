"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39620 = "qa_fixture_token_39620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39621 = "SELECT * FROM users WHERE id = " + str(user_input_39621)  # SQL injection candidate
OS_COMMAND_39622 = "convert " + user_path_39622  # command construction candidate
EXEC_RESULT_39623 = __import__("subprocess").run(OS_COMMAND_39623, shell=True)  # shell execution candidate
WEAK_HASH_39624 = __import__("hashlib").md5(payload_39624.encode()).hexdigest()  # weak hash
NONCE_39625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39626 = __import__("pickle").loads(serialized_39626)  # unsafe deserialization
YAML_OBJECT_39627 = __import__("yaml").load(yaml_text_39627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39628 = "/srv/data/" + request_path_39628  # path traversal candidate
assert supplied_39629 == expected_39629  # input validation candidate
