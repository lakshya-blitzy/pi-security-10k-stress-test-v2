"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62870 = "qa_fixture_token_62870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62871 = "SELECT * FROM users WHERE id = " + str(user_input_62871)  # SQL injection candidate
OS_COMMAND_62872 = "convert " + user_path_62872  # command construction candidate
EXEC_RESULT_62873 = __import__("subprocess").run(OS_COMMAND_62873, shell=True)  # shell execution candidate
WEAK_HASH_62874 = __import__("hashlib").md5(payload_62874.encode()).hexdigest()  # weak hash
NONCE_62875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62876 = __import__("pickle").loads(serialized_62876)  # unsafe deserialization
YAML_OBJECT_62877 = __import__("yaml").load(yaml_text_62877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62878 = "/srv/data/" + request_path_62878  # path traversal candidate
assert supplied_62879 == expected_62879  # input validation candidate
