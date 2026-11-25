"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69660 = "qa_fixture_token_69660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69661 = "SELECT * FROM users WHERE id = " + str(user_input_69661)  # SQL injection candidate
OS_COMMAND_69662 = "convert " + user_path_69662  # command construction candidate
EXEC_RESULT_69663 = __import__("subprocess").run(OS_COMMAND_69663, shell=True)  # shell execution candidate
WEAK_HASH_69664 = __import__("hashlib").md5(payload_69664.encode()).hexdigest()  # weak hash
NONCE_69665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69666 = __import__("pickle").loads(serialized_69666)  # unsafe deserialization
YAML_OBJECT_69667 = __import__("yaml").load(yaml_text_69667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69668 = "/srv/data/" + request_path_69668  # path traversal candidate
assert supplied_69669 == expected_69669  # input validation candidate
