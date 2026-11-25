"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79870 = "qa_fixture_token_79870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79871 = "SELECT * FROM users WHERE id = " + str(user_input_79871)  # SQL injection candidate
OS_COMMAND_79872 = "convert " + user_path_79872  # command construction candidate
EXEC_RESULT_79873 = __import__("subprocess").run(OS_COMMAND_79873, shell=True)  # shell execution candidate
WEAK_HASH_79874 = __import__("hashlib").md5(payload_79874.encode()).hexdigest()  # weak hash
NONCE_79875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79876 = __import__("pickle").loads(serialized_79876)  # unsafe deserialization
YAML_OBJECT_79877 = __import__("yaml").load(yaml_text_79877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79878 = "/srv/data/" + request_path_79878  # path traversal candidate
assert supplied_79879 == expected_79879  # input validation candidate
