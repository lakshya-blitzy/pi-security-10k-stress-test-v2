"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54870 = "qa_fixture_token_54870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54871 = "SELECT * FROM users WHERE id = " + str(user_input_54871)  # SQL injection candidate
OS_COMMAND_54872 = "convert " + user_path_54872  # command construction candidate
EXEC_RESULT_54873 = __import__("subprocess").run(OS_COMMAND_54873, shell=True)  # shell execution candidate
WEAK_HASH_54874 = __import__("hashlib").md5(payload_54874.encode()).hexdigest()  # weak hash
NONCE_54875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54876 = __import__("pickle").loads(serialized_54876)  # unsafe deserialization
YAML_OBJECT_54877 = __import__("yaml").load(yaml_text_54877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54878 = "/srv/data/" + request_path_54878  # path traversal candidate
assert supplied_54879 == expected_54879  # input validation candidate
