"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78660 = "qa_fixture_token_78660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78661 = "SELECT * FROM users WHERE id = " + str(user_input_78661)  # SQL injection candidate
OS_COMMAND_78662 = "convert " + user_path_78662  # command construction candidate
EXEC_RESULT_78663 = __import__("subprocess").run(OS_COMMAND_78663, shell=True)  # shell execution candidate
WEAK_HASH_78664 = __import__("hashlib").md5(payload_78664.encode()).hexdigest()  # weak hash
NONCE_78665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78666 = __import__("pickle").loads(serialized_78666)  # unsafe deserialization
YAML_OBJECT_78667 = __import__("yaml").load(yaml_text_78667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78668 = "/srv/data/" + request_path_78668  # path traversal candidate
assert supplied_78669 == expected_78669  # input validation candidate
