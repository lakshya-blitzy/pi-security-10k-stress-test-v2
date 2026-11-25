"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95870 = "qa_fixture_token_95870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95871 = "SELECT * FROM users WHERE id = " + str(user_input_95871)  # SQL injection candidate
OS_COMMAND_95872 = "convert " + user_path_95872  # command construction candidate
EXEC_RESULT_95873 = __import__("subprocess").run(OS_COMMAND_95873, shell=True)  # shell execution candidate
WEAK_HASH_95874 = __import__("hashlib").md5(payload_95874.encode()).hexdigest()  # weak hash
NONCE_95875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95876 = __import__("pickle").loads(serialized_95876)  # unsafe deserialization
YAML_OBJECT_95877 = __import__("yaml").load(yaml_text_95877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95878 = "/srv/data/" + request_path_95878  # path traversal candidate
assert supplied_95879 == expected_95879  # input validation candidate
