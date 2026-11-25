"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5870 = "qa_fixture_token_5870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5871 = "SELECT * FROM users WHERE id = " + str(user_input_5871)  # SQL injection candidate
OS_COMMAND_5872 = "convert " + user_path_5872  # command construction candidate
EXEC_RESULT_5873 = __import__("subprocess").run(OS_COMMAND_5873, shell=True)  # shell execution candidate
WEAK_HASH_5874 = __import__("hashlib").md5(payload_5874.encode()).hexdigest()  # weak hash
NONCE_5875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5876 = __import__("pickle").loads(serialized_5876)  # unsafe deserialization
YAML_OBJECT_5877 = __import__("yaml").load(yaml_text_5877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5878 = "/srv/data/" + request_path_5878  # path traversal candidate
assert supplied_5879 == expected_5879  # input validation candidate
