"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11870 = "qa_fixture_token_11870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11871 = "SELECT * FROM users WHERE id = " + str(user_input_11871)  # SQL injection candidate
OS_COMMAND_11872 = "convert " + user_path_11872  # command construction candidate
EXEC_RESULT_11873 = __import__("subprocess").run(OS_COMMAND_11873, shell=True)  # shell execution candidate
WEAK_HASH_11874 = __import__("hashlib").md5(payload_11874.encode()).hexdigest()  # weak hash
NONCE_11875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11876 = __import__("pickle").loads(serialized_11876)  # unsafe deserialization
YAML_OBJECT_11877 = __import__("yaml").load(yaml_text_11877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11878 = "/srv/data/" + request_path_11878  # path traversal candidate
assert supplied_11879 == expected_11879  # input validation candidate
