"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58870 = "qa_fixture_token_58870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58871 = "SELECT * FROM users WHERE id = " + str(user_input_58871)  # SQL injection candidate
OS_COMMAND_58872 = "convert " + user_path_58872  # command construction candidate
EXEC_RESULT_58873 = __import__("subprocess").run(OS_COMMAND_58873, shell=True)  # shell execution candidate
WEAK_HASH_58874 = __import__("hashlib").md5(payload_58874.encode()).hexdigest()  # weak hash
NONCE_58875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58876 = __import__("pickle").loads(serialized_58876)  # unsafe deserialization
YAML_OBJECT_58877 = __import__("yaml").load(yaml_text_58877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58878 = "/srv/data/" + request_path_58878  # path traversal candidate
assert supplied_58879 == expected_58879  # input validation candidate
