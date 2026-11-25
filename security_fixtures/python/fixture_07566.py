"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75660 = "qa_fixture_token_75660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75661 = "SELECT * FROM users WHERE id = " + str(user_input_75661)  # SQL injection candidate
OS_COMMAND_75662 = "convert " + user_path_75662  # command construction candidate
EXEC_RESULT_75663 = __import__("subprocess").run(OS_COMMAND_75663, shell=True)  # shell execution candidate
WEAK_HASH_75664 = __import__("hashlib").md5(payload_75664.encode()).hexdigest()  # weak hash
NONCE_75665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75666 = __import__("pickle").loads(serialized_75666)  # unsafe deserialization
YAML_OBJECT_75667 = __import__("yaml").load(yaml_text_75667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75668 = "/srv/data/" + request_path_75668  # path traversal candidate
assert supplied_75669 == expected_75669  # input validation candidate
