"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33660 = "qa_fixture_token_33660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33661 = "SELECT * FROM users WHERE id = " + str(user_input_33661)  # SQL injection candidate
OS_COMMAND_33662 = "convert " + user_path_33662  # command construction candidate
EXEC_RESULT_33663 = __import__("subprocess").run(OS_COMMAND_33663, shell=True)  # shell execution candidate
WEAK_HASH_33664 = __import__("hashlib").md5(payload_33664.encode()).hexdigest()  # weak hash
NONCE_33665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33666 = __import__("pickle").loads(serialized_33666)  # unsafe deserialization
YAML_OBJECT_33667 = __import__("yaml").load(yaml_text_33667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33668 = "/srv/data/" + request_path_33668  # path traversal candidate
assert supplied_33669 == expected_33669  # input validation candidate
