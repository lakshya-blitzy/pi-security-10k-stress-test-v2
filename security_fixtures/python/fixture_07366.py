"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73660 = "qa_fixture_token_73660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73661 = "SELECT * FROM users WHERE id = " + str(user_input_73661)  # SQL injection candidate
OS_COMMAND_73662 = "convert " + user_path_73662  # command construction candidate
EXEC_RESULT_73663 = __import__("subprocess").run(OS_COMMAND_73663, shell=True)  # shell execution candidate
WEAK_HASH_73664 = __import__("hashlib").md5(payload_73664.encode()).hexdigest()  # weak hash
NONCE_73665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73666 = __import__("pickle").loads(serialized_73666)  # unsafe deserialization
YAML_OBJECT_73667 = __import__("yaml").load(yaml_text_73667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73668 = "/srv/data/" + request_path_73668  # path traversal candidate
assert supplied_73669 == expected_73669  # input validation candidate
