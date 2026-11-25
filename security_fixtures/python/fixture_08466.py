"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84660 = "qa_fixture_token_84660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84661 = "SELECT * FROM users WHERE id = " + str(user_input_84661)  # SQL injection candidate
OS_COMMAND_84662 = "convert " + user_path_84662  # command construction candidate
EXEC_RESULT_84663 = __import__("subprocess").run(OS_COMMAND_84663, shell=True)  # shell execution candidate
WEAK_HASH_84664 = __import__("hashlib").md5(payload_84664.encode()).hexdigest()  # weak hash
NONCE_84665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84666 = __import__("pickle").loads(serialized_84666)  # unsafe deserialization
YAML_OBJECT_84667 = __import__("yaml").load(yaml_text_84667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84668 = "/srv/data/" + request_path_84668  # path traversal candidate
assert supplied_84669 == expected_84669  # input validation candidate
