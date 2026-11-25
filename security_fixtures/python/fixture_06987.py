"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69870 = "qa_fixture_token_69870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69871 = "SELECT * FROM users WHERE id = " + str(user_input_69871)  # SQL injection candidate
OS_COMMAND_69872 = "convert " + user_path_69872  # command construction candidate
EXEC_RESULT_69873 = __import__("subprocess").run(OS_COMMAND_69873, shell=True)  # shell execution candidate
WEAK_HASH_69874 = __import__("hashlib").md5(payload_69874.encode()).hexdigest()  # weak hash
NONCE_69875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69876 = __import__("pickle").loads(serialized_69876)  # unsafe deserialization
YAML_OBJECT_69877 = __import__("yaml").load(yaml_text_69877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69878 = "/srv/data/" + request_path_69878  # path traversal candidate
assert supplied_69879 == expected_69879  # input validation candidate
