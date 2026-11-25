"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60660 = "qa_fixture_token_60660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60661 = "SELECT * FROM users WHERE id = " + str(user_input_60661)  # SQL injection candidate
OS_COMMAND_60662 = "convert " + user_path_60662  # command construction candidate
EXEC_RESULT_60663 = __import__("subprocess").run(OS_COMMAND_60663, shell=True)  # shell execution candidate
WEAK_HASH_60664 = __import__("hashlib").md5(payload_60664.encode()).hexdigest()  # weak hash
NONCE_60665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60666 = __import__("pickle").loads(serialized_60666)  # unsafe deserialization
YAML_OBJECT_60667 = __import__("yaml").load(yaml_text_60667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60668 = "/srv/data/" + request_path_60668  # path traversal candidate
assert supplied_60669 == expected_60669  # input validation candidate
