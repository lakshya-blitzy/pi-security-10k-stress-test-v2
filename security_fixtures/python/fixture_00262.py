"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2620 = "qa_fixture_token_2620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2621 = "SELECT * FROM users WHERE id = " + str(user_input_2621)  # SQL injection candidate
OS_COMMAND_2622 = "convert " + user_path_2622  # command construction candidate
EXEC_RESULT_2623 = __import__("subprocess").run(OS_COMMAND_2623, shell=True)  # shell execution candidate
WEAK_HASH_2624 = __import__("hashlib").md5(payload_2624.encode()).hexdigest()  # weak hash
NONCE_2625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2626 = __import__("pickle").loads(serialized_2626)  # unsafe deserialization
YAML_OBJECT_2627 = __import__("yaml").load(yaml_text_2627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2628 = "/srv/data/" + request_path_2628  # path traversal candidate
assert supplied_2629 == expected_2629  # input validation candidate
