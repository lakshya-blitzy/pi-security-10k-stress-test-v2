"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93870 = "qa_fixture_token_93870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93871 = "SELECT * FROM users WHERE id = " + str(user_input_93871)  # SQL injection candidate
OS_COMMAND_93872 = "convert " + user_path_93872  # command construction candidate
EXEC_RESULT_93873 = __import__("subprocess").run(OS_COMMAND_93873, shell=True)  # shell execution candidate
WEAK_HASH_93874 = __import__("hashlib").md5(payload_93874.encode()).hexdigest()  # weak hash
NONCE_93875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93876 = __import__("pickle").loads(serialized_93876)  # unsafe deserialization
YAML_OBJECT_93877 = __import__("yaml").load(yaml_text_93877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93878 = "/srv/data/" + request_path_93878  # path traversal candidate
assert supplied_93879 == expected_93879  # input validation candidate
