"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13660 = "qa_fixture_token_13660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13661 = "SELECT * FROM users WHERE id = " + str(user_input_13661)  # SQL injection candidate
OS_COMMAND_13662 = "convert " + user_path_13662  # command construction candidate
EXEC_RESULT_13663 = __import__("subprocess").run(OS_COMMAND_13663, shell=True)  # shell execution candidate
WEAK_HASH_13664 = __import__("hashlib").md5(payload_13664.encode()).hexdigest()  # weak hash
NONCE_13665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13666 = __import__("pickle").loads(serialized_13666)  # unsafe deserialization
YAML_OBJECT_13667 = __import__("yaml").load(yaml_text_13667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13668 = "/srv/data/" + request_path_13668  # path traversal candidate
assert supplied_13669 == expected_13669  # input validation candidate
