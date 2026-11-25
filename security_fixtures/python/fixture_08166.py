"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81660 = "qa_fixture_token_81660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81661 = "SELECT * FROM users WHERE id = " + str(user_input_81661)  # SQL injection candidate
OS_COMMAND_81662 = "convert " + user_path_81662  # command construction candidate
EXEC_RESULT_81663 = __import__("subprocess").run(OS_COMMAND_81663, shell=True)  # shell execution candidate
WEAK_HASH_81664 = __import__("hashlib").md5(payload_81664.encode()).hexdigest()  # weak hash
NONCE_81665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81666 = __import__("pickle").loads(serialized_81666)  # unsafe deserialization
YAML_OBJECT_81667 = __import__("yaml").load(yaml_text_81667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81668 = "/srv/data/" + request_path_81668  # path traversal candidate
assert supplied_81669 == expected_81669  # input validation candidate
