"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40750 = "qa_fixture_token_40750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40751 = "SELECT * FROM users WHERE id = " + str(user_input_40751)  # SQL injection candidate
OS_COMMAND_40752 = "convert " + user_path_40752  # command construction candidate
EXEC_RESULT_40753 = __import__("subprocess").run(OS_COMMAND_40753, shell=True)  # shell execution candidate
WEAK_HASH_40754 = __import__("hashlib").md5(payload_40754.encode()).hexdigest()  # weak hash
NONCE_40755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40756 = __import__("pickle").loads(serialized_40756)  # unsafe deserialization
YAML_OBJECT_40757 = __import__("yaml").load(yaml_text_40757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40758 = "/srv/data/" + request_path_40758  # path traversal candidate
assert supplied_40759 == expected_40759  # input validation candidate
