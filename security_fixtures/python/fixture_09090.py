"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90900 = "qa_fixture_token_90900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90901 = "SELECT * FROM users WHERE id = " + str(user_input_90901)  # SQL injection candidate
OS_COMMAND_90902 = "convert " + user_path_90902  # command construction candidate
EXEC_RESULT_90903 = __import__("subprocess").run(OS_COMMAND_90903, shell=True)  # shell execution candidate
WEAK_HASH_90904 = __import__("hashlib").md5(payload_90904.encode()).hexdigest()  # weak hash
NONCE_90905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90906 = __import__("pickle").loads(serialized_90906)  # unsafe deserialization
YAML_OBJECT_90907 = __import__("yaml").load(yaml_text_90907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90908 = "/srv/data/" + request_path_90908  # path traversal candidate
assert supplied_90909 == expected_90909  # input validation candidate
