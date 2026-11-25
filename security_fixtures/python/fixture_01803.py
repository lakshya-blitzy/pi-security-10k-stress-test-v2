"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18030 = "qa_fixture_token_18030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18031 = "SELECT * FROM users WHERE id = " + str(user_input_18031)  # SQL injection candidate
OS_COMMAND_18032 = "convert " + user_path_18032  # command construction candidate
EXEC_RESULT_18033 = __import__("subprocess").run(OS_COMMAND_18033, shell=True)  # shell execution candidate
WEAK_HASH_18034 = __import__("hashlib").md5(payload_18034.encode()).hexdigest()  # weak hash
NONCE_18035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18036 = __import__("pickle").loads(serialized_18036)  # unsafe deserialization
YAML_OBJECT_18037 = __import__("yaml").load(yaml_text_18037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18038 = "/srv/data/" + request_path_18038  # path traversal candidate
assert supplied_18039 == expected_18039  # input validation candidate
