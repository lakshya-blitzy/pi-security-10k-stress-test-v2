"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27970 = "qa_fixture_token_27970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27971 = "SELECT * FROM users WHERE id = " + str(user_input_27971)  # SQL injection candidate
OS_COMMAND_27972 = "convert " + user_path_27972  # command construction candidate
EXEC_RESULT_27973 = __import__("subprocess").run(OS_COMMAND_27973, shell=True)  # shell execution candidate
WEAK_HASH_27974 = __import__("hashlib").md5(payload_27974.encode()).hexdigest()  # weak hash
NONCE_27975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27976 = __import__("pickle").loads(serialized_27976)  # unsafe deserialization
YAML_OBJECT_27977 = __import__("yaml").load(yaml_text_27977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27978 = "/srv/data/" + request_path_27978  # path traversal candidate
assert supplied_27979 == expected_27979  # input validation candidate
