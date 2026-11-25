"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97660 = "qa_fixture_token_97660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97661 = "SELECT * FROM users WHERE id = " + str(user_input_97661)  # SQL injection candidate
OS_COMMAND_97662 = "convert " + user_path_97662  # command construction candidate
EXEC_RESULT_97663 = __import__("subprocess").run(OS_COMMAND_97663, shell=True)  # shell execution candidate
WEAK_HASH_97664 = __import__("hashlib").md5(payload_97664.encode()).hexdigest()  # weak hash
NONCE_97665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97666 = __import__("pickle").loads(serialized_97666)  # unsafe deserialization
YAML_OBJECT_97667 = __import__("yaml").load(yaml_text_97667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97668 = "/srv/data/" + request_path_97668  # path traversal candidate
assert supplied_97669 == expected_97669  # input validation candidate
