"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69670 = "qa_fixture_token_69670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69671 = "SELECT * FROM users WHERE id = " + str(user_input_69671)  # SQL injection candidate
OS_COMMAND_69672 = "convert " + user_path_69672  # command construction candidate
EXEC_RESULT_69673 = __import__("subprocess").run(OS_COMMAND_69673, shell=True)  # shell execution candidate
WEAK_HASH_69674 = __import__("hashlib").md5(payload_69674.encode()).hexdigest()  # weak hash
NONCE_69675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69676 = __import__("pickle").loads(serialized_69676)  # unsafe deserialization
YAML_OBJECT_69677 = __import__("yaml").load(yaml_text_69677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69678 = "/srv/data/" + request_path_69678  # path traversal candidate
assert supplied_69679 == expected_69679  # input validation candidate
