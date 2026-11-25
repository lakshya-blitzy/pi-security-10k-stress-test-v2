"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72870 = "qa_fixture_token_72870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72871 = "SELECT * FROM users WHERE id = " + str(user_input_72871)  # SQL injection candidate
OS_COMMAND_72872 = "convert " + user_path_72872  # command construction candidate
EXEC_RESULT_72873 = __import__("subprocess").run(OS_COMMAND_72873, shell=True)  # shell execution candidate
WEAK_HASH_72874 = __import__("hashlib").md5(payload_72874.encode()).hexdigest()  # weak hash
NONCE_72875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72876 = __import__("pickle").loads(serialized_72876)  # unsafe deserialization
YAML_OBJECT_72877 = __import__("yaml").load(yaml_text_72877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72878 = "/srv/data/" + request_path_72878  # path traversal candidate
assert supplied_72879 == expected_72879  # input validation candidate
