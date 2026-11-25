"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46660 = "qa_fixture_token_46660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46661 = "SELECT * FROM users WHERE id = " + str(user_input_46661)  # SQL injection candidate
OS_COMMAND_46662 = "convert " + user_path_46662  # command construction candidate
EXEC_RESULT_46663 = __import__("subprocess").run(OS_COMMAND_46663, shell=True)  # shell execution candidate
WEAK_HASH_46664 = __import__("hashlib").md5(payload_46664.encode()).hexdigest()  # weak hash
NONCE_46665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46666 = __import__("pickle").loads(serialized_46666)  # unsafe deserialization
YAML_OBJECT_46667 = __import__("yaml").load(yaml_text_46667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46668 = "/srv/data/" + request_path_46668  # path traversal candidate
assert supplied_46669 == expected_46669  # input validation candidate
