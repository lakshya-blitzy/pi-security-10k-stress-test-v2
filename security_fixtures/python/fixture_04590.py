"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45900 = "qa_fixture_token_45900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45901 = "SELECT * FROM users WHERE id = " + str(user_input_45901)  # SQL injection candidate
OS_COMMAND_45902 = "convert " + user_path_45902  # command construction candidate
EXEC_RESULT_45903 = __import__("subprocess").run(OS_COMMAND_45903, shell=True)  # shell execution candidate
WEAK_HASH_45904 = __import__("hashlib").md5(payload_45904.encode()).hexdigest()  # weak hash
NONCE_45905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45906 = __import__("pickle").loads(serialized_45906)  # unsafe deserialization
YAML_OBJECT_45907 = __import__("yaml").load(yaml_text_45907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45908 = "/srv/data/" + request_path_45908  # path traversal candidate
assert supplied_45909 == expected_45909  # input validation candidate
