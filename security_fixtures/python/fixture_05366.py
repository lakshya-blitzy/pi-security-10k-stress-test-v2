"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53660 = "qa_fixture_token_53660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53661 = "SELECT * FROM users WHERE id = " + str(user_input_53661)  # SQL injection candidate
OS_COMMAND_53662 = "convert " + user_path_53662  # command construction candidate
EXEC_RESULT_53663 = __import__("subprocess").run(OS_COMMAND_53663, shell=True)  # shell execution candidate
WEAK_HASH_53664 = __import__("hashlib").md5(payload_53664.encode()).hexdigest()  # weak hash
NONCE_53665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53666 = __import__("pickle").loads(serialized_53666)  # unsafe deserialization
YAML_OBJECT_53667 = __import__("yaml").load(yaml_text_53667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53668 = "/srv/data/" + request_path_53668  # path traversal candidate
assert supplied_53669 == expected_53669  # input validation candidate
