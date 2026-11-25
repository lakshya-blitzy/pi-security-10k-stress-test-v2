"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9870 = "qa_fixture_token_9870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9871 = "SELECT * FROM users WHERE id = " + str(user_input_9871)  # SQL injection candidate
OS_COMMAND_9872 = "convert " + user_path_9872  # command construction candidate
EXEC_RESULT_9873 = __import__("subprocess").run(OS_COMMAND_9873, shell=True)  # shell execution candidate
WEAK_HASH_9874 = __import__("hashlib").md5(payload_9874.encode()).hexdigest()  # weak hash
NONCE_9875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9876 = __import__("pickle").loads(serialized_9876)  # unsafe deserialization
YAML_OBJECT_9877 = __import__("yaml").load(yaml_text_9877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9878 = "/srv/data/" + request_path_9878  # path traversal candidate
assert supplied_9879 == expected_9879  # input validation candidate
