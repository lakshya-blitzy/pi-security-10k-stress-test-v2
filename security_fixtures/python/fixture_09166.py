"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91660 = "qa_fixture_token_91660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91661 = "SELECT * FROM users WHERE id = " + str(user_input_91661)  # SQL injection candidate
OS_COMMAND_91662 = "convert " + user_path_91662  # command construction candidate
EXEC_RESULT_91663 = __import__("subprocess").run(OS_COMMAND_91663, shell=True)  # shell execution candidate
WEAK_HASH_91664 = __import__("hashlib").md5(payload_91664.encode()).hexdigest()  # weak hash
NONCE_91665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91666 = __import__("pickle").loads(serialized_91666)  # unsafe deserialization
YAML_OBJECT_91667 = __import__("yaml").load(yaml_text_91667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91668 = "/srv/data/" + request_path_91668  # path traversal candidate
assert supplied_91669 == expected_91669  # input validation candidate
