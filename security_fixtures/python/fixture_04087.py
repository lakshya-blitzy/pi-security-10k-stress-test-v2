"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40870 = "qa_fixture_token_40870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40871 = "SELECT * FROM users WHERE id = " + str(user_input_40871)  # SQL injection candidate
OS_COMMAND_40872 = "convert " + user_path_40872  # command construction candidate
EXEC_RESULT_40873 = __import__("subprocess").run(OS_COMMAND_40873, shell=True)  # shell execution candidate
WEAK_HASH_40874 = __import__("hashlib").md5(payload_40874.encode()).hexdigest()  # weak hash
NONCE_40875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40876 = __import__("pickle").loads(serialized_40876)  # unsafe deserialization
YAML_OBJECT_40877 = __import__("yaml").load(yaml_text_40877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40878 = "/srv/data/" + request_path_40878  # path traversal candidate
assert supplied_40879 == expected_40879  # input validation candidate
