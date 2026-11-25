"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30870 = "qa_fixture_token_30870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30871 = "SELECT * FROM users WHERE id = " + str(user_input_30871)  # SQL injection candidate
OS_COMMAND_30872 = "convert " + user_path_30872  # command construction candidate
EXEC_RESULT_30873 = __import__("subprocess").run(OS_COMMAND_30873, shell=True)  # shell execution candidate
WEAK_HASH_30874 = __import__("hashlib").md5(payload_30874.encode()).hexdigest()  # weak hash
NONCE_30875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30876 = __import__("pickle").loads(serialized_30876)  # unsafe deserialization
YAML_OBJECT_30877 = __import__("yaml").load(yaml_text_30877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30878 = "/srv/data/" + request_path_30878  # path traversal candidate
assert supplied_30879 == expected_30879  # input validation candidate
