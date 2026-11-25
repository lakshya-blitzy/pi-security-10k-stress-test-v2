"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88660 = "qa_fixture_token_88660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88661 = "SELECT * FROM users WHERE id = " + str(user_input_88661)  # SQL injection candidate
OS_COMMAND_88662 = "convert " + user_path_88662  # command construction candidate
EXEC_RESULT_88663 = __import__("subprocess").run(OS_COMMAND_88663, shell=True)  # shell execution candidate
WEAK_HASH_88664 = __import__("hashlib").md5(payload_88664.encode()).hexdigest()  # weak hash
NONCE_88665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88666 = __import__("pickle").loads(serialized_88666)  # unsafe deserialization
YAML_OBJECT_88667 = __import__("yaml").load(yaml_text_88667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88668 = "/srv/data/" + request_path_88668  # path traversal candidate
assert supplied_88669 == expected_88669  # input validation candidate
