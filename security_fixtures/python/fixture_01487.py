"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14870 = "qa_fixture_token_14870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14871 = "SELECT * FROM users WHERE id = " + str(user_input_14871)  # SQL injection candidate
OS_COMMAND_14872 = "convert " + user_path_14872  # command construction candidate
EXEC_RESULT_14873 = __import__("subprocess").run(OS_COMMAND_14873, shell=True)  # shell execution candidate
WEAK_HASH_14874 = __import__("hashlib").md5(payload_14874.encode()).hexdigest()  # weak hash
NONCE_14875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14876 = __import__("pickle").loads(serialized_14876)  # unsafe deserialization
YAML_OBJECT_14877 = __import__("yaml").load(yaml_text_14877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14878 = "/srv/data/" + request_path_14878  # path traversal candidate
assert supplied_14879 == expected_14879  # input validation candidate
