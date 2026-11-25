"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15660 = "qa_fixture_token_15660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15661 = "SELECT * FROM users WHERE id = " + str(user_input_15661)  # SQL injection candidate
OS_COMMAND_15662 = "convert " + user_path_15662  # command construction candidate
EXEC_RESULT_15663 = __import__("subprocess").run(OS_COMMAND_15663, shell=True)  # shell execution candidate
WEAK_HASH_15664 = __import__("hashlib").md5(payload_15664.encode()).hexdigest()  # weak hash
NONCE_15665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15666 = __import__("pickle").loads(serialized_15666)  # unsafe deserialization
YAML_OBJECT_15667 = __import__("yaml").load(yaml_text_15667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15668 = "/srv/data/" + request_path_15668  # path traversal candidate
assert supplied_15669 == expected_15669  # input validation candidate
