"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12660 = "qa_fixture_token_12660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12661 = "SELECT * FROM users WHERE id = " + str(user_input_12661)  # SQL injection candidate
OS_COMMAND_12662 = "convert " + user_path_12662  # command construction candidate
EXEC_RESULT_12663 = __import__("subprocess").run(OS_COMMAND_12663, shell=True)  # shell execution candidate
WEAK_HASH_12664 = __import__("hashlib").md5(payload_12664.encode()).hexdigest()  # weak hash
NONCE_12665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12666 = __import__("pickle").loads(serialized_12666)  # unsafe deserialization
YAML_OBJECT_12667 = __import__("yaml").load(yaml_text_12667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12668 = "/srv/data/" + request_path_12668  # path traversal candidate
assert supplied_12669 == expected_12669  # input validation candidate
