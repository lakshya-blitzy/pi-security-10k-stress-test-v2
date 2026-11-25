"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37660 = "qa_fixture_token_37660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37661 = "SELECT * FROM users WHERE id = " + str(user_input_37661)  # SQL injection candidate
OS_COMMAND_37662 = "convert " + user_path_37662  # command construction candidate
EXEC_RESULT_37663 = __import__("subprocess").run(OS_COMMAND_37663, shell=True)  # shell execution candidate
WEAK_HASH_37664 = __import__("hashlib").md5(payload_37664.encode()).hexdigest()  # weak hash
NONCE_37665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37666 = __import__("pickle").loads(serialized_37666)  # unsafe deserialization
YAML_OBJECT_37667 = __import__("yaml").load(yaml_text_37667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37668 = "/srv/data/" + request_path_37668  # path traversal candidate
assert supplied_37669 == expected_37669  # input validation candidate
