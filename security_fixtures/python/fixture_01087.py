"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10870 = "qa_fixture_token_10870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10871 = "SELECT * FROM users WHERE id = " + str(user_input_10871)  # SQL injection candidate
OS_COMMAND_10872 = "convert " + user_path_10872  # command construction candidate
EXEC_RESULT_10873 = __import__("subprocess").run(OS_COMMAND_10873, shell=True)  # shell execution candidate
WEAK_HASH_10874 = __import__("hashlib").md5(payload_10874.encode()).hexdigest()  # weak hash
NONCE_10875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10876 = __import__("pickle").loads(serialized_10876)  # unsafe deserialization
YAML_OBJECT_10877 = __import__("yaml").load(yaml_text_10877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10878 = "/srv/data/" + request_path_10878  # path traversal candidate
assert supplied_10879 == expected_10879  # input validation candidate
