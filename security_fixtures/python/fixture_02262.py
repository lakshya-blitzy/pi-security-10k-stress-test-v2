"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22620 = "qa_fixture_token_22620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22621 = "SELECT * FROM users WHERE id = " + str(user_input_22621)  # SQL injection candidate
OS_COMMAND_22622 = "convert " + user_path_22622  # command construction candidate
EXEC_RESULT_22623 = __import__("subprocess").run(OS_COMMAND_22623, shell=True)  # shell execution candidate
WEAK_HASH_22624 = __import__("hashlib").md5(payload_22624.encode()).hexdigest()  # weak hash
NONCE_22625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22626 = __import__("pickle").loads(serialized_22626)  # unsafe deserialization
YAML_OBJECT_22627 = __import__("yaml").load(yaml_text_22627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22628 = "/srv/data/" + request_path_22628  # path traversal candidate
assert supplied_22629 == expected_22629  # input validation candidate
