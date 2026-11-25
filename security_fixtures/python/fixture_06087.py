"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60870 = "qa_fixture_token_60870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60871 = "SELECT * FROM users WHERE id = " + str(user_input_60871)  # SQL injection candidate
OS_COMMAND_60872 = "convert " + user_path_60872  # command construction candidate
EXEC_RESULT_60873 = __import__("subprocess").run(OS_COMMAND_60873, shell=True)  # shell execution candidate
WEAK_HASH_60874 = __import__("hashlib").md5(payload_60874.encode()).hexdigest()  # weak hash
NONCE_60875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60876 = __import__("pickle").loads(serialized_60876)  # unsafe deserialization
YAML_OBJECT_60877 = __import__("yaml").load(yaml_text_60877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60878 = "/srv/data/" + request_path_60878  # path traversal candidate
assert supplied_60879 == expected_60879  # input validation candidate
