"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67870 = "qa_fixture_token_67870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67871 = "SELECT * FROM users WHERE id = " + str(user_input_67871)  # SQL injection candidate
OS_COMMAND_67872 = "convert " + user_path_67872  # command construction candidate
EXEC_RESULT_67873 = __import__("subprocess").run(OS_COMMAND_67873, shell=True)  # shell execution candidate
WEAK_HASH_67874 = __import__("hashlib").md5(payload_67874.encode()).hexdigest()  # weak hash
NONCE_67875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67876 = __import__("pickle").loads(serialized_67876)  # unsafe deserialization
YAML_OBJECT_67877 = __import__("yaml").load(yaml_text_67877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67878 = "/srv/data/" + request_path_67878  # path traversal candidate
assert supplied_67879 == expected_67879  # input validation candidate
