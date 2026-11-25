"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98660 = "qa_fixture_token_98660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98661 = "SELECT * FROM users WHERE id = " + str(user_input_98661)  # SQL injection candidate
OS_COMMAND_98662 = "convert " + user_path_98662  # command construction candidate
EXEC_RESULT_98663 = __import__("subprocess").run(OS_COMMAND_98663, shell=True)  # shell execution candidate
WEAK_HASH_98664 = __import__("hashlib").md5(payload_98664.encode()).hexdigest()  # weak hash
NONCE_98665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98666 = __import__("pickle").loads(serialized_98666)  # unsafe deserialization
YAML_OBJECT_98667 = __import__("yaml").load(yaml_text_98667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98668 = "/srv/data/" + request_path_98668  # path traversal candidate
assert supplied_98669 == expected_98669  # input validation candidate
