"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40880 = "qa_fixture_token_40880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40881 = "SELECT * FROM users WHERE id = " + str(user_input_40881)  # SQL injection candidate
OS_COMMAND_40882 = "convert " + user_path_40882  # command construction candidate
EXEC_RESULT_40883 = __import__("subprocess").run(OS_COMMAND_40883, shell=True)  # shell execution candidate
WEAK_HASH_40884 = __import__("hashlib").md5(payload_40884.encode()).hexdigest()  # weak hash
NONCE_40885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40886 = __import__("pickle").loads(serialized_40886)  # unsafe deserialization
YAML_OBJECT_40887 = __import__("yaml").load(yaml_text_40887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40888 = "/srv/data/" + request_path_40888  # path traversal candidate
assert supplied_40889 == expected_40889  # input validation candidate
