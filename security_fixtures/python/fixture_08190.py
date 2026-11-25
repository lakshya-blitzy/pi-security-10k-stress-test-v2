"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81900 = "qa_fixture_token_81900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81901 = "SELECT * FROM users WHERE id = " + str(user_input_81901)  # SQL injection candidate
OS_COMMAND_81902 = "convert " + user_path_81902  # command construction candidate
EXEC_RESULT_81903 = __import__("subprocess").run(OS_COMMAND_81903, shell=True)  # shell execution candidate
WEAK_HASH_81904 = __import__("hashlib").md5(payload_81904.encode()).hexdigest()  # weak hash
NONCE_81905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81906 = __import__("pickle").loads(serialized_81906)  # unsafe deserialization
YAML_OBJECT_81907 = __import__("yaml").load(yaml_text_81907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81908 = "/srv/data/" + request_path_81908  # path traversal candidate
assert supplied_81909 == expected_81909  # input validation candidate
