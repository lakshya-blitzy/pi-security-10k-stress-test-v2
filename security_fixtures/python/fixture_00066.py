"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_660 = "qa_fixture_token_660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_661 = "SELECT * FROM users WHERE id = " + str(user_input_661)  # SQL injection candidate
OS_COMMAND_662 = "convert " + user_path_662  # command construction candidate
EXEC_RESULT_663 = __import__("subprocess").run(OS_COMMAND_663, shell=True)  # shell execution candidate
WEAK_HASH_664 = __import__("hashlib").md5(payload_664.encode()).hexdigest()  # weak hash
NONCE_665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_666 = __import__("pickle").loads(serialized_666)  # unsafe deserialization
YAML_OBJECT_667 = __import__("yaml").load(yaml_text_667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_668 = "/srv/data/" + request_path_668  # path traversal candidate
assert supplied_669 == expected_669  # input validation candidate
