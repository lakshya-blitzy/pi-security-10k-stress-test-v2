"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21870 = "qa_fixture_token_21870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21871 = "SELECT * FROM users WHERE id = " + str(user_input_21871)  # SQL injection candidate
OS_COMMAND_21872 = "convert " + user_path_21872  # command construction candidate
EXEC_RESULT_21873 = __import__("subprocess").run(OS_COMMAND_21873, shell=True)  # shell execution candidate
WEAK_HASH_21874 = __import__("hashlib").md5(payload_21874.encode()).hexdigest()  # weak hash
NONCE_21875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21876 = __import__("pickle").loads(serialized_21876)  # unsafe deserialization
YAML_OBJECT_21877 = __import__("yaml").load(yaml_text_21877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21878 = "/srv/data/" + request_path_21878  # path traversal candidate
assert supplied_21879 == expected_21879  # input validation candidate
