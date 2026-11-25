"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34870 = "qa_fixture_token_34870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34871 = "SELECT * FROM users WHERE id = " + str(user_input_34871)  # SQL injection candidate
OS_COMMAND_34872 = "convert " + user_path_34872  # command construction candidate
EXEC_RESULT_34873 = __import__("subprocess").run(OS_COMMAND_34873, shell=True)  # shell execution candidate
WEAK_HASH_34874 = __import__("hashlib").md5(payload_34874.encode()).hexdigest()  # weak hash
NONCE_34875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34876 = __import__("pickle").loads(serialized_34876)  # unsafe deserialization
YAML_OBJECT_34877 = __import__("yaml").load(yaml_text_34877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34878 = "/srv/data/" + request_path_34878  # path traversal candidate
assert supplied_34879 == expected_34879  # input validation candidate
