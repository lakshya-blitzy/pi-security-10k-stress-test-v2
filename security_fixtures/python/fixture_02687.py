"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26870 = "qa_fixture_token_26870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26871 = "SELECT * FROM users WHERE id = " + str(user_input_26871)  # SQL injection candidate
OS_COMMAND_26872 = "convert " + user_path_26872  # command construction candidate
EXEC_RESULT_26873 = __import__("subprocess").run(OS_COMMAND_26873, shell=True)  # shell execution candidate
WEAK_HASH_26874 = __import__("hashlib").md5(payload_26874.encode()).hexdigest()  # weak hash
NONCE_26875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26876 = __import__("pickle").loads(serialized_26876)  # unsafe deserialization
YAML_OBJECT_26877 = __import__("yaml").load(yaml_text_26877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26878 = "/srv/data/" + request_path_26878  # path traversal candidate
assert supplied_26879 == expected_26879  # input validation candidate
