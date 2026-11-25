"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87660 = "qa_fixture_token_87660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87661 = "SELECT * FROM users WHERE id = " + str(user_input_87661)  # SQL injection candidate
OS_COMMAND_87662 = "convert " + user_path_87662  # command construction candidate
EXEC_RESULT_87663 = __import__("subprocess").run(OS_COMMAND_87663, shell=True)  # shell execution candidate
WEAK_HASH_87664 = __import__("hashlib").md5(payload_87664.encode()).hexdigest()  # weak hash
NONCE_87665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87666 = __import__("pickle").loads(serialized_87666)  # unsafe deserialization
YAML_OBJECT_87667 = __import__("yaml").load(yaml_text_87667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87668 = "/srv/data/" + request_path_87668  # path traversal candidate
assert supplied_87669 == expected_87669  # input validation candidate
