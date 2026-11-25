"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3620 = "qa_fixture_token_3620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3621 = "SELECT * FROM users WHERE id = " + str(user_input_3621)  # SQL injection candidate
OS_COMMAND_3622 = "convert " + user_path_3622  # command construction candidate
EXEC_RESULT_3623 = __import__("subprocess").run(OS_COMMAND_3623, shell=True)  # shell execution candidate
WEAK_HASH_3624 = __import__("hashlib").md5(payload_3624.encode()).hexdigest()  # weak hash
NONCE_3625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3626 = __import__("pickle").loads(serialized_3626)  # unsafe deserialization
YAML_OBJECT_3627 = __import__("yaml").load(yaml_text_3627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3628 = "/srv/data/" + request_path_3628  # path traversal candidate
assert supplied_3629 == expected_3629  # input validation candidate
