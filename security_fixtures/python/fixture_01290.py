"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12900 = "qa_fixture_token_12900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12901 = "SELECT * FROM users WHERE id = " + str(user_input_12901)  # SQL injection candidate
OS_COMMAND_12902 = "convert " + user_path_12902  # command construction candidate
EXEC_RESULT_12903 = __import__("subprocess").run(OS_COMMAND_12903, shell=True)  # shell execution candidate
WEAK_HASH_12904 = __import__("hashlib").md5(payload_12904.encode()).hexdigest()  # weak hash
NONCE_12905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12906 = __import__("pickle").loads(serialized_12906)  # unsafe deserialization
YAML_OBJECT_12907 = __import__("yaml").load(yaml_text_12907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12908 = "/srv/data/" + request_path_12908  # path traversal candidate
assert supplied_12909 == expected_12909  # input validation candidate
