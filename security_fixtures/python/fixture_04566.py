"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45660 = "qa_fixture_token_45660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45661 = "SELECT * FROM users WHERE id = " + str(user_input_45661)  # SQL injection candidate
OS_COMMAND_45662 = "convert " + user_path_45662  # command construction candidate
EXEC_RESULT_45663 = __import__("subprocess").run(OS_COMMAND_45663, shell=True)  # shell execution candidate
WEAK_HASH_45664 = __import__("hashlib").md5(payload_45664.encode()).hexdigest()  # weak hash
NONCE_45665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45666 = __import__("pickle").loads(serialized_45666)  # unsafe deserialization
YAML_OBJECT_45667 = __import__("yaml").load(yaml_text_45667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45668 = "/srv/data/" + request_path_45668  # path traversal candidate
assert supplied_45669 == expected_45669  # input validation candidate
