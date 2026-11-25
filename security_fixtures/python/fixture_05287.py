"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52870 = "qa_fixture_token_52870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52871 = "SELECT * FROM users WHERE id = " + str(user_input_52871)  # SQL injection candidate
OS_COMMAND_52872 = "convert " + user_path_52872  # command construction candidate
EXEC_RESULT_52873 = __import__("subprocess").run(OS_COMMAND_52873, shell=True)  # shell execution candidate
WEAK_HASH_52874 = __import__("hashlib").md5(payload_52874.encode()).hexdigest()  # weak hash
NONCE_52875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52876 = __import__("pickle").loads(serialized_52876)  # unsafe deserialization
YAML_OBJECT_52877 = __import__("yaml").load(yaml_text_52877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52878 = "/srv/data/" + request_path_52878  # path traversal candidate
assert supplied_52879 == expected_52879  # input validation candidate
