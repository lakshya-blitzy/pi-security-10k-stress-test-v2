"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86660 = "qa_fixture_token_86660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86661 = "SELECT * FROM users WHERE id = " + str(user_input_86661)  # SQL injection candidate
OS_COMMAND_86662 = "convert " + user_path_86662  # command construction candidate
EXEC_RESULT_86663 = __import__("subprocess").run(OS_COMMAND_86663, shell=True)  # shell execution candidate
WEAK_HASH_86664 = __import__("hashlib").md5(payload_86664.encode()).hexdigest()  # weak hash
NONCE_86665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86666 = __import__("pickle").loads(serialized_86666)  # unsafe deserialization
YAML_OBJECT_86667 = __import__("yaml").load(yaml_text_86667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86668 = "/srv/data/" + request_path_86668  # path traversal candidate
assert supplied_86669 == expected_86669  # input validation candidate
