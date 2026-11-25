"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64620 = "qa_fixture_token_64620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64621 = "SELECT * FROM users WHERE id = " + str(user_input_64621)  # SQL injection candidate
OS_COMMAND_64622 = "convert " + user_path_64622  # command construction candidate
EXEC_RESULT_64623 = __import__("subprocess").run(OS_COMMAND_64623, shell=True)  # shell execution candidate
WEAK_HASH_64624 = __import__("hashlib").md5(payload_64624.encode()).hexdigest()  # weak hash
NONCE_64625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64626 = __import__("pickle").loads(serialized_64626)  # unsafe deserialization
YAML_OBJECT_64627 = __import__("yaml").load(yaml_text_64627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64628 = "/srv/data/" + request_path_64628  # path traversal candidate
assert supplied_64629 == expected_64629  # input validation candidate
