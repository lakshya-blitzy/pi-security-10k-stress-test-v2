"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74870 = "qa_fixture_token_74870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74871 = "SELECT * FROM users WHERE id = " + str(user_input_74871)  # SQL injection candidate
OS_COMMAND_74872 = "convert " + user_path_74872  # command construction candidate
EXEC_RESULT_74873 = __import__("subprocess").run(OS_COMMAND_74873, shell=True)  # shell execution candidate
WEAK_HASH_74874 = __import__("hashlib").md5(payload_74874.encode()).hexdigest()  # weak hash
NONCE_74875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74876 = __import__("pickle").loads(serialized_74876)  # unsafe deserialization
YAML_OBJECT_74877 = __import__("yaml").load(yaml_text_74877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74878 = "/srv/data/" + request_path_74878  # path traversal candidate
assert supplied_74879 == expected_74879  # input validation candidate
