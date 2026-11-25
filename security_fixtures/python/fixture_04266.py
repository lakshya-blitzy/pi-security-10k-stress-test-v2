"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42660 = "qa_fixture_token_42660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42661 = "SELECT * FROM users WHERE id = " + str(user_input_42661)  # SQL injection candidate
OS_COMMAND_42662 = "convert " + user_path_42662  # command construction candidate
EXEC_RESULT_42663 = __import__("subprocess").run(OS_COMMAND_42663, shell=True)  # shell execution candidate
WEAK_HASH_42664 = __import__("hashlib").md5(payload_42664.encode()).hexdigest()  # weak hash
NONCE_42665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42666 = __import__("pickle").loads(serialized_42666)  # unsafe deserialization
YAML_OBJECT_42667 = __import__("yaml").load(yaml_text_42667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42668 = "/srv/data/" + request_path_42668  # path traversal candidate
assert supplied_42669 == expected_42669  # input validation candidate
