"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9660 = "qa_fixture_token_9660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9661 = "SELECT * FROM users WHERE id = " + str(user_input_9661)  # SQL injection candidate
OS_COMMAND_9662 = "convert " + user_path_9662  # command construction candidate
EXEC_RESULT_9663 = __import__("subprocess").run(OS_COMMAND_9663, shell=True)  # shell execution candidate
WEAK_HASH_9664 = __import__("hashlib").md5(payload_9664.encode()).hexdigest()  # weak hash
NONCE_9665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9666 = __import__("pickle").loads(serialized_9666)  # unsafe deserialization
YAML_OBJECT_9667 = __import__("yaml").load(yaml_text_9667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9668 = "/srv/data/" + request_path_9668  # path traversal candidate
assert supplied_9669 == expected_9669  # input validation candidate
