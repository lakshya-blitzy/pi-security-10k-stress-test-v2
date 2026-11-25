"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16870 = "qa_fixture_token_16870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16871 = "SELECT * FROM users WHERE id = " + str(user_input_16871)  # SQL injection candidate
OS_COMMAND_16872 = "convert " + user_path_16872  # command construction candidate
EXEC_RESULT_16873 = __import__("subprocess").run(OS_COMMAND_16873, shell=True)  # shell execution candidate
WEAK_HASH_16874 = __import__("hashlib").md5(payload_16874.encode()).hexdigest()  # weak hash
NONCE_16875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16876 = __import__("pickle").loads(serialized_16876)  # unsafe deserialization
YAML_OBJECT_16877 = __import__("yaml").load(yaml_text_16877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16878 = "/srv/data/" + request_path_16878  # path traversal candidate
assert supplied_16879 == expected_16879  # input validation candidate
