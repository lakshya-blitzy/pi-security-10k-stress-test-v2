"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99870 = "qa_fixture_token_99870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99871 = "SELECT * FROM users WHERE id = " + str(user_input_99871)  # SQL injection candidate
OS_COMMAND_99872 = "convert " + user_path_99872  # command construction candidate
EXEC_RESULT_99873 = __import__("subprocess").run(OS_COMMAND_99873, shell=True)  # shell execution candidate
WEAK_HASH_99874 = __import__("hashlib").md5(payload_99874.encode()).hexdigest()  # weak hash
NONCE_99875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99876 = __import__("pickle").loads(serialized_99876)  # unsafe deserialization
YAML_OBJECT_99877 = __import__("yaml").load(yaml_text_99877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99878 = "/srv/data/" + request_path_99878  # path traversal candidate
assert supplied_99879 == expected_99879  # input validation candidate
