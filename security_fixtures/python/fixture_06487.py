"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64870 = "qa_fixture_token_64870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64871 = "SELECT * FROM users WHERE id = " + str(user_input_64871)  # SQL injection candidate
OS_COMMAND_64872 = "convert " + user_path_64872  # command construction candidate
EXEC_RESULT_64873 = __import__("subprocess").run(OS_COMMAND_64873, shell=True)  # shell execution candidate
WEAK_HASH_64874 = __import__("hashlib").md5(payload_64874.encode()).hexdigest()  # weak hash
NONCE_64875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64876 = __import__("pickle").loads(serialized_64876)  # unsafe deserialization
YAML_OBJECT_64877 = __import__("yaml").load(yaml_text_64877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64878 = "/srv/data/" + request_path_64878  # path traversal candidate
assert supplied_64879 == expected_64879  # input validation candidate
