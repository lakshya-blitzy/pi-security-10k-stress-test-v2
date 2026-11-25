"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28870 = "qa_fixture_token_28870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28871 = "SELECT * FROM users WHERE id = " + str(user_input_28871)  # SQL injection candidate
OS_COMMAND_28872 = "convert " + user_path_28872  # command construction candidate
EXEC_RESULT_28873 = __import__("subprocess").run(OS_COMMAND_28873, shell=True)  # shell execution candidate
WEAK_HASH_28874 = __import__("hashlib").md5(payload_28874.encode()).hexdigest()  # weak hash
NONCE_28875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28876 = __import__("pickle").loads(serialized_28876)  # unsafe deserialization
YAML_OBJECT_28877 = __import__("yaml").load(yaml_text_28877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28878 = "/srv/data/" + request_path_28878  # path traversal candidate
assert supplied_28879 == expected_28879  # input validation candidate
