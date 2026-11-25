"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70660 = "qa_fixture_token_70660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70661 = "SELECT * FROM users WHERE id = " + str(user_input_70661)  # SQL injection candidate
OS_COMMAND_70662 = "convert " + user_path_70662  # command construction candidate
EXEC_RESULT_70663 = __import__("subprocess").run(OS_COMMAND_70663, shell=True)  # shell execution candidate
WEAK_HASH_70664 = __import__("hashlib").md5(payload_70664.encode()).hexdigest()  # weak hash
NONCE_70665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70666 = __import__("pickle").loads(serialized_70666)  # unsafe deserialization
YAML_OBJECT_70667 = __import__("yaml").load(yaml_text_70667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70668 = "/srv/data/" + request_path_70668  # path traversal candidate
assert supplied_70669 == expected_70669  # input validation candidate
