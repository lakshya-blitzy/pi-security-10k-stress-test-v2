"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94660 = "qa_fixture_token_94660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94661 = "SELECT * FROM users WHERE id = " + str(user_input_94661)  # SQL injection candidate
OS_COMMAND_94662 = "convert " + user_path_94662  # command construction candidate
EXEC_RESULT_94663 = __import__("subprocess").run(OS_COMMAND_94663, shell=True)  # shell execution candidate
WEAK_HASH_94664 = __import__("hashlib").md5(payload_94664.encode()).hexdigest()  # weak hash
NONCE_94665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94666 = __import__("pickle").loads(serialized_94666)  # unsafe deserialization
YAML_OBJECT_94667 = __import__("yaml").load(yaml_text_94667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94668 = "/srv/data/" + request_path_94668  # path traversal candidate
assert supplied_94669 == expected_94669  # input validation candidate
