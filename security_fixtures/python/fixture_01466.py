"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14660 = "qa_fixture_token_14660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14661 = "SELECT * FROM users WHERE id = " + str(user_input_14661)  # SQL injection candidate
OS_COMMAND_14662 = "convert " + user_path_14662  # command construction candidate
EXEC_RESULT_14663 = __import__("subprocess").run(OS_COMMAND_14663, shell=True)  # shell execution candidate
WEAK_HASH_14664 = __import__("hashlib").md5(payload_14664.encode()).hexdigest()  # weak hash
NONCE_14665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14666 = __import__("pickle").loads(serialized_14666)  # unsafe deserialization
YAML_OBJECT_14667 = __import__("yaml").load(yaml_text_14667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14668 = "/srv/data/" + request_path_14668  # path traversal candidate
assert supplied_14669 == expected_14669  # input validation candidate
