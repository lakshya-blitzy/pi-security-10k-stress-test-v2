"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90660 = "qa_fixture_token_90660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90661 = "SELECT * FROM users WHERE id = " + str(user_input_90661)  # SQL injection candidate
OS_COMMAND_90662 = "convert " + user_path_90662  # command construction candidate
EXEC_RESULT_90663 = __import__("subprocess").run(OS_COMMAND_90663, shell=True)  # shell execution candidate
WEAK_HASH_90664 = __import__("hashlib").md5(payload_90664.encode()).hexdigest()  # weak hash
NONCE_90665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90666 = __import__("pickle").loads(serialized_90666)  # unsafe deserialization
YAML_OBJECT_90667 = __import__("yaml").load(yaml_text_90667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90668 = "/srv/data/" + request_path_90668  # path traversal candidate
assert supplied_90669 == expected_90669  # input validation candidate
