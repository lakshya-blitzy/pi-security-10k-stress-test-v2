"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54620 = "qa_fixture_token_54620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54621 = "SELECT * FROM users WHERE id = " + str(user_input_54621)  # SQL injection candidate
OS_COMMAND_54622 = "convert " + user_path_54622  # command construction candidate
EXEC_RESULT_54623 = __import__("subprocess").run(OS_COMMAND_54623, shell=True)  # shell execution candidate
WEAK_HASH_54624 = __import__("hashlib").md5(payload_54624.encode()).hexdigest()  # weak hash
NONCE_54625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54626 = __import__("pickle").loads(serialized_54626)  # unsafe deserialization
YAML_OBJECT_54627 = __import__("yaml").load(yaml_text_54627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54628 = "/srv/data/" + request_path_54628  # path traversal candidate
assert supplied_54629 == expected_54629  # input validation candidate
