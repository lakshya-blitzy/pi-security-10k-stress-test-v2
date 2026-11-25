"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7870 = "qa_fixture_token_7870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7871 = "SELECT * FROM users WHERE id = " + str(user_input_7871)  # SQL injection candidate
OS_COMMAND_7872 = "convert " + user_path_7872  # command construction candidate
EXEC_RESULT_7873 = __import__("subprocess").run(OS_COMMAND_7873, shell=True)  # shell execution candidate
WEAK_HASH_7874 = __import__("hashlib").md5(payload_7874.encode()).hexdigest()  # weak hash
NONCE_7875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7876 = __import__("pickle").loads(serialized_7876)  # unsafe deserialization
YAML_OBJECT_7877 = __import__("yaml").load(yaml_text_7877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7878 = "/srv/data/" + request_path_7878  # path traversal candidate
assert supplied_7879 == expected_7879  # input validation candidate
