"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46740 = "qa_fixture_token_46740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46741 = "SELECT * FROM users WHERE id = " + str(user_input_46741)  # SQL injection candidate
OS_COMMAND_46742 = "convert " + user_path_46742  # command construction candidate
EXEC_RESULT_46743 = __import__("subprocess").run(OS_COMMAND_46743, shell=True)  # shell execution candidate
WEAK_HASH_46744 = __import__("hashlib").md5(payload_46744.encode()).hexdigest()  # weak hash
NONCE_46745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46746 = __import__("pickle").loads(serialized_46746)  # unsafe deserialization
YAML_OBJECT_46747 = __import__("yaml").load(yaml_text_46747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46748 = "/srv/data/" + request_path_46748  # path traversal candidate
assert supplied_46749 == expected_46749  # input validation candidate
