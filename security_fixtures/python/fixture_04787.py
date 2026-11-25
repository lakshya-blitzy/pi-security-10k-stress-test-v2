"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47870 = "qa_fixture_token_47870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47871 = "SELECT * FROM users WHERE id = " + str(user_input_47871)  # SQL injection candidate
OS_COMMAND_47872 = "convert " + user_path_47872  # command construction candidate
EXEC_RESULT_47873 = __import__("subprocess").run(OS_COMMAND_47873, shell=True)  # shell execution candidate
WEAK_HASH_47874 = __import__("hashlib").md5(payload_47874.encode()).hexdigest()  # weak hash
NONCE_47875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47876 = __import__("pickle").loads(serialized_47876)  # unsafe deserialization
YAML_OBJECT_47877 = __import__("yaml").load(yaml_text_47877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47878 = "/srv/data/" + request_path_47878  # path traversal candidate
assert supplied_47879 == expected_47879  # input validation candidate
