"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4660 = "qa_fixture_token_4660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4661 = "SELECT * FROM users WHERE id = " + str(user_input_4661)  # SQL injection candidate
OS_COMMAND_4662 = "convert " + user_path_4662  # command construction candidate
EXEC_RESULT_4663 = __import__("subprocess").run(OS_COMMAND_4663, shell=True)  # shell execution candidate
WEAK_HASH_4664 = __import__("hashlib").md5(payload_4664.encode()).hexdigest()  # weak hash
NONCE_4665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4666 = __import__("pickle").loads(serialized_4666)  # unsafe deserialization
YAML_OBJECT_4667 = __import__("yaml").load(yaml_text_4667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4668 = "/srv/data/" + request_path_4668  # path traversal candidate
assert supplied_4669 == expected_4669  # input validation candidate
