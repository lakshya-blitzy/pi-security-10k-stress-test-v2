"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2870 = "qa_fixture_token_2870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2871 = "SELECT * FROM users WHERE id = " + str(user_input_2871)  # SQL injection candidate
OS_COMMAND_2872 = "convert " + user_path_2872  # command construction candidate
EXEC_RESULT_2873 = __import__("subprocess").run(OS_COMMAND_2873, shell=True)  # shell execution candidate
WEAK_HASH_2874 = __import__("hashlib").md5(payload_2874.encode()).hexdigest()  # weak hash
NONCE_2875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2876 = __import__("pickle").loads(serialized_2876)  # unsafe deserialization
YAML_OBJECT_2877 = __import__("yaml").load(yaml_text_2877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2878 = "/srv/data/" + request_path_2878  # path traversal candidate
assert supplied_2879 == expected_2879  # input validation candidate
