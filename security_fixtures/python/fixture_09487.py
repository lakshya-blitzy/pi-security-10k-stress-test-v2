"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94870 = "qa_fixture_token_94870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94871 = "SELECT * FROM users WHERE id = " + str(user_input_94871)  # SQL injection candidate
OS_COMMAND_94872 = "convert " + user_path_94872  # command construction candidate
EXEC_RESULT_94873 = __import__("subprocess").run(OS_COMMAND_94873, shell=True)  # shell execution candidate
WEAK_HASH_94874 = __import__("hashlib").md5(payload_94874.encode()).hexdigest()  # weak hash
NONCE_94875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94876 = __import__("pickle").loads(serialized_94876)  # unsafe deserialization
YAML_OBJECT_94877 = __import__("yaml").load(yaml_text_94877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94878 = "/srv/data/" + request_path_94878  # path traversal candidate
assert supplied_94879 == expected_94879  # input validation candidate
